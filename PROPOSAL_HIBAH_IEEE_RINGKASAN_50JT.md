# PROPOSAL PENELITIAN HIBAH (FORMAT IEEE)
## Sistem Prediksi Risiko Hipertensi Berbasis Machine Learning

---
## 0. Ringkasan Eksekutif (≈3 halaman setara)
- **Masalah**: Hipertensi mempengaruhi 1,4 miliar orang (33% usia 30–79); 44% tidak terdiagnosis [1]. Faktor risiko utama penyakit kardiovaskular (PKV); bertanggung jawab ±67% kematian stroke dan ±50% penyakit jantung koroner [2], [3].
- **Celakanya di Indonesia**: Prevalensi 34,1% (Riskesdas 2018) [4]; banyak baru terdeteksi saat komplikasi berat. Biaya perawatan HTN & PKV diperkirakan Rp48 triliun/tahun [5].
- **Solusi yang diusulkan**: Sistem prediksi risiko hipertensi berbasis ML (Gradient Boosting), dikemas aplikasi web Streamlit untuk screening cepat, murah, dan mudah diakses.
- **Data & Model**: 1.985 sampel, 10 fitur klinis/lifestyle; pipeline: preprocessing (scaler + OHE) → Gradient Boosting. Performa uji: Akurasi 97,98%; F1 0,9805; ROC-AUC 0,9984.
- **Manfaat**: Deteksi dini, rekomendasi personal, alat bantu puskesmas/klinik, edukasi masyarakat.
- **Luaran kunci**: Model produksi (`model_hipertensi.pkl`), aplikasi web, dokumentasi teknis, paper jurnal, HKI software, deployment cloud/local.
- **Anggaran**: Rp 50.000.000 (ringkas di §6).

### 0.1 Tujuan
1) Membangun model ML berperforma tinggi untuk prediksi risiko hipertensi (target AUC ≥0,95; F1 ≥0,95). 2) Menghadirkan aplikasi web user-friendly untuk screening. 3) Mengidentifikasi faktor risiko utama (feature importance) yang dapat dijelaskan klinis. 4) Validasi kegunaan melalui uji pengguna (tenaga kesehatan & masyarakat). 5) Publikasi, dokumentasi, dan diseminasi terbuka.

### 0.2 Metodologi Singkat
- **Data**: 1.985 rekam pasien; 10 fitur (Age, BMI, Salt_Intake, Stress_Score, Sleep_Duration, BP_History, Medication, Family_History, Exercise_Level, Smoking_Status).
- **Preprocessing**: Imputasi (median/mode), StandardScaler (numerik), OneHotEncoder (kategorikal), deteksi outlier (IQR).
- **Modeling**: Banding 5 algoritma (LogReg, RandomForest, GradientBoosting, XGBoost, SVM); pilih terbaik via 5-fold stratified CV (metrik utama F1, ROC-AUC).
- **Evaluasi**: Confusion matrix, Accuracy, Precision, Recall, F1, ROC-AUC; analisis threshold & feature importance.
- **Aplikasi**: Streamlit + Plotly; form input 10 fitur; output probabilitas, gauge chart, rekomendasi klinis; disclaimer medis.

### 0.3 Hasil Awal (Proof-of-Concept)
- Gradient Boosting terpilih: Akurasi 97,98%; F1 0,9805; ROC-AUC 0,9984 (test set 397 sampel). Specificity 98,42%; Sensitivity 97,57%.
- Feature importance teratas: BP_History_Prehypertension (24,6%), BP_History_Normal (17,0%), Age (10,0%), BMI (8,5%).

### 0.4 Rencana Implementasi (12 Bulan)
- **Bln 1-2**: Data cleaning, EDA, preprocessing final.
- **Bln 3-4**: Training + hyperparameter tuning; pilih model.
- **Bln 5**: Validasi eksternal + model card.
- **Bln 6-7**: Pengembangan aplikasi web, integrasi model.
- **Bln 8-9**: Uji coba pengguna (puskesmas/dokter umum); perbaikan UX.
- **Bln 10-11**: Publikasi/paper; deployment cloud; dokumentasi pengguna.
- **Bln 12**: Diseminasi, pelatihan, laporan akhir.

### 0.5 Luaran Terukur
- Model produksi + kode sumber terpublikasi.
- Aplikasi web siap pakai (cloud + opsi offline lokal).
- 1–2 artikel jurnal (Scopus) + 1 konferensi.
- HKI perangkat lunak.
- Paket pelatihan (video, manual, FAQ).

---
## 1. Rencana Anggaran Biaya (RAB) — Plafon Rp 50.000.000
**Prinsip**: Fokus pada pengembangan, validasi, dan diseminasi minimalis namun cukup untuk publikasi & uji lapangan kecil.

| No | Kategori | Item | Qty | Unit (Rp) | Total (Rp) |
|----|----------|------|-----|-----------|-----------|
| **1** | Gaji/Honor | Peneliti Utama (lead, 6 jam/mgg × 12 bln) | 12 bln | 2.000.000 | 24.000.000 |
| | | Asisten Riset (20 jam/mgg × 6 bln) | 6 bln | 1.000.000 | 6.000.000 |
| | **Subtotal Gaji** | | | | **30.000.000** |
| **2** | Operasional & Infrastruktur | Cloud/Hosting & domain (12 bln) | 1 | 2.000.000 | 2.000.000 |
| | | Honor uji pengguna (n=20 @ Rp150k) | 20 | 150.000 | 3.000.000 |
| | | Transport lokal & komunikasi | lumpsum | 3.000.000 | 3.000.000 |
| | **Subtotal Operasional** | | | | **8.000.000** |
| **3** | Publikasi & Diseminasi | Biaya publikasi/presentasi (1 paper/konf) | 1 | 7.000.000 | 7.000.000 |
| | | Materi pelatihan (cetak/online) | 1 | 1.000.000 | 1.000.000 |
| | **Subtotal Publikasi** | | | | **8.000.000** |
| **4** | Kontingensi (10%) | Cadangan risiko | - | - | 4.000.000 |
| **TOTAL** | | | | | **50.000.000** |

Catatan: Pembebanan gaji disesuaikan plafon; perangkat keras diasumsikan sudah tersedia. Jika diperlukan perangkat tambahan, diambil dari kontingensi atau substitusi honor.

---
## 2. Sitasi & Referensi Format IEEE
- In-text gunakan tanda kurung siku [n] sesuai urutan kemunculan.
- Daftar berikut sudah dinomori. Anda dapat mengganti sitasi di teks utama dengan nomor yang bersesuaian.

[1] World Health Organization, “Hypertension,” Fact Sheet, Sep. 2025. 
[2] K. T. Mills *et al.*, “Global disparities of hypertension prevalence and control,” *Circulation*, vol. 134, no. 6, pp. 441–450, 2016.
[3] GBD 2019 Diseases and Injuries Collaborators, “Global burden of 369 diseases and injuries…,” *Lancet*, vol. 396, pp. 1204–1222, 2020.
[4] Kementerian Kesehatan RI, “Riset Kesehatan Dasar (RISKESDAS) 2018,” Jakarta, 2018.
[5] Institute for Health Metrics and Evaluation, “GBD Results 2019 Dashboard,” 2020.
[6] AHA/ACC Task Force, “2017 ACC/AHA Guideline for the Management of Blood Pressure in Adults,” *J. Am. Coll. Cardiol.*, vol. 71, no. 6, pp. e127–e248, 2017.
[7] A. V. Chobanian *et al.*, “Seventh report of the Joint National Committee…,” *Hypertension*, vol. 42, no. 6, pp. 1206–1252, 2003.
[8] M. F. Fawcett, “An introduction to ROC analysis,” *Pattern Recognit. Lett.*, vol. 27, no. 8, pp. 861–874, 2006.
[9] T. Chen and C. Guestrin, “XGBoost: A scalable tree boosting system,” in *Proc. KDD*, 2016, pp. 785–794.
[10] J. H. Friedman, “Greedy function approximation: A gradient boosting machine,” *Ann. Statist.*, vol. 29, no. 5, pp. 1189–1232, 2001.
[11] L. Breiman, “Random forests,” *Mach. Learn.*, vol. 45, no. 1, pp. 5–32, 2001.
[12] R. Kohavi, “A study of cross-validation and bootstrap…,” in *IJCAI*, 1995, pp. 1137–1143.
[13] A. P. Bradley, “The use of the area under the ROC curve…,” *Pattern Recognit.*, vol. 30, no. 7, pp. 1145–1159, 1997.
[14] S. Lundberg and S.-I. Lee, “A unified approach to interpreting model predictions,” in *NeurIPS*, 2017, pp. 4765–4774.
[15] F. Pedregosa *et al.*, “Scikit-learn: Machine learning in Python,” *J. Mach. Learn. Res.*, vol. 12, pp. 2825–2830, 2011.
[16] T. Hastie, R. Tibshirani, and J. Friedman, *The Elements of Statistical Learning*, 2nd ed. Springer, 2009.
[17] J. R. Nielsen, *Usability Engineering*. Morgan Kaufmann, 2012.
[18] B. Shahriari *et al.*, “Taking the human out of the loop: A review of Bayesian optimization,” *Proc. IEEE*, vol. 104, no. 1, pp. 148–175, 2016.
[19] A. Rajkomar *et al.*, “Scalable and accurate deep learning with EHR,” *npj Digit. Med.*, vol. 1, no. 1, p. 18, 2018.
[20] P. Poirier *et al.*, “Obesity and cardiovascular disease,” *Circulation*, vol. 113, no. 6, pp. 898–918, 2006.
[21] F. J. He and G. A. MacGregor, “Salt and health…,” *J. Hum. Hypertens.*, vol. 23, pp. 363–384, 2009.
[22] S. Lewington *et al.*, “Age-specific relevance of usual blood pressure to vascular mortality,” *Lancet*, vol. 360, pp. 1903–1913, 2002.
[23] E. Knutson *et al.*, “Sleep duration and blood pressure,” *J. Hypertens.*, vol. 28, no. 10, pp. 1999–2007, 2010.
[24] W. B. Kannel and P. A. Wolf, “Framingham study insights…,” in *Supraventricular Arrhythmias*, Blackwell, 2008, pp. 63–79.
[25] P. Hopkins and R. Williams, “Genetics of hypertension,” Raven, 1981.
[26] S. P. Whelton *et al.*, “Effect of aerobic exercise on blood pressure,” *Ann. Intern. Med.*, vol. 136, no. 7, pp. 493–503, 2002.
[27] P. Primatesta *et al.*, “Left ventricular hypertrophy in white coat hypertension,” *J. Hum. Hypertens.*, vol. 15, no. 10, pp. 737–742, 2001.
[28] C. Metz, “Basic principles of ROC analysis,” *Semin. Nucl. Med.*, vol. 8, no. 4, pp. 283–298, 1978.
[29] A. Caruana *et al.*, “Intelligible models for healthcare,” in *KDD*, 2015, pp. 1721–1730.
[30] S. Ross, “Atherosclerosis: An inflammatory disease,” *N. Engl. J. Med.*, vol. 340, no. 2, pp. 115–126, 1999.
[31] WHO, *Pharmacological Treatment of Hypertension in Adults*, Geneva, 2021.
[32] WHO, *Global Action Plan on Physical Activity 2018–2030*, Geneva, 2019.
[33] Streamlit, “Streamlit Documentation,” 2023. [Online]. Available: https://docs.streamlit.io/
[34] Plotly, “Plotly Python Documentation,” 2023. [Online]. Available: https://plotly.com/python/
[35] Python Software Foundation, “Python 3 Docs,” 2023. [Online]. Available: https://docs.python.org/

---
## 3. Catatan Implementasi
- Untuk menyesuaikan dokumen utama, ganti setiap sitasi gaya author-year menjadi nomor [n] sesuai daftar di atas.
- RAB sudah diturunkan ke plafon Rp 50.000.000 dengan fokus pada honor minimalis, uji pengguna kecil, dan satu publikasi.
- Ringkasan eksekutif di atas dapat dipindah ke bagian depan proposal sebagai 2–3 halaman setara.

---
**Dokumen siap digunakan.**
