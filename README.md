# 🔐 XSS Attack Detection using Machine Learning

## 📌 Project Overview
This project focuses on detecting **Cross-Site Scripting (XSS) attacks** using a machine learning approach.  
A **Random Forest Classifier** is trained on a dataset to classify whether input data is **malicious (XSS)** or **benign (normal)**.

---

## 🎯 Objectives
- Detect XSS attacks automatically using ML
- Preprocess and analyze dataset
- Train and evaluate a classification model
- Generate performance metrics and report

---

## 📂 Dataset
- File: `XSS Attack Dataset with 461 entries.xlsx`
- Contains:
  - App Names
  - Permissions
  - API Name
  - Website Name
  - IP Address
  - Location
  - Label (Yes = Attack, No = Normal)

---

## ⚙️ Technologies Used
- Python 🐍
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn (optional)
- OpenPyXL (for Excel reading)

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install pandas numpy scikit-learn matplotlib seaborn openpyxl
