@echo off
REM ========================================
REM SCRIPT UNTUK MENJALANKAN APLIKASI
REM Sistem Prediksi Risiko Hipertensi
REM ========================================
setlocal enableextensions

echo.
echo ========================================
echo   SISTEM PREDIKSI RISIKO HIPERTENSI
echo ========================================
echo.
echo Menyiapkan aplikasi...
echo.

REM Pindah ke direktori script ini (portabel untuk komputer lain)
cd /d "%~dp0"

REM Cek file penting
if not exist "app.py" (
	echo [ERROR] File app.py tidak ditemukan.
	goto :end
)
if not exist "model_hipertensi.pkl" (
	echo [ERROR] File model_hipertensi.pkl tidak ditemukan.
	goto :end
)

REM Pilih executable Python yang tersedia
set "PYEXE="
where py >nul 2>nul
if %errorlevel%==0 (
	set "PYEXE=py -3"
) else (
	where python >nul 2>nul
	if %errorlevel%==0 (
		set "PYEXE=python"
	)
)

if "%PYEXE%"=="" (
	echo [ERROR] Python tidak ditemukan. Install Python 3.10+ terlebih dahulu.
	goto :end
)

REM Buat virtual environment jika belum ada
if not exist ".venv\Scripts\python.exe" (
	echo Membuat virtual environment .venv ...
	call %PYEXE% -m venv .venv
	if errorlevel 1 (
		echo [ERROR] Gagal membuat virtual environment.
		goto :end
	)
)

REM Upgrade pip dan install dependency
echo Menginstall dependency (jika belum terpasang) ...
call ".venv\Scripts\python.exe" -m pip install --upgrade pip
call ".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (
	echo [ERROR] Gagal install dependency.
	goto :end
)

REM Pilih port: 8501, fallback 8502 jika sedang dipakai
set "PORT=8501"
netstat -ano | findstr ":8501" >nul
if %errorlevel%==0 set "PORT=8502"
if "%PORT%"=="8502" (
	netstat -ano | findstr ":8502" >nul
	if %errorlevel%==0 set "PORT=8503"
)

REM Jalankan Streamlit (tanpa prompt email)
echo Membuka browser otomatis...
echo URL: http://localhost:%PORT%
echo.
echo CATATAN: Jangan tutup jendela ini!
echo Tekan Ctrl+C untuk menghentikan aplikasi.
echo.

call ".venv\Scripts\python.exe" -m streamlit run app.py --server.headless true --server.address 0.0.0.0 --server.port %PORT%

:end
pause
