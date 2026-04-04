# Script untuk testing model hipertensi - Versi Sederhana
# Jalankan di Jupyter Notebook atau terminal dengan conda environment

"""
CARA MENGGUNAKAN MODEL HIPERTENSI.PKL

Ikuti langkah-langkah berikut:

LANGKAH 1: IMPORT LIBRARY
-------------------------
"""

import pickle
import pandas as pd

"""
LANGKAH 2: LOAD MODEL DARI FILE
--------------------------------
Model yang sudah di-training disimpan dalam file .pkl
Kita buka dengan pickle.load()
"""

# Buka file dan load model
with open('model_hipertensi.pkl', 'rb') as file:
    model = pickle.load(file)

print("✓ Model berhasil di-load dari model_hipertensi.pkl\n")

"""
LANGKAH 3: SIAPKAN DATA PASIEN BARU
------------------------------------
Data harus memiliki kolom yang sama dengan data training:
- Age, Salt_Intake, Stress_Score, BP_History, Sleep_Duration
- BMI, Medication, Family_History, Exercise_Level, Smoking_Status
"""

# Contoh 1: Pasien dengan risiko tinggi
pasien_risiko_tinggi = {
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

# Contoh 2: Pasien dengan risiko rendah
pasien_risiko_rendah = {
    'Age': 30,
    'Salt_Intake': 6.0,
    'Stress_Score': 2,
    'BP_History': 'Normal',
    'Sleep_Duration': 7.5,
    'BMI': 22.0,
    'Medication': 'NaN',
    'Family_History': 'No',
    'Exercise_Level': 'High',
    'Smoking_Status': 'Non-Smoker'
}

"""
LANGKAH 4: KONVERSI DATA KE DATAFRAME
--------------------------------------
Model membutuhkan input dalam format pandas DataFrame
"""

# Konversi dictionary ke DataFrame
df_pasien_1 = pd.DataFrame([pasien_risiko_tinggi])
df_pasien_2 = pd.DataFrame([pasien_risiko_rendah])

"""
LANGKAH 5: LAKUKAN PREDIKSI
----------------------------
Ada 2 jenis prediksi:
1. predict() -> menghasilkan label (0 atau 1)
2. predict_proba() -> menghasilkan probabilitas
"""

# Prediksi pasien 1
prediksi_1 = model.predict(df_pasien_1)[0]
probabilitas_1 = model.predict_proba(df_pasien_1)[0]

# Prediksi pasien 2
prediksi_2 = model.predict(df_pasien_2)[0]
probabilitas_2 = model.predict_proba(df_pasien_2)[0]

"""
LANGKAH 6: INTERPRETASI HASIL
------------------------------
prediksi: 0 = Tidak Berisiko, 1 = Berisiko
probabilitas[0] = probabilitas tidak berisiko
probabilitas[1] = probabilitas berisiko
"""

print("="*70)
print("HASIL PREDIKSI PASIEN 1 (Profil Risiko Tinggi)")
print("="*70)
print(f"Usia: {pasien_risiko_tinggi['Age']}, BMI: {pasien_risiko_tinggi['BMI']}")
print(f"Riwayat: {pasien_risiko_tinggi['BP_History']}, Merokok: {pasien_risiko_tinggi['Smoking_Status']}")
print("-"*70)
print(f"Prediksi: {'BERISIKO HIPERTENSI' if prediksi_1 == 1 else 'TIDAK BERISIKO'}")
print(f"Probabilitas Berisiko: {probabilitas_1[1]*100:.2f}%")
print(f"Probabilitas Tidak Berisiko: {probabilitas_1[0]*100:.2f}%")
print()

print("="*70)
print("HASIL PREDIKSI PASIEN 2 (Profil Risiko Rendah)")
print("="*70)
print(f"Usia: {pasien_risiko_rendah['Age']}, BMI: {pasien_risiko_rendah['BMI']}")
print(f"Riwayat: {pasien_risiko_rendah['BP_History']}, Merokok: {pasien_risiko_rendah['Smoking_Status']}")
print("-"*70)
print(f"Prediksi: {'BERISIKO HIPERTENSI' if prediksi_2 == 1 else 'TIDAK BERISIKO'}")
print(f"Probabilitas Berisiko: {probabilitas_2[1]*100:.2f}%")
print(f"Probabilitas Tidak Berisiko: {probabilitas_2[0]*100:.2f}%")
print()

"""
LANGKAH 7: MEMBUAT FUNGSI REUSABLE (OPSIONAL)
----------------------------------------------
Untuk mempermudah penggunaan berulang
"""

def prediksi_hipertensi(data_pasien, model_path='model_hipertensi.pkl'):
    """
    Fungsi untuk memprediksi risiko hipertensi
    
    Parameter:
        data_pasien (dict): Data pasien dengan semua fitur
        model_path (str): Path ke file model
        
    Returns:
        dict: Hasil prediksi dengan label dan probabilitas
    """
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
        'prediksi_angka': int(pred)
    }

# Contoh penggunaan fungsi
print("="*70)
print("CONTOH PENGGUNAAN FUNGSI PREDIKSI_HIPERTENSI()")
print("="*70)

pasien_baru = {
    'Age': 50,
    'Salt_Intake': 10.0,
    'Stress_Score': 6,
    'BP_History': 'Prehypertension',
    'Sleep_Duration': 6.0,
    'BMI': 28.0,
    'Medication': 'Beta Blocker',
    'Family_History': 'Yes',
    'Exercise_Level': 'Moderate',
    'Smoking_Status': 'Ex-Smoker'
}

hasil = prediksi_hipertensi(pasien_baru)

print("Data Pasien Baru:")
for key, value in pasien_baru.items():
    print(f"  {key}: {value}")

print("\nHasil Prediksi:")
print(f"  Klasifikasi: {hasil['label']}")
print(f"  Probabilitas Berisiko: {hasil['probabilitas_berisiko']}")
print(f"  Probabilitas Tidak Berisiko: {hasil['probabilitas_tidak_berisiko']}")
print("="*70)

print("\n✓ Script selesai! Model berhasil digunakan untuk prediksi.")
