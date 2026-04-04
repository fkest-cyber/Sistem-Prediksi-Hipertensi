# CARA MENJALANKAN APLIKASI TANPA VS CODE

## 🚀 METODE 1: Double-Click File Batch (TERMUDAH)

### Langkah-langkah:
1. **Buka File Explorer**
2. **Navigasi ke:** `d:\project python rudi bima 2026\`
3. **Double-click file:** `JALANKAN_APLIKASI.bat`
4. **Tunggu:** Browser akan otomatis terbuka di `http://localhost:8501`
5. **Selesai!** Aplikasi siap digunakan

### Catatan Penting:
- ❌ **JANGAN TUTUP** jendela Command Prompt yang muncul
- Untuk stop aplikasi: Tekan `Ctrl+C` di jendela Command Prompt, atau tutup jendela tersebut
- Jika browser tidak otomatis buka: Manual buka browser dan ketik `http://localhost:8501`

---

## 💻 METODE 2: Command Prompt Manual

### Langkah-langkah:
1. **Tekan tombol Windows** atau klik Start Menu
2. **Ketik:** `cmd` atau `PowerShell`
3. **Enter** untuk buka Command Prompt
4. **Ketik perintah berikut:**
   ```
   cd /d "d:\project python rudi bima 2026"
   streamlit run app.py
   ```
5. **Tekan Enter**
6. **Buka browser** → ketik: `http://localhost:8501`

---

## 🖱️ METODE 3: Shortcut Desktop

### Cara Buat Shortcut:
1. **Klik kanan di Desktop** → Pilih `New` → `Shortcut`
2. **Di "Type the location"**, masukkan:
   ```
   "d:\project python rudi bima 2026\JALANKAN_APLIKASI.bat"
   ```
3. **Klik Next**
4. **Nama shortcut:** `Prediksi Hipertensi`
5. **Klik Finish**

### Cara Pakai:
- **Double-click** icon shortcut di desktop
- Aplikasi akan langsung jalan
- Browser otomatis buka

---

## ☁️ METODE 4: Deploy ke Cloud (Akses dari Mana Saja)

### Streamlit Cloud (GRATIS):
**Keuntungan:**
- ✅ Akses dari HP/laptop mana saja
- ✅ Tidak perlu install Python
- ✅ Tidak perlu jalankan manual
- ✅ URL permanen (misal: `https://hipertensi-prediksi.streamlit.app`)

**Langkah Deploy:**
1. **Upload code ke GitHub:**
   - Buat akun GitHub (gratis): https://github.com
   - Upload folder project
   
2. **Deploy ke Streamlit Cloud:**
   - Daftar di https://streamlit.io/cloud (gratis)
   - Klik "New app"
   - Connect GitHub repository
   - Pilih file `app.py`
   - Klik "Deploy"
   
3. **Selesai!** Dapatkan URL publik yang bisa dibagikan

---

## 📱 METODE 5: Akses dari HP/Laptop Lain (Jaringan Lokal)

### Jika aplikasi sudah jalan di komputer:
1. **Cari IP komputer:**
   - Buka Command Prompt
   - Ketik: `ipconfig`
   - Lihat IPv4 Address (contoh: `192.168.1.9`)

2. **Di HP/laptop lain (WiFi sama):**
   - Buka browser
   - Ketik: `http://[IP-KOMPUTER]:8501`
   - Contoh: `http://192.168.1.9:8501`

---

## 🔧 TROUBLESHOOTING

### Masalah: "streamlit: command not found"
**Solusi:**
```cmd
pip install streamlit
```

### Masalah: Port 8501 sudah digunakan
**Solusi 1 - Ganti port:**
```cmd
streamlit run app.py --server.port 8502
```

**Solusi 2 - Kill process yang ada:**
```cmd
netstat -ano | findstr :8501
taskkill /PID [PROCESS_ID] /F
```

### Masalah: Browser tidak otomatis buka
**Solusi:**
- Manual buka browser (Chrome/Firefox)
- Ketik URL: `http://localhost:8501`

### Masalah: Model tidak ditemukan
**Pastikan file ada:**
```cmd
dir "d:\project python rudi bima 2026\model_hipertensi.pkl"
```
Jika tidak ada, model perlu di-train ulang.

---

## 📋 CHECKLIST SEBELUM JALANKAN

✅ Python sudah terinstall (minimal 3.8)
✅ Library terinstall: streamlit, pandas, numpy, scikit-learn, plotly
✅ File `app.py` ada di folder
✅ File `model_hipertensi.pkl` ada di folder yang sama
✅ Tidak ada aplikasi lain yang pakai port 8501

---

## 🎯 REKOMENDASI

**Untuk penggunaan pribadi/testing:**
→ Gunakan **METODE 1** (batch file) - paling mudah

**Untuk demo/presentasi:**
→ Gunakan **METODE 3** (shortcut desktop) - lebih profesional

**Untuk produksi/akses publik:**
→ Gunakan **METODE 4** (Streamlit Cloud) - gratis & accessible

**Untuk akses multi-device lokal:**
→ Gunakan **METODE 5** (network access) - praktis untuk kantor/rumah

---

## 📞 BANTUAN LEBIH LANJUT

Jika ada masalah:
1. Cek file `JALANKAN_APLIKASI.bat` bisa di-klik
2. Pastikan path folder benar: `d:\project python rudi bima 2026\`
3. Test manual di Command Prompt dulu
4. Cek log error di terminal window

**Semua sudah siap!** Tinggal double-click `JALANKAN_APLIKASI.bat` 🚀
