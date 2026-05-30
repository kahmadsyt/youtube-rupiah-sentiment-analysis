
import streamlit as st
import joblib
from pathlib import Path


# ============================================================
# Konfigurasi Path
# ============================================================

APP_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = APP_DIR.parent

MODEL_PATH = PROJECT_ROOT / "model_artifacts" / "sentiment_model_tfidf_logreg_balanced.joblib"


# ============================================================
# Load Model
# ============================================================

@st.cache_resource
def load_model():
    """
    Memuat model pipeline TF-IDF + Logistic Regression Balanced.
    Model hanya dibaca dari artifact lokal dan tidak membaca dataset komentar.
    """
    if not MODEL_PATH.exists():
        st.error("File model tidak ditemukan. Pastikan model artifact sudah dibuat di folder model_artifacts/.")
        st.stop()

    model = joblib.load(MODEL_PATH)
    return model


# ============================================================
# Fungsi Prediksi
# ============================================================

def predict_sentiment(model, text):
    """
    Melakukan prediksi sentimen dari input teks manual.
    """
    text = str(text).strip()

    if not text:
        return None

    prediction = model.predict([text])[0]
    return prediction


# ============================================================
# UI Streamlit
# ============================================================

st.set_page_config(
    page_title="Analisis Sentimen Rupiah",
    page_icon="📊",
    layout="centered"
)

st.title("Analisis Sentimen Komentar YouTube terhadap Isu Pelemahan Rupiah")

st.write(
    "Aplikasi ini menggunakan model Machine Learning berbasis TF-IDF dan Logistic Regression "
    "untuk memprediksi sentimen dari teks komentar yang dimasukkan secara manual."
)

st.info(
    "Catatan: Aplikasi ini tidak membaca dataset komentar YouTube, tidak menggunakan YouTube API, "
    "dan tidak menampilkan data mentah komentar."
)

model = load_model()

user_input = st.text_area(
    "Masukkan teks komentar:",
    height=150,
    placeholder="Contoh: Rupiah melemah membuat harga kebutuhan semakin mahal..."
)

predict_button = st.button("Prediksi Sentimen")

if predict_button:
    if not user_input.strip():
        st.warning("Silakan masukkan teks komentar terlebih dahulu.")
    else:
        prediction = predict_sentiment(model, user_input)

        st.subheader("Hasil Prediksi")

        if prediction == "positif":
            st.success(f"Sentimen: {prediction.upper()}")
        elif prediction == "negatif":
            st.error(f"Sentimen: {prediction.upper()}")
        else:
            st.warning(f"Sentimen: {prediction.upper()}")

        st.write(
            "Interpretasi: hasil prediksi ini merupakan estimasi model berdasarkan pola teks "
            "yang dipelajari dari data training. Hasil tetap perlu dipahami sebagai bantuan analisis, "
            "bukan sebagai kesimpulan mutlak."
        )

st.caption("Model: Tuned TF-IDF + Logistic Regression Balanced")
