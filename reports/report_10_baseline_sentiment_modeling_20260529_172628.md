# Report 10 - Baseline Sentiment Modeling

## 1. Ringkasan Tahap

Tahap ini membangun model baseline untuk klasifikasi sentimen komentar YouTube terhadap isu pelemahan nilai rupiah.

Model baseline yang digunakan:

- Feature extraction: TF-IDF
- Model: Multinomial Naive Bayes

## 2. Dataset

- File input lokal: `youtube_comments_modeling_ready_20260529_171713.csv`
- Folder input: `data/modeling/`
- Jumlah data total: `3661`
- Jumlah data latih: `2928`
- Jumlah data uji: `733`

## 3. Evaluasi Metrik Utama

| metrik             |   nilai |
|:-------------------|--------:|
| Accuracy           |  0.678  |
| Precision Macro    |  0.8576 |
| Recall Macro       |  0.3699 |
| F1-Score Macro     |  0.3379 |
| Precision Weighted |  0.7666 |
| Recall Weighted    |  0.678  |
| F1-Score Weighted  |  0.5665 |

## 4. Classification Report

| label        |   precision |   recall |   f1-score |   support |
|:-------------|------------:|---------:|-----------:|----------:|
| negatif      |      0.9    |   0.0709 |     0.1314 |   127     |
| netral       |      0.6727 |   0.9979 |     0.8037 |   484     |
| positif      |      1      |   0.041  |     0.0787 |   122     |
| accuracy     |      0.678  |   0.678  |     0.678  |     0.678 |
| macro avg    |      0.8576 |   0.3699 |     0.3379 |   733     |
| weighted avg |      0.7666 |   0.678  |     0.5665 |   733     |

## 5. Confusion Matrix

|                |   Predicted negatif |   Predicted netral |   Predicted positif |
|:---------------|--------------------:|-------------------:|--------------------:|
| Actual negatif |                   9 |                118 |                   0 |
| Actual netral  |                   1 |                483 |                   0 |
| Actual positif |                   0 |                117 |                   5 |

## 6. Catatan Keamanan

- File `.env` tidak dibaca.
- API key tidak ditampilkan.
- Kolom `author` tidak digunakan.
- Isi komentar tidak ditampilkan dalam laporan.
- Dataset pada folder `data/modeling/` tidak boleh dipublikasikan ke GitHub.

## 7. Kesimpulan Awal

Model baseline TF-IDF + Multinomial Naive Bayes telah berhasil dilatih dan dievaluasi.

Hasil evaluasi ini menjadi acuan awal untuk membandingkan model lain pada tahap berikutnya.
