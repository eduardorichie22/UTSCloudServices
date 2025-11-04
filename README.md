# 🚀 UTS Cloud Services - MU News App

Ini adalah proyek Ujian Tengah Semester mata kuliah Cloud Services (COMP6991031).

Aplikasi ini adalah web app sederhana yang dibuat dengan Python Flask untuk menampilkan berita terbaru Manchester United, yang kemudian di-containerize menggunakan Docker dan di-deploy secara otomatis dengan GitHub Actions CI/CD.

---

## 🛠️ Teknologi yang Digunakan

* **Backend:** Python (Flask)
* **Containerization:** Docker
* **CI/CD:** GitHub Actions
* **Registry:** GitHub Packages (Container Registry)

---

## 🏃‍♂️ Cara Menjalankan (Siap Pakai)

Anda tidak perlu `git clone` atau `docker build`. Anda bisa langsung menjalankan *image* yang sudah dipublikasikan ke GitHub Container Registry.

Pastikan **Docker Desktop** Anda sedang berjalan, lalu jalankan dua perintah berikut di terminal Anda:

### 1. Tarik (Pull) Image
Perintah ini mengunduh *image* yang sudah jadi dari *registry* GitHub.

docker pull ghcr.io/eduardorichie22/utscloudservices:latest

2. Jalankan (Run) Container
Perintah ini menjalankan image yang sudah diunduh.

docker run -d -p 5000:5000 ghcr.io/eduardorichie22/utscloudservices:latest

3. Buka Aplikasi
Buka browser Anda dan pergi ke alamat:

http://localhost:5000