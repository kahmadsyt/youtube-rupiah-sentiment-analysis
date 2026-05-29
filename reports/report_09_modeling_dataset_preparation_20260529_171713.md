# Report 09 - Modeling Dataset Preparation

## 1. Ringkasan Tahap

Tahap ini bertujuan untuk menyiapkan dataset hasil labeling sentimen agar siap digunakan pada tahap modeling machine learning.

Pada tahap ini belum dilakukan training model. Fokus utama tahap ini adalah validasi dataset, pembersihan nilai kosong, normalisasi label, penghapusan duplikasi, pemeriksaan distribusi target, dan penyimpanan dataset siap modeling secara lokal.

## 2. Sumber Dataset

- File sumber: `youtube_comments_labeled_20260529_153650.csv`
- Folder sumber: `data/labeled/`
- Waktu modifikasi file sumber: `2026-05-29 15:37:10`

## 3. Output Dataset Modeling

- File output lokal: `youtube_comments_modeling_ready_20260529_171713.csv`
- Folder output lokal: `data/modeling/`
- Jumlah baris awal: `3670`
- Jumlah baris setelah drop nilai kosong: `3670`
- Jumlah duplikasi dihapus: `9`
- Jumlah baris akhir: `3661`
- Jumlah kolom akhir: `2`

## 4. Kolom Modeling

| Kolom | Peran |
|---|---|
| `text_clean` | Fitur teks |
| `sentiment_label` | Target sentimen |

## 5. Distribusi Target Setelah Pembersihan

| sentiment_label   |   jumlah |   persentase |
|:------------------|---------:|-------------:|
| netral            |     2416 |        65.99 |
| negatif           |      637 |        17.4  |
| positif           |      608 |        16.61 |

## 6. Ringkasan Distribusi Target

| metrik                           | nilai   |
|:---------------------------------|:--------|
| Total data siap modeling         | 3661    |
| Label dominan                    | netral  |
| Jumlah label dominan             | 2416    |
| Persentase label dominan         | 65.99%  |
| Label minoritas                  | positif |
| Jumlah label minoritas           | 608     |
| Persentase label minoritas       | 16.61%  |
| Rasio dominan terhadap minoritas | 3.97    |

## 7. Catatan Keamanan

- File `.env` tidak dibaca dan tidak ditampilkan.
- API key tidak dibaca dan tidak ditampilkan.
- Kolom `author` tidak digunakan dan tidak ditampilkan.
- Dataset komentar penuh tidak boleh dipublikasikan ke GitHub.
- Folder `data/modeling/` tidak boleh dipublikasikan ke GitHub.
- File yang aman untuk GitHub adalah notebook, metadata, laporan ringkasan, dan visualisasi agregat.

## 8. Kesimpulan

Dataset siap modeling telah berhasil disiapkan secara lokal. Dataset ini dapat digunakan pada tahap berikutnya untuk proses feature extraction dan training model machine learning.

Namun, karena dataset masih memuat teks komentar hasil preprocessing, file dataset pada folder `data/modeling/` tetap harus dikecualikan dari GitHub.
