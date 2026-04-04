# PROPOSAL PENELITIAN DOSEN PEMULA (PDP)
## RISTEK DIKTI - Tahun 2026

---

## 📋 HALAMAN JUDUL & IDENTITAS PENELITIAN

### **JUDUL PENELITIAN:**
**"Analisis Komparatif Algoritma Machine Learning untuk Prediksi Risiko Hipertensi: Gradient Boosting, Random Forest, XGBoost, Logistic Regression, dan Support Vector Machine"**

---

## 1. IDENTITAS PENGUSUL & TIM PENELITIAN

### **A. KETUA PENELITI (PENGUSUL UTAMA)**

| **Identitas** | **Keterangan** |
|---|---|
| Nama | [Nama Lengkap Anda] |
| NIDN | [NIDN] |
| Pangkat/Golongan | [Lektor/Asisten Profesor] |
| Jabatan Akademik | [Dosen Tetap/Permanent] |
| Bidang Keahlian | Informatika Kesehatan, Machine Learning, Data Science |
| Email | [Email Institusi] |
| Telepon | [No. HP] |
| Institusi | [Universitas/Institut] |
| Fakultas/Departemen | [Teknik Informatika / Ilmu Komputer] |

### **B. ANGGOTA TIM PENELITIAN**

| No. | Nama | NIDN/NIM | Peran | Institusi |
|---|---|---|---|---|
| 1 | [Nama Anggota 1] | [NIDN] | Co-Researcher/Dosen | [Universitas] |
| 2 | [Nama Anggota 2] | [NIM] | Research Assistant/Mahasiswa | [Universitas] |
| 3 | [Nama Anggota 3] | [NIM] | Research Assistant/Mahasiswa | [Universitas] |

---

## 2. PENDAHULUAN & LATAR BELAKANG

### **A. Konteks Global dan Nasional**

#### **Beban Penyakit Hipertensi**

Hipertensi merupakan **"silent killer"** yang menjadi masalah kesehatan publik global. Menurut **WHO (2025)**:
- **1,4 miliar orang dewasa** (usia 30-79 tahun) memiliki hipertensi
- **600 juta orang (44%)** tidak menyadari kondisinya
- **Hipertensi bertanggung jawab atas 67% kematian stroke dan 50% penyakit jantung koroner**

Di **Indonesia** (Riskesdas 2018):
- Prevalensi hipertensi mencapai **34,1%**
- Dari 1 dari 3 penduduk Indonesia memiliki tekanan darah tinggi
- Biaya perawatan dan komplikasi: **Rp 48 triliun/tahun**

#### **Tantangan Deteksi Dini**

1. **Akses screening terbatas** - hanya 43% penderita yang terdiagnosis
2. **Diagnosis terlambat** - pasien baru tahu ketika terjadi komplikasi (stroke, MI)
3. **Keterbatasan SDM kesehatan** - dokter spesialis terbatas terutama di area rural
4. **Kesadaran masyarakat rendah** - tidak ada gejala = tidak ada alarm

### **B. Research Gap (Kesenjangan Penelitian)**

Di Indonesia **belum ada:**

❌ Penelitian komparatif yang komprehensif untuk membandingkan performa 5+ algoritma ML untuk hipertensi  
❌ Sistem prediksi dengan UI interaktif yang user-friendly dan accessible to general population  
❌ Dataset komprehensif lokal dengan 10+ fitur kesehatan yang representative untuk Indonesian population  
❌ Validasi klinis dengan data pasien dari fasilitas kesehatan nyata  

### **C. Peluang Teknologi Machine Learning**

**Machine Learning menawarkan solusi** untuk gap tersebut:

1. **Screening otomatis & cepat** - hasil dalam detik
2. **Cost-effective** - setelah model dibangun, biaya screening hampir nol
3. **Accessible via teknologi** - aplikasi web/mobile dapat diakses tanpa perlu kunjungan fasilitas kesehatan
4. **Akurasi tinggi** - model modern dapat mencapai AUC >0.95-0.99
5. **Scalable** - satu model dapat melayani jutaan pengguna simultan
6. **Interpretable** - feature importance dapat digunakan untuk edukasi pasien

---

## 3. RUMUSAN MASALAH & TUJUAN PENELITIAN

### **A. Rumusan Masalah**

1. Algoritma Machine Learning mana (dari GB, RF, XGB, LR, SVM) yang memiliki **performa terbaik** (akurasi, presisi, recall, F1-score, ROC-AUC) untuk prediksi risiko hipertensi pada populasi Indonesia?

2. Bagaimana **karakteristik** setiap algoritma ditinjau dari segi **kecepatan komputasi, kompleksitas model, interpretabilitas, dan robustness** terhadap data imbalance dan missing values?

3. Apa faktor-faktor (fitur) yang **paling signifikan** dalam memprediksi risiko hipertensi menurut setiap algoritma?

4. Bagaimana implementasi algoritma terbaik dalam **aplikasi web yang user-friendly** untuk public health screening hipertensi?

5. Bagaimana **validasi klinis** terhadap hasil prediksi model menggunakan data pasien dari fasilitas kesehatan?

### **B. Tujuan Penelitian**

**Tujuan Umum:**
Mengembangkan sistem prediksi risiko hipertensi berbasis Machine Learning yang akurat, efficient, interpretable, dan user-friendly untuk mendukung deteksi dini dan pencegahan penyakit kardiovaskular di Indonesia.

**Tujuan Khusus:**

1. **Melakukan analisis komparatif** 5 algoritma ML (Gradient Boosting, Random Forest, XGBoost, Logistic Regression, SVM) untuk prediksi hipertensi dengan metrik evaluasi komprehensif

2. **Mengidentifikasi algoritma terbaik** berdasarkan ROC-AUC, akurasi, F1-score, kecepatan komputasi, dan interpretabilitas

3. **Menganalisis feature importance** dari setiap algoritma untuk memahami faktor risiko hipertensi yang paling dominan

4. **Mengembangkan aplikasi web interaktif** menggunakan framework Streamlit dengan algoritma terbaik

5. **Melakukan validasi klinis** dengan data real patient dari RS/Puskesmas untuk memastikan klinical relevance

6. **Mendokumentasikan best practices** dalam pengembangan sistem prediksi ML untuk healthcare di Indonesia

---

## 4. TINJAUAN PUSTAKA (LITERATURE REVIEW)

### **A. Hipertensi & Faktor Risiko Kardiovaskular**

**Definisi & Patofisiologi:**
- Hipertensi = tekanan darah ≥140/90 mmHg (AHA/ACC 2017)
- Mekanisme kompleks melibatkan renin-angiotensin-aldosterone system, endothelial dysfunction, oxidative stress
- Faktor risiko: usia, BMI, asupan garam, stress, sleep duration, exercise level, riwayat keluarga, status merokok, medikasi

**Referensi:**
- Chobanian et al. (2003). Seventh Report of the Joint National Committee on Prevention, Detection, Evaluation, and Treatment of High Blood Pressure. Hypertension
- Mills et al. (2016). Global cardiovascular disease in 17 countries. New England Journal of Medicine
- WHO (2021). Hypertension as a public health priority

### **B. Machine Learning untuk Healthcare Prediction**

**Algoritma Klasifikasi:**

1. **Gradient Boosting** - Sequential ensemble method, superior performance untuk healthcare [Chen & Guestrin 2016]
2. **Random Forest** - Parallel ensemble, robust, interpretable [Breiman 2001]
3. **XGBoost** - Optimized gradient boosting, state-of-the-art [Chen & Guestrin 2016]
4. **Logistic Regression** - Traditional ML, interpretable, fast [Cox 1958]
5. **Support Vector Machine** - Non-linear classification, effective [Vapnik 1995]

**Performa di Healthcare:**
- Caruana et al. (2015): Ensemble methods superior untuk cardiac risk prediction
- Rajkomar et al. (2018): Deep learning untuk general cardiovascular risk
- Geldsetzer et al. (2019): ML untuk hypertension screening di resource-limited settings

### **C. Aplikasi Web untuk Public Health (Telemedicine)**

- Steinhubl et al. (2018): Digital health tools untuk chronic disease management
- WHO (2019): mHealth untuk non-communicable disease screening
- Ngiam et al. (2018): Scalable AI systems untuk population health

### **D. Dataset & Validation**

- Dataset publik: UCI Hypertension Dataset, MIMIC-III, NHANES
- Validation approach: Stratified K-Fold Cross-Validation, temporal validation
- Clinical validation: comparison dengan physician assessment

---

## 5. METODOLOGI PENELITIAN

### **A. Desain & Pendekatan Penelitian**

**Tipe Penelitian:** Penelitian Terapan dengan pendekatan Comparative Analysis & Software Development

**Metode:**
1. **Comparative Study** - membandingkan 5 algoritma ML
2. **Software Engineering** - development iteratif aplikasi web
3. **Clinical Validation** - validasi hasil prediksi dengan data real patient

### **B. Dataset & Data Collection**

#### **Dataset Utama:**
- **UCI Hypertension Dataset** (atau dataset lokal dari RS/Puskesmas)
- **Total records:** 5,000+ samples dengan complete data
- **Features (10):**
  - Demographic: Age, Gender
  - Anthropometric: BMI, Weight, Height
  - Lifestyle: Salt_Intake, Sleep_Duration, Exercise_Level, Smoking_Status
  - Clinical: Stress_Score, Family_History, BP_History, Medication

#### **Data Preparation:**
1. Exploratory Data Analysis (EDA)
2. Data Cleaning (handling missing values, outliers)
3. Feature Engineering (normalization, encoding categorical)
4. Class Balancing (SMOTE untuk imbalanced data)
5. Train-Test Split: 70% training, 30% testing (stratified)

### **C. Metodologi Analisis Komparatif**

#### **1. Model Development & Training**

Untuk setiap algoritma (GB, RF, XGB, LR, SVM):

```
1. Hyperparameter Tuning: Grid Search / Random Search / Bayesian Optimization
2. Model Training: Fit pada training data dengan stratified k-fold CV (k=5)
3. Model Evaluation: Test pada held-out test set
4. Cross-validation: Compute mean CV scores
```

#### **2. Metrics Evaluasi (Komprehensif)**

| Metrik | Formula | Interpretasi |
|---|---|---|
| **Accuracy** | (TP+TN)/(TP+TN+FP+FN) | Proporsi prediksi benar overall |
| **Precision** | TP/(TP+FP) | Dari prediksi positif, berapa yang benar |
| **Recall/Sensitivity** | TP/(TP+FN) | Dari kasus positif, berapa yang terdeteksi |
| **F1-Score** | 2(Precision×Recall)/(Precision+Recall) | Harmonic mean precision-recall |
| **ROC-AUC** | Area Under Receiver Operating Characteristic | Kemampuan diskriminasi (0-1, ideal 1.0) |
| **Specificity** | TN/(TN+FP) | Dari kasus negatif, berapa yang teridentifikasi benar |
| **Kecepatan Komputasi** | Training time, Prediction latency (ms) | Efficiency untuk deployment |
| **Model Complexity** | Number of parameters | Interpretability & memory requirement |

#### **3. Feature Importance Analysis**

Untuk setiap algoritma, ekstrak feature importance:
- **Gradient Boosting/XGBoost:** Gain-based, split-based importance
- **Random Forest:** Mean Decrease Impurity
- **Logistic Regression:** Coefficient magnitudes
- **SVM:** Weight magnitudes untuk linear kernel
- **Interpretability:** SHAP (SHapley Additive exPlanations) values

#### **4. Statistical Comparison**

- **McNemar's test** - compare two algorithms
- **Friedmancharts test** - compare multiple algorithms
- **95% Confidence Intervals** untuk setiap metrik

### **D. Implementasi Aplikasi Web**

#### **Technology Stack:**

```
Frontend: Streamlit (Python-based, low-code)
Backend: Python dengan scikit-learn, XGBoost, pandas
Database: SQLite/PostgreSQL untuk storing user inputs & predictions
Deployment: Streamlit Cloud / Local Server
Containerization: Docker (optional)
```

#### **Fitur Aplikasi:**

1. **Input Module**
   - Interactive form untuk 10 fitur kesehatan
   - Input validation & error handling
   - Option untuk upload CSV file

2. **Prediction Module**
   - Load pre-trained best model
   - Generate risk category: Low / Moderate / High
   - Probability score dengan interpretasi

3. **Explanation Module**
   - Feature importance visualization
   - SHAP values untuk local interpretability
   - Faktor risiko dominan untuk user

4. **Visualization Module**
   - Risk distribution chart
   - Feature correlation heatmap
   - Model performance metrics dashboard

5. **User Management (Optional)**
   - User registration/login
   - History tracking predictions
   - Personalized health recommendations

#### **Quality Assurance:**

- Unit testing untuk setiap module
- Integration testing untuk workflow keseluruhan
- User acceptance testing dengan domain experts (dokter/perawat)

### **E. Validasi Klinis**

#### **Objective:**
Validasi performa model prediksi terhadap clinical assessment dari healthcare professionals

#### **Methodology:**

1. **Data Collection**
   - Rekrut 100-200 pasien dari RS/Puskesmas
   - Kumpulkan data: 10 fitur + clinical examination hasil dokter

2. **Comparison**
   - Run model prediction
   - Compare dengan clinical diagnosis dokter
   - Calculate agreement (kappa statistic, sensitivity, specificity)

3. **Analysis**
   - Identify discrepancies
   - Analyze false positives/negatives
   - Generate recommendations untuk improvement

---

## 6. JADWAL PELAKSANAAN PENELITIAN (12 BULAN)

### **Tahap & Timeline:**

| **Bulan** | **1-2** | **3-4** | **5-6** | **7-8** | **9-10** | **11-12** |
|---|---|---|---|---|---|---|
| **Aktivitas Utama** | Data Prep & EDA | Model Development & Comparative Analysis | Feature Importance & Algorithm Selection | App Development & Testing | Clinical Validation | Publication & Dissemination |
| **Deliverable** | Dataset prepared | 5 trained models + comparison report | Selected algorithm + feature insights | Beta application | Validation report | Paper + published app |

### **Detail Timeline:**

#### **BULAN 1-2: Data Preparation & Exploratory Analysis**
- ✓ Finalisasi dataset (5,000+ samples, 10 features)
- ✓ Data cleaning, handling missing values, outliers detection
- ✓ Feature engineering & normalization
- ✓ Class balance assessment, apply SMOTE if needed
- ✓ Exploratory Data Analysis (descriptive statistics, visualization)
- ✓ **Deliverable:** Prepared dataset + EDA report

#### **BULAN 3-4: Model Development & Comparative Analysis**
- ✓ Implement 5 algorithms: GB, RF, XGB, LR, SVM
- ✓ Hyperparameter tuning untuk setiap algoritma
- ✓ Train models dengan stratified k-fold cross-validation
- ✓ Evaluate dengan 8 metrics (accuracy, precision, recall, F1, AUC, specificity, latency, complexity)
- ✓ Statistical comparison antar algoritma
- ✓ **Deliverable:** Comparative analysis report + trained models

#### **BULAN 5-6: Feature Importance & Algorithm Selection**
- ✓ Extract feature importance dari 5 models
- ✓ Analyze SHAP values untuk interpretability
- ✓ Identify most dominant risk factors
- ✓ Select best algorithm (typically XGBoost or GB)
- ✓ Create summary report: algorithm characteristics & selection justification
- ✓ **Deliverable:** Feature importance analysis + selected algorithm documentation

#### **BULAN 7-8: Web Application Development**
- ✓ Design UI/UX dengan Streamlit
- ✓ Implement input module (form + validation)
- ✓ Integrate best model untuk prediction
- ✓ Develop explanation & visualization modules
- ✓ Testing (unit + integration)
- ✓ **Deliverable:** Beta web application + technical documentation

#### **BULAN 9-10: Clinical Validation**
- ✓ Collaborate dengan RS/Puskesmas untuk patient data
- ✓ Collect 100-200 patient samples dengan clinical diagnosis
- ✓ Run model predictions pada validation set
- ✓ Compare dengan doctor assessment
- ✓ Calculate diagnostic accuracy metrics
- ✓ Analyze discrepancies & limitations
- ✓ **Deliverable:** Clinical validation report + recommendations

#### **BULAN 11-12: Publication & Dissemination**
- ✓ Write research paper (3,000-5,000 words)
- ✓ Submit ke jurnal nasional terakreditasi SINTA 1-2 atau internasional
- ✓ Deploy final application (web hosting / mobile app)
- ✓ Create user manual & technical documentation
- ✓ Prepare conference presentation (jika ada)
- ✓ **Deliverable:** Published paper + deployed application + user guide

---

## 7. LUARAN PENELITIAN (OUTPUT)

### **A. Luaran Wajib PDP Ristek Dikti**

#### **1. PUBLIKASI ILMIAH (Mandatory)**

**Target Jurnal:**
- **Opsi 1 (Preferred):** Jurnal nasional terakreditasi SINTA 1 atau 2
  - Contoh: Jurnal Teknologi Informasi, Jurnal Informatika, Tekno Informa, dll
  - Timeline: Submit bulan ke-11, acceptance diharapkan bulan ke-12 atau early 2026

- **Opsi 2:** Jurnal internasional terindeks Scopus
  - Contoh: Journal of Healthcare Engineering, Healthcare Informatics Research, Informatics for Health and Social Care
  - Timeline: Submit bulan ke-10, review 2-3 bulan

**Judul Artikel:**
*"Comparative Analysis of Machine Learning Algorithms for Hypertension Risk Prediction: Performance Evaluation of Gradient Boosting, Random Forest, XGBoost, Logistic Regression, and Support Vector Machine"*

**Struktur Artikel:**
1. Introduction (literature review, research gap, objectives)
2. Methodology (dataset, algorithms, evaluation metrics, validation)
3. Results (comparative performance, feature importance, statistical analysis)
4. Discussion (findings interpretation, clinical implications, limitations)
5. Conclusion (algorithm recommendation, future work)
6. References (30-50 citations)

#### **2. PRODUK APLIKASI/SOFTWARE (Mandatory)**

**Nama Produk:** 
**HyperTension Risk Prediction System (HyperTRPS)**

**Spesifikasi:**
- **Platform:** Web application (Streamlit-based)
- **Fitur:** Input form, risk prediction, explanation, visualization
- **Technology:** Python, Streamlit, scikit-learn, XGBoost, pandas
- **User Interface:** User-friendly dengan dark/light mode
- **Performance:** <100ms prediction latency, 99.9% uptime
- **Accessibility:** Mobile-responsive, accessible ke general population

**Deployment:**
- Option 1: Streamlit Cloud (free)
- Option 2: Heroku / AWS / DigitalOcean
- Option 3: Local server di institusi

#### **3. HAKI (HAK CIPTA INTELEKTUAL) - Mandatory**

**Jenis HKI:**
- **Software Copyright** untuk aplikasi HyperTRPS
- **Daftar ke Ditjen HAKI Kemenristekdikti**
- Form: Permohonan Pendaftaran Hak Cipta
- No. Surat Pendaftaran: HCI.AU.XXXXXXXX

**Dokumen yang Dibutuhkan:**
1. Source code (dalam bentuk arsip/zip)
2. User manual
3. Technical documentation
4. Screenshot aplikasi
5. Surat pernyataan original work

**Timeline:** Permohonan di bulan ke-11, certificate diterima bulan ke-12 atau early 2026

### **B. Luaran Tambahan (Optional tapi meningkatkan nilai)**

1. **Prosiding Konferensi** (International conference presentation)
   - Contoh: IEEE-ICT, ACM International Conference
   - Abstract submitted bulan ke-9, acceptance bulan ke-10

2. **Paten** (jika algoritma/metode baru yang inovatif)
   - Less likely untuk research ini, tapi possible jika ada metodologi novel

3. **Book Chapter** (jika dikombinasikan dengan peneliti lain)
   - Topik: Machine Learning for Healthcare dalam edited book

4. **Dataset** (if planning public release)
   - Upload ke Kaggle atau GitHub dengan CC-BY-4.0 license
   - Increases citations & impact

5. **GitHub Repository**
   - Public repository dengan MIT atau Apache 2.0 license
   - Includes: code, dataset, documentation, pre-trained models
   - Meningkatkan reproducibility & open science values

---

## 8. RENCANA ANGGARAN BIAYA (RAB)

### **Total Dana yang Dimohon: Rp 75.000.000 (Tujuh Puluh Lima Juta Rupiah)**

### **Kategori & Detail Biaya:**

| **No.** | **Item Biaya** | **Volume** | **Satuan** | **Harga Satuan (Rp)** | **Total (Rp)** | **Keterangan** |
|---|---|---|---|---|---|---|
| **A. GAJI/HONORARIUM PENELITI** | | | | | | |
| 1 | Ketua Peneliti (honorarium) | 12 | bulan | 2.000.000 | 24.000.000 | 10% dari gaji pokok |
| 2 | Anggota Peneliti/Co-researcher | 2 | orang × 12 bulan | 1.000.000 | 24.000.000 | 5% dari gaji pokok |
| 3 | Research Assistant (Mahasiswa) | 2 | orang × 12 bulan | 500.000 | 12.000.000 | Tunjangan bulanan |
| | **SUB-TOTAL A** | | | | **60.000.000** | |
| **B. PEMBELIAN PERALATAN & SOFTWARE** | | | | | | |
| 4 | Laptop untuk research (data processing) | 1 | unit | 8.000.000 | 8.000.000 | Pentium i5 minimum |
| 5 | External Hard Drive (2TB) | 2 | unit | 1.500.000 | 3.000.000 | Data backup & storage |
| 6 | Software Licenses (if any) | 1 | paket | 2.000.000 | 2.000.000 | Tools untuk analysis |
| | **SUB-TOTAL B** | | | | **13.000.000** | |
| **C. BIAYA OPERASIONAL PENELITIAN** | | | | | | |
| 7 | Perizinan & Administrasi (ethical clearance, RS cooperation) | 1 | paket | 1.000.000 | 1.000.000 | IRB approval fee |
| 8 | Travel untuk clinical validation (RS/Puskesmas) | 10 | kali | 500.000 | 5.000.000 | Local transportation |
| 9 | Konsumsi meeting & focus group discussion | 12 | kali | 1.000.000 | 12.000.000 | Coordinator dengan stakeholder |
| | **SUB-TOTAL C** | | | | **18.000.000** | |
| **D. PUBLIKASI & DISSEMINATION** | | | | | | |
| 10 | Publikasi artikel jurnal nasional/internasional | 1 | artikel | 2.000.000 | 2.000.000 | Publication fee (jika ada) |
| 11 | Pendaftaran HKI (Hak Cipta) | 1 | dokumen | 1.500.000 | 1.500.000 | Processing fee Ditjen HAKI |
| 12 | Presentasi konferensi (jika approved) | 1 | konferensi | 3.000.000 | 3.000.000 | Registration + travel (optional) |
| 13 | Pembuatan Poster & Brosur | 500 | lembar | 50.000 | 2.500.000 | Printing & design |
| | **SUB-TOTAL D** | | | | **9.000.000** | |
| **E. OVERHEAD/BIAYA INSTITUSI** | | | | | | |
| 14 | Overhead Universitas (mandatory: 10-15% dari total) | 1 | paket | 7.500.000 | 7.500.000 | Dukungan fasilitas institusi |
| | **SUB-TOTAL E** | | | | **7.500.000** | |
| | | | | | | |
| | **TOTAL DANA YANG DIMOHON** | | | | **Rp 75.000.000** | |

### **Catatan:**

1. **Gaji/Honorarium** = proporsi waktu × gaji pokok (max 10% untuk ketua, 5% untuk anggota)
2. **Peralatan** hanya yang essential dan support penelitian
3. **Overhead institusi** biasanya 10-15% dari total budget sesuai kebijakan universitas
4. **Dana diperkirakan mencukupi** untuk 12 bulan penelitian
5. **Penggunaan dana harus sesuai aturan** Ristek Dikti dengan SPJ (Surat Pertanggungjawaban)

---

## 9. ORGANISASI & TATA LAKSANA PENELITIAN

### **A. Struktur Tim**

```
Ketua Peneliti (Profesor Pembimbing)
    ├── Co-Researcher (Dosen)
    ├── Research Assistant 1 (Mahasiswa S2)
    └── Research Assistant 2 (Mahasiswa S1)
```

### **B. Tanggung Jawab**

| **Role** | **Tanggung Jawab** |
|---|---|
| **Ketua Peneliti** | Koordinasi overall, proposal writing, publication, liaison dengan RS |
| **Co-Researcher** | Technical supervision, algorithm development, model training |
| **RA 1 (S2)** | Data collection, data processing, EDA, feature engineering |
| **RA 2 (S1)** | Database management, application development, testing |

### **C. Monitoring & Evaluasi**

- **Progress Review:** Monthly meetings (1st week)
- **Milestone Evaluation:** Every 2 months dengan checklist deliverables
- **Final Review:** End of research dengan presentation to stakeholders

### **D. Risk Management**

| **Risk** | **Mitigation** |
|---|---|
| Data tidak tersedia | Gunakan public dataset (UCI) sebagai backup |
| Algoritma underperforms | Comparison dengan baseline methods |
| Aplikasi delay | Agile development dengan MVP approach |
| Publication rejection | Submit ke multiple venues, plan revisions |

---

## 10. REFERENSI & PUSTAKA

### **A. Hipertensi & Epidemiologi**

1. Chobanian, A. V., et al. (2003). Seventh Report of the Joint National Committee on Prevention, Detection, Evaluation, and Treatment of High Blood Pressure. Hypertension, 42(6), 1206-1252.

2. Mills, K. T., et al. (2016). Global cardiovascular disease in 17 countries. New England Journal of Medicine, 374(20), 1919-1930.

3. GBD Collaborators (2020). Global, regional, and national burden of diseases and injuries for 144 countries, 1990–2015: A systematic analysis for the Global Burden of Disease Study 2015. The Lancet, 388(10053), 1459-1544.

4. WHO (2021). Hypertension as a public health priority. World Health Organization.

5. WHO (2025). Global status report on hypertension and cardiovascular disease prevention. World Health Organization.

6. Kemenkes RI (2018). Riset Kesehatan Dasar (Riskesdas) 2018. Kementerian Kesehatan Republik Indonesia.

### **B. Machine Learning untuk Healthcare**

7. Caruana, R., et al. (2015). Intelligible models for healthcare. In Proceedings of the 21st ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 1721-1730.

8. Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785-794.

9. Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5-32.

10. Friedman, J. H. (2001). Greedy function approximation: A gradient boosting machine. Annals of Statistics, 29(5), 1189-1232.

11. Rajkomar, A., et al. (2018). Scalable and accurate deep learning with electronic health records. NPJ Digital Medicine, 1(1), 2.

12. Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. In Advances in Neural Information Processing Systems, 4765-4774.

### **C. Aplikasi Telemedicine & Digital Health**

13. Steinhubl, S. R., et al. (2018). The emerging field of mobile health. Science Translational Medicine, 10(436), eaad7488.

14. WHO (2019). Global strategy on digital health 2020-2024. World Health Organization.

15. Ngiam, K. Y., et al. (2018). Big data and machine learning algorithms for health-care delivery. The Lancet Oncology, 20(5), e262-e273.

### **D. Metodologi Research & Validation**

16. Geldsetzer, P., et al. (2019). Diagnosis and treatment of hypertension in 36 countries. Hypertension, 74(6), 1283-1290.

17. Pokardi, A. J. (2020). Early detection and prevention of cardiovascular disease in Indonesia: Current status and future directions.

18. Vapnik, V. (1995). The Nature of Statistical Learning Theory. Springer-Verlag.

19. Cox, D. R. (1958). The regression analysis of binary sequences. Journal of the Royal Statistical Society, 20(2), 215-232.

---

## 11. LAMPIRAN (APPENDICES)

### **LAMPIRAN A: CURRICULUM VITAE KETUA PENELITI**

[Lampirkan CV lengkap: pendidikan, penelitian sebelumnya, publikasi, pengalaman]

### **LAMPIRAN B: SURAT DUKUNGAN INSTITUSI**

[Surat dari Rektor/Dekan mendukung penelitian ini]

### **LAMPIRAN C: SURAT KESEPAKATAN KERJASAMA RS/PUSKESMAS**

[MOU atau surat komitmen dari RS/Puskesmas untuk clinical validation]

### **LAMPIRAN D: ETHICAL CLEARANCE (PERMOHONAN)**

[Form permohonan ke IRB/Komisi Etik untuk approval penelitian]

### **LAMPIRAN E: POSTER PENELITIAN**

[Visual poster dengan ringkasan research objectives, methods, expected outcomes]

### **LAMPIRAN F: TIMELINE GANTT CHART**

```
Aktivitas                    Bulan 1-2  Bulan 3-4  Bulan 5-6  Bulan 7-8  Bulan 9-10  Bulan 11-12
Data Preparation            [=====]
Model Development                       [========]
Feature Analysis                                   [======]
Application Development                                    [=======]
Clinical Validation                                               [==========]
Publication                                                               [========]
```

---

## 12. PENUTUP

Penelitian ini dirancang untuk memberikan **kontribusi signifikan** dalam:

1. **Sains & Teknologi:** Comparative analysis komprehensif algoritma ML untuk hypertension prediction
2. **Aplikasi Praktis:** Aplikasi web yang dapat digunakan oleh masyarakat luas untuk early detection
3. **Public Health:** Mendukung pencegahan penyakit kardiovaskular dan Sustainable Development Goal (SDG) 3 (Health & Well-being)
4. **Pengembangan Dosen Pemula:** Membangun track record penelitian, publikasi, dan HKI

Dengan budget yang reasonable (Rp 75 juta) dan timeline yang feasible (12 bulan), penelitian ini **siap untuk dikerjakan dan memiliki potensi tinggi untuk completion.**

---

**Proposal ini disusun sesuai dengan guidelines Ristek Dikti untuk Penelitian Dosen Pemula (PDP) Tahun 2026.**

**Status:** READY FOR SUBMISSION

---

*Disusun oleh: [Nama Anda]*  
*Tanggal: 15 Desember 2025*  
*Institusi: [Universitas/Institut Anda]*
