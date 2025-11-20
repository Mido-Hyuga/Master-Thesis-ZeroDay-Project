# app.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.metrics import classification_report, accuracy_score
import hashlib
from web3 import Web3
import tkinter as tk
from tkinter import messagebox

# ========================================
# 1️⃣ TRAIN MODEL
# ========================================
def train_model():
    global rf, iso, X_test, y_test
    try:
        df = pd.read_csv("datasets/merged_dataset.csv")
        df.columns = df.columns.str.strip()
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)
        df["attack"] = df["Label"].apply(lambda x: 0 if x.lower() == "benign" else 1)
        X = df.drop(columns=["Label", "attack"])
        y = df["attack"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42, stratify=y
        )

        rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
        rf.fit(X_train, y_train)

        iso = IsolationForest(contamination=0.1, random_state=42, n_jobs=-1)
        iso.fit(X_train)

        messagebox.showinfo("Success", "✅ Model trained successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Training failed:\n{e}")

# ========================================
# 2️⃣ TEST MODEL, SAVE RESULTS, HASH FILE
# ========================================
def test_and_hash():
    global hash_value
    try:
        df_web = pd.read_csv("datasets/WebAttacks_benign.csv")
        df_web.columns = df_web.columns.str.strip()
        df_web.replace([np.inf, -np.inf], np.nan, inplace=True)
        df_web.dropna(inplace=True)
        df_web["attack"] = df_web["Label"].apply(lambda x: 0 if x.lower() == "benign" else 1)
        X_web = df_web.drop(columns=["Label", "attack"])
        y_web = df_web["attack"]

        y_pred_rf = rf.predict(X_web)
        y_pred_iso = iso.predict(X_web)
        y_pred_iso = np.where(y_pred_iso == -1, 1, 0)
        y_pred_hybrid = np.where((y_pred_rf == 1) | (y_pred_iso == 1), 1, 0)

        acc_rf = accuracy_score(y_web, y_pred_rf)
        acc_iso = accuracy_score(y_web, y_pred_iso)
        acc_hybrid = accuracy_score(y_web, y_pred_hybrid)

        df_results = pd.DataFrame({
            "Model": ["RandomForest", "IsolationForest", "Hybrid"],
            "Accuracy": [acc_rf, acc_iso, acc_hybrid]
        })
        df_results.to_csv("results.csv", index=False)

        with open("results.csv", "rb") as f:
            data = f.read()
            hash_value = hashlib.sha256(data).hexdigest()

        messagebox.showinfo("Hashed", f"✅ Results saved and hashed!\nHash:\n{hash_value[:32]}...")
    except Exception as e:
        messagebox.showerror("Error", f"Testing failed:\n{e}")

# ========================================
# 3️⃣ STORE HASH ON GANACHE BLOCKCHAIN
# ========================================
def store_hash():
    try:
        ganache_url = "http://ganache:8545"
        w3 = Web3(Web3.HTTPProvider(ganache_url))

        if not w3.is_connected():
            messagebox.showerror("Error", "❌ Cannot connect to Ganache!")
            return

        account = w3.eth.accounts[0]
        tx = {
            'from': account,
            'to': account,
            'value': 0,
            'gas': 2000000,
            'gasPrice': w3.to_wei('50', 'gwei'),
            'data': w3.to_hex(text=hash_value)
        }

        tx_hash = w3.eth.send_transaction(tx)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        messagebox.showinfo("Blockchain", f"✅ Hash stored on blockchain!\nTx: {tx_hash.hex()}")
    except Exception as e:
        messagebox.showerror("Error", f"Blockchain storage failed:\n{e}")

# ========================================
# 🖥️ SIMPLE TKINTER INTERFACE
# ========================================
root = tk.Tk()
root.title("Zero-Day Detection App")
root.geometry("400x250")

tk.Label(root, text="Zero-Day Detection System", font=("Arial", 14, "bold")).pack(pady=10)
tk.Button(root, text="Train Model", command=train_model, width=25, height=2).pack(pady=5)
tk.Button(root, text="Test & Hash Results", command=test_and_hash, width=25, height=2).pack(pady=5)
tk.Button(root, text="Store Hash on Blockchain", command=store_hash, width=25, height=2).pack(pady=5)

root.mainloop()
