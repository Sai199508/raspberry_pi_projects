# 🚀 Raspberry Pi Python Projects

[![CI/CD](https://github.com/<YOUR_USERNAME>/<REPO_NAME>/actions/workflows/ci.yml/badge.svg)](https://github.com/<YOUR_USERNAME>/<REPO_NAME>/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?style=for-the-badge)
![Testing](https://img.shields.io/badge/Testing-PyTest-orange?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi-red?style=for-the-badge)
[![Coverage](https://img.shields.io/badge/Coverage-0%25-lightgrey?style=for-the-badge)](https://github.com/<YOUR_USERNAME>/<REPO_NAME>/actions/workflows/ci.yml) <!-- Automatic coverage badge if you configure Codecov or Coveralls later -->

---

# 🧠 Overview

This repository contains **IoT and Raspberry Pi projects** built using Python.

The goal is to demonstrate:

✔ Hardware integration  
✔ Modular service architecture  
✔ Mock-based testing  
✔ REST API design  

---

# 📂 Projects

### 🌡 Smart Temperature Monitoring

Monitors room temperature and triggers alerts.

**Features:**

- Sensor abstraction
- Alert system
- Unit testing with mocks

---

### 🔐 Smart Door Lock System

Simulates a PIN based door lock.

**Features:**

- Authentication service
- Lock controller
- Keypad input simulation

---

### 🏠 Home Automation API

Control devices using REST API.

**Endpoints:**

- `POST /light/on`
- `POST /light/off`

---

# ⚙️ Installation

```bash
pip install -r requirements.txt


---

# 🧪 Run Tests


pytest


---

# ▶ Run API

cd home_automation_api

uvicorn main:app --reload

Access API at: http://127.0.0.1:8000


---

# 🧠 Technologies

Python  
FastAPI  
PyTest  
Raspberry Pi  

---
# 📈 Continuous Integration

✅ Tests (PyTest + Mock-based)
✅ Linting (Flake8)
✅ Type Checking (MyPy)
✅ Coverage (Coverage.py, badge will update after adding Codecov)

# 🚀 Future Improvements

Add real GPIO integration  
Add MQTT IoT communication  
Add mobile dashboard  

---

# 👨‍💻 Author

**SaiKumar**

GitHub
https://github.com/Sai199508

---

# ⭐ Support

If you found this project helpful, please consider **starring ⭐ the repository**.

---

# 📜 License

This project is available for **learning and educational purposes**.
