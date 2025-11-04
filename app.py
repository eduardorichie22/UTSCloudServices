import feedparser
import requests
import textwrap
from flask import Flask, render_template

# Buat aplikasi web Flask
app = Flask(__name__)

MANU_NEWS_URL = "https://www.manchestereveningnews.co.uk/all-about/manchester-united-fc?service=rss"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def fetch_news_data():
    """Fungsi ini mengambil data dan me-return LIST berisi dictionary."""
    berita_list = []
    try:
        response = requests.get(MANU_NEWS_URL, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return [] # Return list kosong jika gagal

        feed = feedparser.parse(response.content)
        
        if feed.entries:
            for entry in feed.entries[:5]: # Ambil 5 berita
                berita_item = {
                    'title': entry.title if 'title' in entry else "Tanpa Judul",
                    'link': entry.link if 'link' in entry else "#",
                    'summary': entry.summary if 'summary' in entry else "Tanpa Ringkasan"
                }
                berita_list.append(berita_item)
        
        return berita_list
        
    except Exception as e:
        print(f"Error saat fetch berita: {e}")
        return [] # Return list kosong jika ada error

# Ini adalah 'rute' (halaman) utama website Anda
@app.route('/')
def home():
    # 1. Panggil fungsi untuk ambil data
    data_berita = fetch_news_data()
    
    # 2. 'Render' file index.html dan kirim data beritanya
    return render_template('index.html', berita_list=data_berita)

# Perintah untuk menjalankan server saat file ini dieksekusi
if __name__ == "__main__":
    # host='0.0.0.0' penting agar bisa diakses dari luar container Docker
    app.run(host='0.0.0.0', port=5000)