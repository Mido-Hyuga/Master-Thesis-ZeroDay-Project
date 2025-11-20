# Distributed System using DOCKER 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣶⣶⣶⠀⣶⣶⣶⣶⠀⢰⣶⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⣿⣿⣿⣿⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣤⣤⣤⠀⢠⣤⣤⣤⠀⣤⣤⣤⣤⠀⢠⣤⣤⣤⠀⣰⣿⣿⣦⡀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⠀⢸⣿⣿⣿⠀⣿⣿⣿⣿⠀⢸⣿⣿⣿⠀⣿⣿⠹⣿⣷⣀⠀⠀⠀
⠀⠘⠛⠛⠛⠀⠘⠛⠛⠛⠀⠛⠛⠛⠛⠀⠘⠛⠛⠛⢀⣿⣿⡀⠙⠿⠿⣿⣶⣆
⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⠟⢁⣤⣴⣶⣾⡿⠋
⣿⣿⣿⣛⣛⣛⣛⣿⣟⣛⣛⣻⣿⣟⣛⣛⣻⣿⣟⣋⣉⣠⣤⣾⣿⣟⣻⣍⠀⠀
⢹⣿⣿⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠋⠀⠀⠀⠀⠀
⠈⢻⣿⣿⣿⡿⠿⠿⠿⠛⠉⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠙⢿⣿⣿⣶⣦⣤⣤⣤⣤⣤⣴⣶⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠛⠿⠿⠿⠿⠿⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 

![Global Architecture](../images/docker-architecture.jpg)

---

## ⚙️ Step-by-Step Instructions

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/<USERNAME>/ZeroDay-Detection-AI-Blockchain.git
cd ZeroDay-Detection-AI-Blockchain
```

---

### **2️⃣ Create Ganache Container (Blockchain Simulation)**

```bash
docker run -d --name ganache-local -p 7545:7545 trufflesuite/ganache-cli
```
- `-d` → run in detached mode  
- `--name ganache-local` → container name  
- `-p 7545:7545` → map Ganache UI port to host  
- Starts a local Ethereum blockchain simulator for testing

---

### **3️⃣ Create Python Container and Link with Ganache**

```bash
docker run -it --name py-run --link ganache-local:ganache -v "%cd%":/app -w /app python:3.9 bash
```
- `--link ganache-local:ganache` → links Python container to Ganache  
- `-v "%cd%":/app` → mounts current project directory inside container  
- `-w /app` → sets working directory inside container  
- `-it` → interactive terminal to enter the container

Now you are **inside the Python container**.

---

### **4️⃣ Install Python Libraries inside the Container**

```bash
pip install pandas numpy scikit-learn matplotlib seaborn web3
```

---

### **5️⃣ Install System Libraries for GUI**

```bash
apt-get update && apt-get install -y python3-tk
apt-get install -y libxrender-dev libx11-6 libxext-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev libxtst-dev tk-dev
```
- Required to run **Tkinter GUI** (Python GUI library)

---

### **6️⃣ Setup X Server for GUI**

1. Install **XLaunch** (Windows) or **XQuartz** (Mac)  
2. Start the X server  
3. In the Python container, export the DISPLAY environment variable:

```bash
export DISPLAY=<your-ip-address>:0
```
- Replace `<your-ip-address>` with your host machine's IP  
- `:0` is the display number (change if multiple sessions)

---

### **7️⃣ Run the Application**

Inside the Python container:

```bash
python3 app.py
```
- GUI should appear on your host machine through X11 forwarding  
- Interact with the application and train/test the AI model

---

### **8️⃣ Training the AI Model**

1. Load the **CICIDS2017 dataset**  
2. Preprocess data (clean, scale, split)  
3. Train the ML model using scripts (`train_model.py` or `app.py`)  
4. Test detection of Zero-Day attacks in simulated distributed systems


