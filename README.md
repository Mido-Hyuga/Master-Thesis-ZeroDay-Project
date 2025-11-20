# ZeroDay-Detection-AI-Blockchain

📚 **Project Overview**  
This project focuses on detecting Zero-Day attacks in distributed systems by leveraging **Artificial Intelligence (Machine Learning)** and **Blockchain technology**. The system collects data from networked components, trains an AI model on known attack patterns, and monitors new activities to identify potential threats. Blockchain ensures data integrity and traceability across distributed nodes.

---

## 📝 Author and Institution

- **Author:** BOUSLAM EL MEHDI  
- **Institution:** ENSA - Ibn Tofail University  
- **Program:** Master's in Information Systems Security  
- **Academic Year:** 2024-2025  

---

## 🖼 Architecture

![Global Architecture](images/architecture-global.png)

---

## 🔧 Requirements

### Software
- Docker & Docker Compose  
- Python 3.9  
- X11 server (for GUI, e.g., XLaunch on Windows)  
- Git  

### Python Libraries
- pandas  
- numpy  
- scikit-learn  
- matplotlib  
- seaborn  
- web3  

### System Libraries
- python3-tk  
- libxrender-dev  
- libx11-6  
- libxext-dev  
- libxinerama-dev  
- libxi-dev  
- libxrandr-dev  
- libxcursor-dev  
- libxtst-dev  
- tk-dev  

### Dataset
- **CICIDS2017:** [https://www.unb.ca/cic/datasets/](https://www.unb.ca/cic/datasets/)

---


## 📂 Project Structure
ZeroDay-Detection-AI-Blockchain/
│
├─ app.py                # Main application GUI
├─
├─ data/                 # Datasets (CICIDS2017)
├─ images/               # Architecture images
│   └─ architectures.png
├─ docker/               # Docker setup & instructions
│   └─ README.md
|
├─ requirements.txt      # Python dependencies
└─ README.md             # Project documentation

---

## 🚀 Usage

- Start Ganache container

- Run Python container and link to Ganache

- Install dependencies and system libraries

- Export DISPLAY for GUI

- Launch the application: python3 app.py

- Train or test the AI model

---

## 🖊️ Notes

- Keep **Ganache** and **Python containers** running while using the GUI  
- Make sure X server is running for GUI operations  
- Any outputs generated in `/app` are persisted to host machine
- Read README file inside Docker Folder ⚠️🚨📌❗
---

## 📖 References

- CICIDS2017 Dataset: [https://www.unb.ca/cic/datasets/](https://www.unb.ca/cic/datasets/)  
- Ganache CLI: [https://trufflesuite.com/ganache/](https://trufflesuite.com/ganache/)  
- Python Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, web3

---

**End of README**

