
# Laporan Ringkasan Tahap 12 — Tuning Sederhana dan Finalisasi Model Sentimen

## 1. Tujuan

Tahap ini bertujuan untuk melakukan tuning sederhana terhadap model klasifikasi sentimen berbasis TF-IDF.
Model yang diuji adalah LinearSVC dan Logistic Regression Balanced.

## 2. Dataset

Dataset modeling dibaca dari folder data/modeling/.

Nama file dataset:
youtube_comments_modeling_ready_20260529_171713.csv

Jumlah data setelah validasi:
3661 baris

Kolom fitur teks:
text_clean

Kolom target:
sentiment_label

## 3. Model yang Dibandingkan

Model yang dibandingkan meliputi:

1. Baseline TF-IDF + Multinomial Naive Bayes
2. TF-IDF + Logistic Regression Balanced Tahap 11
3. TF-IDF + LinearSVC Tahap 11
4. Tuned TF-IDF + LinearSVC
5. Tuned TF-IDF + Logistic Regression Balanced

## 4. Model Final

Model final terpilih:

Tuned TF-IDF + Logistic Regression Balanced

## 5. Metrik Model Final

Accuracy: 0.8881  
F1 Macro: 0.8607  
Recall Macro: 0.8661  
F1 Weighted: 0.8886  

F1-score kelas negatif: 0.8154  
Recall kelas negatif: 0.8346  

F1-score kelas positif: 0.8490  
Recall kelas positif: 0.8525  

## 6. Interpretasi

Model final dipilih karena memiliki performa terbaik berdasarkan prioritas F1 Macro, Recall Macro,
performa kelas negatif dan positif, serta F1 Weighted.

Hasil tuning menunjukkan bahwa pendekatan TF-IDF dengan model klasifikasi linear mampu memberikan
performa yang baik untuk klasifikasi sentimen komentar YouTube terkait isu pelemahan nilai rupiah.

## 7. Catatan Keamanan

Model artifact belum disimpan pada tahap ini karena pipeline TF-IDF memuat vocabulary teks.
Penyimpanan artifact akan dipertimbangkan pada tahap deployment lokal dengan tetap menjaga keamanan data.
