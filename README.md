# 🚀 Raspberry Pi Python Projects

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?style=for-the-badge)
![Testing](https://img.shields.io/badge/Testing-PyTest-orange?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi-red?style=for-the-badge)

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

Features:

- Sensor abstraction
- Alert system
- Unit testing with mocks

---

### 🔐 Smart Door Lock System

Simulates a PIN based door lock.

Features:

- Authentication service
- Lock controller
- Keypad input simulation

---

### 🏠 Home Automation API

Control devices using REST API.

Endpoints:
POST /light/on
POST /light/off


---

# ⚙️ Installation


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