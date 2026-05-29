# Laporan Validasi Pseudo-Label Sentimen — Tahap 08

## 1. Informasi Dataset

- Nama file input: `youtube_comments_labeled_20260529_153650.csv`
- Waktu modifikasi file: `2026-05-29 15:37:10`
- Jumlah baris: `3670`
- Jumlah kolom: `24`

## 2. Validasi Kolom Utama

Kolom wajib yang diperiksa:

- `text_original`
- `text_clean`
- `sentiment_label`

Hasil validasi:

- Missing required columns: `[]`

## 3. Validasi Kategori Label

Kategori label yang diperbolehkan:

- `positif`
- `negatif`
- `netral`

Label unik yang ditemukan:

`['negatif', 'netral', 'positif']`

Label tidak valid yang ditemukan:

`[]`

## 4. Distribusi Label Sentimen

| sentiment_label | jumlah_komentar | proporsi_persen |
| --- | --- | --- |
| positif | 608 | 16.57 |
| negatif | 637 | 17.36 |
| netral | 2425 | 66.08 |

## 5. Ringkasan Ketidakseimbangan Label

- Label dominan: `netral`
- Jumlah label dominan: `2425`
- Proporsi label dominan: `66.08%`
- Label minoritas: `positif`
- Jumlah label minoritas: `608`
- Proporsi label minoritas: `16.57%`
- Rasio dominan terhadap minoritas: `3.99`
- Status distribusi: `Distribusi label cukup tidak seimbang.`

## 6. Ringkasan Status Sinyal Sentimen

| signal_status | jumlah_komentar | proporsi_persen |
| --- | --- | --- |
| no_lexicon_signal | 2277 | 62.04 |
| weak_single_signal | 786 | 21.42 |
| clearer_signal | 339 | 9.24 |
| mixed_or_ambiguous_signal | 268 | 7.3 |

## 7. Catatan Keterbatasan

Label sentimen pada dataset ini masih berupa pseudo-label yang dihasilkan menggunakan pendekatan lexicon/rule-based. Label tersebut belum dapat dianggap sebagai ground truth final.

Beberapa keterbatasan utama:

1. Sistem belum sepenuhnya memahami konteks kalimat.
2. Komentar YouTube banyak menggunakan bahasa informal, slang, singkatan, dan emotikon.
3. Sarkasme, sindiran, dan ironi sulit dikenali oleh pendekatan rule-based.
4. Komentar pendek dapat memiliki skor sentimen rendah.
5. Dominasi label netral perlu dibaca secara hati-hati.
6. Komentar dengan sinyal sentimen lemah perlu diperlakukan sebagai label dengan tingkat keyakinan terbatas.

## 8. Rekomendasi Tindak Lanjut

1. Melakukan pemeriksaan manual terbatas terhadap sampel komentar.
2. Memeriksa komentar dengan status sinyal lemah atau ambigu.
3. Mengevaluasi ulang lexicon jika ditemukan banyak ketidaksesuaian label.
4. Menjadikan pseudo-label sebagai label awal, bukan ground truth final.
5. Melanjutkan ke tahap persiapan modeling hanya setelah validasi label terdokumentasi.

## 9. Catatan Keamanan Data

Notebook ini tidak membaca file `.env`, tidak menampilkan API key, tidak menampilkan kolom `author`, dan tidak menyimpan ulang dataset komentar penuh.

Folder `data/raw/`, `data/processed/`, dan `data/labeled/` tidak boleh dipublikasikan ke GitHub.
