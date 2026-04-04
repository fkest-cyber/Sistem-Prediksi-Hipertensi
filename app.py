# ========================================
# SISTEM PREDIKSI RISIKO HIPERTENSI
# Aplikasi Web dengan Streamlit
# ========================================

import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go
import numpy as np

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Risiko Hipertensi",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .risk-high {
        background-color: #ffebee;
        border-left: 5px solid #f44336;
        padding: 1rem;
        border-radius: 5px;
    }
    .risk-low {
        background-color: #e8f5e9;
        border-left: 5px solid #4caf50;
        padding: 1rem;
        border-radius: 5px;
    }
    .metric-box {
        background-color: #f5f5f5;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    try:
        with open('model_hipertensi.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("❌ File model_hipertensi.pkl tidak ditemukan!")
        st.stop()

model = load_model()

# Header
st.markdown('<p class="main-header">🏥 SISTEM PREDIKSI RISIKO HIPERTENSI</p>', unsafe_allow_html=True)
st.markdown("---")

# Informasi
with st.expander("ℹ️ Tentang Aplikasi Ini"):
    st.write("""
    **Sistem Prediksi Risiko Hipertensi** menggunakan Machine Learning (Gradient Boosting Classifier) 
    untuk memprediksi risiko hipertensi berdasarkan data kesehatan pasien.
    
    **Performa Model:**
    - Akurasi: 97.98%
    - F1-Score: 98.05%
    - ROC-AUC: 0.9984 (Excellent!)
    
    **Dataset:** 1,985 data pasien dengan 10 fitur kesehatan
    
    ⚠️ **Disclaimer:** Hasil prediksi ini adalah untuk screening awal saja dan BUKAN pengganti diagnosis medis profesional.
    """)

st.markdown("### 📋 Input Data Pasien")

# Layout dua kolom
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📊 Data Numerik")
    age = st.slider("🎂 Usia (tahun)", 18, 84, 55, help="Usia pasien dalam tahun")
    bmi = st.number_input("⚖️ BMI (Body Mass Index)", 11.9, 41.9, 30.0, 0.1, 
                          help="Berat (kg) / Tinggi² (m)")
    salt_intake = st.slider("🧂 Asupan Garam (g/hari)", 2.5, 16.4, 12.0, 0.1,
                           help="Konsumsi garam harian dalam gram")
    stress_score = st.slider("😰 Skor Stress", 0, 10, 7,
                            help="Tingkat stress (0=sangat rendah, 10=sangat tinggi)")
    sleep_duration = st.slider("😴 Durasi Tidur (jam/hari)", 1.5, 11.4, 5.5, 0.1,
                              help="Rata-rata jam tidur per hari")

with col2:
    st.markdown("#### 🏷️ Data Kategorikal")
    bp_history = st.selectbox("💉 Riwayat Tekanan Darah", 
                             ["Normal", "Prehypertension", "Hypertension"],
                             index=1,
                             help="Riwayat tekanan darah pasien")
    
    medication = st.selectbox("💊 Medikasi", 
                            ["NaN", "ACE Inhibitor", "Beta Blocker", "Diuretic", "Other"],
                            index=2,
                            help="Obat yang sedang dikonsumsi (pilih NaN jika tidak ada)")
    
    family_history = st.radio("👨‍👩‍👧‍👦 Riwayat Keluarga Hipertensi", 
                             ["No", "Yes"],
                             index=1,
                             help="Apakah ada anggota keluarga dengan hipertensi?")
    
    exercise_level = st.selectbox("🏃 Level Aktivitas Fisik", 
                                 ["Low", "Moderate", "High"],
                                 index=0,
                                 help="Tingkat aktivitas fisik sehari-hari")
    
    smoking_status = st.selectbox("🚬 Status Merokok", 
                                 ["Non-Smoker", "Ex-Smoker", "Current", "Smoker"],
                                 index=1,
                                 help="Status merokok saat ini")

st.markdown("---")

# Tombol prediksi
col_button1, col_button2, col_button3 = st.columns([1, 1, 1])
with col_button2:
    predict_button = st.button("🔍 PREDIKSI RISIKO SEKARANG", type="primary", use_container_width=True)

if predict_button:
    # Siapkan data
    input_data = {
        'Age': age,
        'Salt_Intake': salt_intake,
        'Stress_Score': stress_score,
        'BP_History': bp_history,
        'Sleep_Duration': sleep_duration,
        'BMI': bmi,
        'Medication': medication,
        'Family_History': family_history,
        'Exercise_Level': exercise_level,
        'Smoking_Status': smoking_status
    }
    
    # Konversi ke DataFrame
    df_input = pd.DataFrame([input_data])
    
    # Prediksi
    with st.spinner('🔄 Sedang memproses prediksi...'):
        prediction = model.predict(df_input)[0]
        probability = model.predict_proba(df_input)[0]
        prob_not_risk = probability[0] * 100
        prob_risk = probability[1] * 100
    
    st.markdown("---")
    st.markdown("## 📊 HASIL PREDIKSI")
    
    # Tampilkan hasil dalam card
    if prediction == 1:
        st.markdown(f"""
        <div class="risk-high">
            <h2 style="color: #d32f2f;">⚠️ BERISIKO HIPERTENSI</h2>
            <h3 style="color: #d32f2f;">Probabilitas: {prob_risk:.2f}%</h3>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="risk-low">
            <h2 style="color: #388e3c;">✅ TIDAK BERISIKO</h2>
            <h3 style="color: #388e3c;">Probabilitas: {prob_not_risk:.2f}%</h3>
        </div>
        """, unsafe_allow_html=True)
    
    # Progress bar probabilitas
    st.markdown("### 📈 Detail Probabilitas")
    col_prob1, col_prob2 = st.columns(2)
    
    with col_prob1:
        st.metric("✅ Tidak Berisiko", f"{prob_not_risk:.2f}%")
        st.progress(prob_not_risk / 100)
    
    with col_prob2:
        st.metric("⚠️ Berisiko", f"{prob_risk:.2f}%")
        st.progress(prob_risk / 100)
    
    # Gauge chart
    st.markdown("### 🎯 Tingkat Risiko")
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = prob_risk,
        title = {'text': "Probabilitas Risiko Hipertensi (%)"},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkred" if prob_risk > 70 else "orange" if prob_risk > 40 else "green"},
            'steps': [
                {'range': [0, 40], 'color': "lightgreen"},
                {'range': [40, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "lightcoral"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 70
            }
        }
    ))
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)
    
    # Rekomendasi
    st.markdown("---")
    st.markdown("### 💊 REKOMENDASI MEDIS")
    
    if prediction == 1:
        st.error("⚠️ **Pasien memiliki RISIKO TINGGI hipertensi!**")
        st.markdown("""
        **Saran Tindakan:**
        1. 🏥 Segera konsultasi dengan dokter spesialis
        2. 📊 Lakukan pemeriksaan tekanan darah rutin
        3. 🧂 Kurangi asupan garam (target < 5g/hari)
        4. 🏃 Tingkatkan aktivitas fisik (minimal 30 menit/hari)
        5. 🧘 Kelola stress dengan meditasi atau yoga
        6. 🚭 Hindari merokok dan alkohol
        7. ⚖️ Kurangi berat badan jika diperlukan (BMI target: 18.5-24.9)
        """)
    else:
        st.success("✅ **Pasien memiliki RISIKO RENDAH hipertensi.**")
        st.markdown("""
        **Saran Tindakan:**
        1. 💚 Pertahankan gaya hidup sehat yang sudah berjalan
        2. 📅 Lakukan check-up kesehatan rutin tahunan
        3. 🥗 Jaga pola makan seimbang
        4. 🏃 Tetap aktif berolahraga secara konsisten
        5. 😊 Kelola stress dengan baik
        """)
    
    # Profil pasien
    st.markdown("---")
    st.markdown("### 👤 PROFIL PASIEN")
    
    col_profile1, col_profile2 = st.columns(2)
    
    with col_profile1:
        st.markdown(f"""
        <div class="metric-box">
        <b>🎂 Usia:</b> {age} tahun<br>
        <b>⚖️ BMI:</b> {bmi}<br>
        <b>🧂 Asupan Garam:</b> {salt_intake} g/hari<br>
        <b>😰 Skor Stress:</b> {stress_score}/10<br>
        <b>😴 Durasi Tidur:</b> {sleep_duration} jam/hari
        </div>
        """, unsafe_allow_html=True)
    
    with col_profile2:
        st.markdown(f"""
        <div class="metric-box">
        <b>💉 Riwayat TD:</b> {bp_history}<br>
        <b>💊 Medikasi:</b> {medication}<br>
        <b>👨‍👩‍👧‍👦 Riwayat Keluarga:</b> {family_history}<br>
        <b>🏃 Level Olahraga:</b> {exercise_level}<br>
        <b>🚬 Status Merokok:</b> {smoking_status}
        </div>
        """, unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 📊 Informasi Model")
st.sidebar.markdown("""
**Model:** Gradient Boosting Classifier

**Performa:**
- Akurasi: 97.98%
- Precision: 98.53%
- Recall: 97.57%
- F1-Score: 98.05%
- ROC-AUC: 0.9984

**Dataset:**
- Total: 1,985 sampel
- Training: 1,588 sampel (80%)
- Testing: 397 sampel (20%)

**Fitur Terpenting:**
1. BP_History_Prehypertension (24.6%)
2. BP_History_Normal (17.0%)
3. Age (10.0%)
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚠️ Disclaimer")
st.sidebar.info("""
Model ini adalah alat **SCREENING AWAL** saja dan 
**BUKAN pengganti** diagnosis medis profesional. 

Selalu konsultasikan dengan dokter untuk diagnosis yang akurat.
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍💻 Developer")
st.sidebar.markdown("""
**Sistem Prediksi Hipertensi**

Powered by: Rudiansyah
- Python 🐍
- Streamlit 🎈
- Scikit-learn 🤖
- XGBoost ⚡
""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray; padding: 1rem;">
    <p>© 2025 Sistem Prediksi Risiko Hipertensi | Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)
