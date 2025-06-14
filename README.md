# 📌 Tugas Akhir Visual Programming: Pomodoro Habit Tracker

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
