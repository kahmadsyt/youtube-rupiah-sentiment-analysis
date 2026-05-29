# Import library utama Streamlit
import streamlit as st

# Konfigurasi halaman dashboard
st.set_page_config(
    page_title="YouTube Rupiah Sentiment Analysis",
    page_icon="📊",
    layout="wide"
)

# Judul aplikasi
st.title("📊 YouTube Rupiah Sentiment Analysis")

# Deskripsi singkat aplikasi
st.write(
    """
    Dashboard ini akan digunakan untuk menampilkan hasil analisis sentimen komentar YouTube
    terkait isu pelemahan nilai rupiah, inflasi, kenaikan harga kebutuhan pokok,
    dan persepsi daya beli masyarakat.
    """
)

# Informasi status awal
st.info("Aplikasi Streamlit awal berhasil dijalankan. Data dan model akan ditambahkan pada tahap berikutnya.")