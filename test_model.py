# Script untuk testing model hipertensi yang sudah disimpan
# Step by step menggunakan model_hipertensi.pkl

import pickle
import pandas as pd

print("="*60)
print("TESTING MODEL PREDIKSI RISIKO HIPERTENSI")
print("="*60)

# STEP 1: Load model yang sudah disimpan
print("\nStep 1: Loading model dari file...")
with open('model_hipertensi.pkl', 'rb') as file:
    model = pickle.load(file)
print("✓ Model berhasil di-load!")

# STEP 2: Siapkan data pasien untuk diprediksi
print("\nStep 2: Menyiapkan data pasien...")
data_pasien = {
    'Age': 55,
    'Salt_Intake': 12.0,
    'Stress_Score': 8,
    'BP_History': 'Prehypertension',
    'Sleep_Duration': 5.0,
    'BMI': 30.0,
    'Medication': 'Beta Blocker',
    'Family_History': 'Yes',
    'Exercise_Level': 'Low',
    'Smoking_Status': 'Current'
}

print("Data Pasien:")
for key, value in data_pasien.items():
    print(f"  - {key}: {value}")

# STEP 3: Konversi dictionary ke DataFrame
print("\nStep 3: Konversi data ke format DataFrame...")
df_pasien = pd.DataFrame([data_pasien])
print("✓ DataFrame berhasil dibuat")
print(f"  Shape: {df_pasien.shape}")

# STEP 4: Prediksi menggunakan model
print("\nStep 4: Melakukan prediksi...")
prediksi = model.predict(df_pasien)[0]
probabilitas = model.predict_proba(df_pasien)[0]

print("✓ Prediksi selesai!")

# STEP 5: Tampilkan hasil
print("\n" + "="*60)
print("HASIL PREDIKSI")
print("="*60)
print(f"Klasifikasi: {'BERISIKO HIPERTENSI' if prediksi == 1 else 'TIDAK BERISIKO'}")
print(f"Probabilitas Tidak Berisiko: {probabilitas[0]*100:.2f}%")
print(f"Probabilitas Berisiko: {probabilitas[1]*100:.2f}%")
print("="*60)
