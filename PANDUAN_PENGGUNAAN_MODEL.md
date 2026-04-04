# 📋 PANDUAN LENGKAP PENGGUNAAN MODEL PREDIKSI HIPERTENSI

## 🎯 Ringkasan Model
- **Nama Model**: Gradient Boosting Classifier
- **File Model**: `model_hipertensi.pkl` (143.20 KB)
- **Akurasi**: 97.98%
- **F1-Score**: 98.05%
- **ROC-AUC**: 99.84%

---

## 📦 Cara Menggunakan Model (5 Langkah Mudah)

### **STEP 1: Import Library yang Diperlukan**

```python
import pickle
import pandas as pd
```

### **STEP 2: Load Model dari File**

```python
# Buka file model
with open('model_hipertensi.pkl', 'rb') as file:
    model = pickle.load(file)

print("✓ Model berhasil di-load!")
```

### **STEP 3: Siapkan Data Pasien**

Data harus memiliki **10 fitur** berikut:

```python
data_pasien = {
    'Age': 52,                          # Usia pasien (tahun)
    'Salt_Intake': 11.5,                # Asupan garam (g/hari)
    'Stress_Score': 7,                  # Skor stress (0-10)
    'BP_History': 'Prehypertension',    # Riwayat tekanan darah
    'Sleep_Duration': 5.5,              # Durasi tidur (jam/hari)
    'BMI': 29.5,                        # Body Mass Index
    'Medication': 'Beta Blocker',       # Jenis medikasi
    'Family_History': 'Yes',            # Riwayat keluarga (Yes/No)
    'Exercise_Level': 'Low',            # Level olahraga
    'Smoking_Status': 'Ex-Smoker'       # Status merokok
}
```

**Nilai-nilai yang Valid:**

| Fitur | Tipe Data | Nilai yang Valid |
|-------|-----------|------------------|
| Age | Numerik | 18-84 |
| Salt_Intake | Numerik | 2.5-16.4 |
| Stress_Score | Numerik | 0-10 |
| BP_History | Kategorikal | 'Normal', 'Prehypertension', 'Hypertension' |
| Sleep_Duration | Numerik | 1.5-11.4 |
| BMI | Numerik | 11.9-41.9 |
| Medication | Kategorikal | 'NaN', 'ACE Inhibitor', 'Beta Blocker', 'Diuretic', 'Other' |
| Family_History | Kategorikal | 'Yes', 'No' |
| Exercise_Level | Kategorikal | 'Low', 'Moderate', 'High' |
| Smoking_Status | Kategorikal | 'Non-Smoker', 'Ex-Smoker', 'Current', 'Smoker' |

### **STEP 4: Konversi ke DataFrame**

```python
# Model membutuhkan input dalam format DataFrame
df_pasien = pd.DataFrame([data_pasien])
```

### **STEP 5: Lakukan Prediksi**

```python
# Prediksi label (0 = Tidak Berisiko, 1 = Berisiko)
prediksi = model.predict(df_pasien)[0]

# Prediksi probabilitas
probabilitas = model.predict_proba(df_pasien)[0]

# Tampilkan hasil
if prediksi == 1:
    print(f"⚠️ BERISIKO HIPERTENSI")
    print(f"Probabilitas: {probabilitas[1]*100:.2f}%")
else:
    print(f"✓ TIDAK BERISIKO")
    print(f"Probabilitas: {probabilitas[0]*100:.2f}%")
```

---

## 🔄 Fungsi Reusable (Copy-Paste Ready)

```python
def prediksi_hipertensi(data_pasien, model_path='model_hipertensi.pkl'):
    """
    Fungsi untuk memprediksi risiko hipertensi
    
    Parameter:
        data_pasien (dict): Data pasien dengan 10 fitur
        model_path (str): Path ke file model .pkl
        
    Returns:
        dict: Hasil prediksi dengan label dan probabilitas
    """
    import pickle
    import pandas as pd
    
    # Load model
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    
    # Konversi ke DataFrame
    df = pd.DataFrame([data_pasien])
    
    # Prediksi
    pred = model.predict(df)[0]
    proba = model.predict_proba(df)[0]
    
    return {
        'label': 'Berisiko' if pred == 1 else 'Tidak Berisiko',
        'probabilitas_berisiko': f"{proba[1]*100:.2f}%",
        'probabilitas_tidak_berisiko': f"{proba[0]*100:.2f}%",
        'prediksi_angka': int(pred),
        'confidence': max(proba[0], proba[1])
    }

# Contoh penggunaan
pasien = {
    'Age': 52, 'Salt_Intake': 11.5, 'Stress_Score': 7,
    'BP_History': 'Prehypertension', 'Sleep_Duration': 5.5,
    'BMI': 29.5, 'Medication': 'Beta Blocker',
    'Family_History': 'Yes', 'Exercise_Level': 'Low',
    'Smoking_Status': 'Ex-Smoker'
}

hasil = prediksi_hipertensi(pasien)
print(f"Hasil: {hasil['label']}")
print(f"Probabilitas Berisiko: {hasil['probabilitas_berisiko']}")
```

---

## 📊 Contoh Lengkap dengan Output

```python
# Load model
with open('model_hipertensi.pkl', 'rb') as file:
    model = pickle.load(file)

# Data pasien
pasien = {
    'Age': 65,
    'Salt_Intake': 14.0,
    'Stress_Score': 9,
    'BP_History': 'Hypertension',
    'Sleep_Duration': 4.5,
    'BMI': 32.5,
    'Medication': 'ACE Inhibitor',
    'Family_History': 'Yes',
    'Exercise_Level': 'Low',
    'Smoking_Status': 'Current'
}

# Konversi dan prediksi
df_pasien = pd.DataFrame([pasien])
prediksi = model.predict(df_pasien)[0]
probabilitas = model.predict_proba(df_pasien)[0]

# Output
print("="*60)
print("HASIL PREDIKSI RISIKO HIPERTENSI")
print("="*60)
print(f"Status: {'⚠️ BERISIKO' if prediksi == 1 else '✓ TIDAK BERISIKO'}")
print(f"Probabilitas Berisiko: {probabilitas[1]*100:.2f}%")
print(f"Probabilitas Tidak Berisiko: {probabilitas[0]*100:.2f}%")
print("="*60)
```

**Output:**
```
============================================================
HASIL PREDIKSI RISIKO HIPERTENSI
============================================================
Status: ⚠️ BERISIKO
Probabilitas Berisiko: 99.99%
Probabilitas Tidak Berisiko: 0.01%
============================================================
```

---

## 🎯 Interpretasi Hasil

### **Probabilitas Berisiko**
- **0-30%**: Risiko Rendah ✅
- **30-70%**: Risiko Sedang ⚠️
- **70-100%**: Risiko Tinggi 🚨

### **Rekomendasi Berdasarkan Hasil**

**Jika Berisiko (prediksi = 1):**
1. Segera konsultasi dengan dokter
2. Pemeriksaan tekanan darah rutin
3. Kurangi asupan garam
4. Tingkatkan aktivitas fisik
5. Kelola stress

**Jika Tidak Berisiko (prediksi = 0):**
1. Pertahankan gaya hidup sehat
2. Check-up rutin tahuan
3. Jaga pola makan seimbang

---

## 🔍 Faktor Risiko Utama (Feature Importance)

Berdasarkan model, faktor-faktor berikut paling berpengaruh:

1. **BP_History (Prehypertension)** - 24.6%
2. **BP_History (Normal)** - 17.0%
3. **Age (Usia)** - 10.0%
4. **Family_History (Yes)** - 9.5%
5. **Stress_Score** - 9.4%

---

## ⚠️ Catatan Penting

1. **Model ini BUKAN pengganti diagnosis medis profesional**
2. Selalu konsultasikan dengan dokter untuk diagnosis akurat
3. Model ini adalah alat screening awal saja
4. Akurasi: 97.98% (dapat salah pada 2% kasus)

---

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'pickle'"
**Solusi**: pickle adalah built-in module, pastikan Python terinstall dengan benar

### Error: "FileNotFoundError: model_hipertensi.pkl"
**Solusi**: Pastikan file .pkl ada di direktori yang sama dengan script

### Error: "KeyError: 'Age'"
**Solusi**: Pastikan semua 10 fitur ada dalam dictionary data_pasien

### Error: "ValueError: could not convert string to float"
**Solusi**: Periksa tipe data setiap fitur (numerik vs kategorikal)

---

## 📞 Informasi Lebih Lanjut

- **Notebook**: `Untitled-1.ipynb`
- **Dataset**: `hypertension_dataset.csv`
- **Model Info**: `model_info.pkl`

Untuk pertanyaan atau bantuan lebih lanjut, silakan cek notebook untuk contoh lengkap!

---

**Dibuat**: December 11, 2025
**Model Version**: 1.0
**Framework**: scikit-learn, XGBoost
