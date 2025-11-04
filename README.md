# 🚀 UTS Cloud Services - MU News App

Ini adalah proyek Ujian Tengah Semester mata kuliah Cloud Services (COMP6991031).

Aplikasi ini adalah web app sederhana yang dibuat dengan Python Flask untuk menampilkan berita terbaru Manchester United, yang kemudian di-containerize menggunakan Docker dan di-deploy secara otomatis dengan GitHub Actions CI/CD.

---

## 🏃‍♂️ Cara Menjalankan (Metode 1: Registry - Direkomendasikan)

Ini adalah cara standar dan paling profesional. Anda tidak perlu `git clone`. Anda bisa langsung menjalankan *image* yang sudah dipublikasikan ke GitHub Container Registry.

Pastikan **Docker Desktop** Anda sedang berjalan, lalu jalankan dua perintah berikut di terminal Anda:

### 1. Tarik (Pull) Image
Perintah ini mengunduh *image* yang sudah jadi dari *registry* GitHub.

docker pull ghcr.io/eduardorichie22/utscloudservices:latest

2. Jalankan (Run) Container
Perintah ini menjalankan image yang sudah di download.

docker run -d -p 5000:5000 ghcr.io/eduardorichie22/utscloudservices:latest

3. Buka Aplikasi
Buka browser Anda dan pergi ke alamat:

http://localhost:5000

📦 [Alternatif] Cara Menjalankan (Metode 2: Manual via .tar)
Klik di sini untuk instruksi manual menggunakan file .tar

Metode ini digunakan jika Anda tidak bisa mengakses registry dan memiliki file .tar secara manual.

1. Unduh File Image
Unduh file mu-news-app.tar dari halaman Releases repositori ini.

2. Muat (Load) Image
Buka terminal Anda di folder tempat Anda mengunduh file .tar, lalu jalankan:

docker load -i mu-news-app.tar
Ini akan memuat image bernama mu-news-app:latest ke Docker Desktop Anda.

3. Jalankan (Run) Container
Perintah ini menjalankan image yang baru saja Anda muat.

docker run -d -p 5000:5000 mu-news-app:latest
4. Buka Aplikasi
Buka browser Anda dan pergi ke alamat:

http://localhost:5000
