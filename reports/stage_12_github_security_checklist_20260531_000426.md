
# Checklist Keamanan GitHub — Tahap 12

## File yang boleh dipush

- Notebook .ipynb
- Laporan ringkasan agregat di folder reports/
- Metadata evaluasi model yang tidak memuat komentar asli
- Visualisasi agregat seperti grafik metrik dan confusion matrix
- File .gitignore
- README.md

## File yang tidak boleh dipush

- .env
- API key YouTube
- data/raw/
- data/processed/
- data/labeled/
- data/modeling/
- Dataset komentar penuh
- File yang memuat kolom author
- Model artifact yang memuat vocabulary TF-IDF
- File hasil prediksi yang berisi komentar asli secara penuh

## Catatan

Model final pada tahap ini belum disimpan sebagai artifact file.
Hal ini dilakukan karena pipeline TF-IDF memuat vocabulary teks yang berasal dari dataset komentar.

Checklist dibuat pada:
20260531_000426
