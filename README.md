# 📌 Tugas Akhir Pemrograman Visual : Pomodoro Habit Tracker

---

## 🧠 Deskripsi Aplikasi

Aplikasi ini merupakan proyek tugas akhir mata kuliah **Visual Programming (PyQt5)** yang bertujuan membantu pengguna dalam membentuk kebiasaan produktif melalui pendekatan **habit tracking** dan **Pomodoro Timer**.

User dapat menambahkan task sesuai tanggal, melihat daftar reminder, serta menggunakan timer fokus yang disertai notifikasi suara.

---

## 🎯 Fitur Utama

| Fitur                  | Keterangan                                                                 |
|------------------------|----------------------------------------------------------------------------|
| ✅ **Menu Bar**        | Menu File, Export (CSV, PDF), Help, Exit                                   |
| ✅ **Status Bar**      | Menampilkan nama lengkap & NIM secara statis                               |
| ✅ **Database SQLite** | Menyimpan data task (title, category, date, time, notes) secara lokal       |
| ✅ **Reminder View**   | Menampilkan task berdasarkan tanggal yang dipilih di kalender              |
| ✅ **Export Data**     | Ekspor task ke file `CSV` dan `PDF`                                        |
| ✅ **Pomodoro Timer**  | Timer fokus dengan kontrol durasi, notifikasi suara saat selesai           |
| ✅ **StyleSheet**      | Styling custom untuk kalender, tombol, timer, dan frame (via Qt Designer)  |

---

## 🧩 Struktur Folder

├── db.py                     # Modul SQLite
├── export.py                 # Export ke CSV & PDF
├── add_task_dialog.py        # Form input task
├── Calendar.py               # File Utama
├── Calendar.ui               # File Qt Designer
├── sounds/
│ └── ding.wav # Suara notifikasi timer
├── asset/
│ └── minus.png
│ └── plus (1).png
│ └── plus (2).png
└── habit_data.db # Auto-generated DB saat run

---

## Data Mahasiswa

Dibuat oleh **Rizki Rahman Maulana (F1D022093)** dengan `Qt Designer` dan `Vs Code`

---

## Proses

1. Design UI di qt designer <br>
![Screenshot (951)](https://github.com/user-attachments/assets/894f66e6-d412-4da2-8d0d-e11d53d8758b)
2. Convert hasil qt designer yang berformat `.ui` ke format `.py` <br>
![Screenshot (952)](https://github.com/user-attachments/assets/92441bbc-700c-437a-b606-49fdb4d37e33)
3. Tertampil hasil convert `.ui`
![Screenshot (961)](https://github.com/user-attachments/assets/90e173e0-ff3d-46f6-bca6-aa2da3afc79b)
5. Tampilan hasil run aplikasi <br>
  - Tampilan Utama
    ![Screenshot (962)](https://github.com/user-attachments/assets/72eb56df-a527-4f3a-9c3d-5318a8fd2a78)
  -  Tampilan Add Task
    ![Screenshot (964)](https://github.com/user-attachments/assets/ce1be3f0-8bbe-406e-b703-8e20759a8126)
  -  Tampilan Task Bertambah di Kalendar
    ![Screenshot (965)](https://github.com/user-attachments/assets/dc6a7332-c11c-47c6-8e54-79440c2971af)
  -  Mencoba fitur Pomodoro
    ![Screenshot (966)](https://github.com/user-attachments/assets/e139de2f-6b86-4817-8e07-c76814b822e6)
  -  Timer Selesai
    ![Screenshot (967)](https://github.com/user-attachments/assets/2178d17d-e1fa-4264-b79b-81c11c0e15cc)
  -   Coba export CSV or PDF
    ![Screenshot (968)](https://github.com/user-attachments/assets/4ac9f9ca-7c23-46c3-810c-07b75b475f44)
  -  Tampilan Output CSV
    ![Screenshot (970)](https://github.com/user-attachments/assets/21fac3a6-19a3-4be1-868c-f98c8ffa4776)
  -  Tampilan output PDF
    ![Screenshot (969)](https://github.com/user-attachments/assets/4b4814fa-2c82-4e51-98fa-6375be60b591)

---
