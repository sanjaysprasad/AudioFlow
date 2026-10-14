# 🎵 AudioFlow — YouTube & Instagram Audio Extractor

> A modern, studio-grade media audio extractor for **YouTube** and **Instagram**, featuring both a **macOS Desktop GUI** and a **Mobile/PC Responsive Web Application**.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=flat&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat&logo=docker&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-v3-38B2AC?style=flat&logo=tailwind-css&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

---

## ✨ Features

- **Multi-Platform Support**:
  - **YouTube**: Standard videos, Shorts, Playlists, and YouTube Music (`music.youtube.com`).
  - **Instagram**: Reels, Posts, and IGTV clips.
- **Audio Formats & Master Quality**:
  - `MP3`: 320 kbps (Maximum), 256 kbps, 192 kbps, 128 kbps, or VBR.
  - `FLAC`: Studio-grade lossless original master fidelity.
  - `WAV`: Raw uncompressed PCM audio.
  - `AAC`: Modern high-efficiency audio.
  - `OPUS`: Ultra-efficient low-latency audio codec.
- **Smart Tracking Sanitizer**: Automatically removes tracking tokens (`?si=...`, `?igsh=...`, `utm_*`).
- **Cover Artwork & Metadata**: Automatically embeds high-res thumbnail covers and ID3 metadata (Artist, Title, Album) into the exported audio files.
- **Dual Interface**:
  - 🖥️ **Desktop App**: Dark-mode GUI with progress bars and folder picker.
  - 📱 **Web App**: Responsive glassmorphism interface that works seamlessly on iPhone, Android, and Desktop browsers.
- **Docker & Cloud Ready**: Includes a production `Dockerfile` ready for 1-click free deployment on Render, Koyeb, or Docker hosts.

---

## 🚀 Quick Start

### 1. Web Application (Mobile & PC)
Run the local web server:
```bash
python3 server.py
```
Open **[http://localhost:8000](http://localhost:8000)** in your browser.

To share a **public HTTPS link** for your phone or friends with zero configuration:
```bash
python3 run_public.py
# Or double-click launch_public_website.command
```

### 2. Desktop Application
Launch the standalone GUI:
```bash
python3 app.py
# Or double-click launch_desktop.command
```

---

## 🐳 Docker Deployment

Build and run with Docker:
```bash
docker build -t audioflow .
docker run -p 7860:7860 audioflow
```

---

## 🛠 Prerequisites

- `python3` (3.11+)
- `ffmpeg` (for audio transcoding)
- Dependencies: `pip install -r requirements.txt`

---

## ⚖️ Disclaimer & License

Distributed under the MIT License. This tool is intended for personal backup, offline listening, and fair-use archiving of public media.
