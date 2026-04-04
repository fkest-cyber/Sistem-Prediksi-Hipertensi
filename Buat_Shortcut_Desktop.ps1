# ========================================
#   SCRIPT OTOMATIS BUAT SHORTCUT DESKTOP
# ========================================
# Cara Pakai: Right-click file ini → "Run with PowerShell"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  MEMBUAT SHORTCUT DI DESKTOP" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Path ke batch file
$batchFilePath = "d:\project python rudi bima 2026\JALANKAN_APLIKASI.bat"

# Path ke Desktop
$desktopPath = [Environment]::GetFolderPath("Desktop")
$shortcutPath = "$desktopPath\Prediksi Hipertensi.lnk"

Write-Host "📂 Lokasi batch file: $batchFilePath" -ForegroundColor Yellow
Write-Host "🖥️  Desktop path: $desktopPath" -ForegroundColor Yellow
Write-Host "🔗 Shortcut akan dibuat: $shortcutPath" -ForegroundColor Yellow
Write-Host ""

# Cek apakah batch file ada
if (!(Test-Path $batchFilePath)) {
    Write-Host "❌ ERROR: File JALANKAN_APLIKASI.bat tidak ditemukan!" -ForegroundColor Red
    Write-Host "   Pastikan file ada di: $batchFilePath" -ForegroundColor Red
    Write-Host ""
    Write-Host "Tekan Enter untuk keluar..."
    Read-Host
    exit
}

# Buat shortcut
Write-Host "⏳ Membuat shortcut..." -ForegroundColor Green

$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcutPath)
$Shortcut.TargetPath = $batchFilePath
$Shortcut.WorkingDirectory = "d:\project python rudi bima 2026"
$Shortcut.WindowStyle = 1  # Normal window
$Shortcut.Description = "Sistem Prediksi Risiko Hipertensi - Machine Learning"
$Shortcut.IconLocation = "C:\Windows\System32\SHELL32.dll,71"  # Medical icon
$Shortcut.Save()

Write-Host ""
Write-Host "✅ SHORTCUT BERHASIL DIBUAT!" -ForegroundColor Green
Write-Host ""
Write-Host "📍 Lokasi shortcut: $shortcutPath" -ForegroundColor Cyan
Write-Host ""
Write-Host "Cara Pakai:" -ForegroundColor Yellow
Write-Host "  1. Cari icon 'Prediksi Hipertensi' di Desktop Anda" -ForegroundColor White
Write-Host "  2. Double-click untuk menjalankan aplikasi" -ForegroundColor White
Write-Host "  3. Browser akan otomatis terbuka dengan aplikasi" -ForegroundColor White
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Tekan Enter untuk keluar..."
Read-Host
