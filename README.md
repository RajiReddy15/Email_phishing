# 📧 Phishing Email Detection using NLP & Deep Learning (LSTM)

## 🚀 Overview

This project focuses on detecting **phishing (spam) emails** using **Natural Language Processing (NLP)** and **Deep Learning (LSTM)**.
The system analyzes email text and classifies it as **Safe Email** or **Phishing Email**.

---

## 🎯 Features

* ✅ Detect phishing emails from text input
* ✅ Batch prediction using CSV file
* ✅ ZIP folder upload (multiple emails)
* ✅ Deep learning model (LSTM) for better accuracy
* ✅ User-friendly interface using Streamlit

---

## 🧠 Technologies Used

* Python
* NLP (Text preprocessing, Tokenization)
* TensorFlow / Keras (LSTM Model)
* Streamlit (Web App)
* Pandas, NumPy

---

## 📂 Project Structure

```
project/
│
├── app.py                 # Streamlit app
├── utils.py               # Prediction function
├── model/
│     ├── model.keras      # Trained LSTM model
│     ├── tokenizer.pkl    # Tokenizer
│     └── config.json      # Max length
│
├── dataset/
│     emails.csv
│
└── README.md
```

---

## 📊 Dataset

* Safe Emails: 11,322
* Phishing Emails: 7,328
* Total Emails: 18,650

---

## ⚙️ Installation

### Step 1: Clone the repository

```bash
git clone <your-repo-link>
cd project
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧪 How to Use

### 🔹 Single Email

* Enter email text
* Click **Check**
* Get prediction (Spam / Safe)

### 🔹 CSV Upload

* Upload CSV file
* Select text column
* Get predictions for all rows

### 🔹 ZIP Upload

* Upload ZIP containing `.txt` emails
* Get predictions for each file

---

## 🧩 Model Architecture

```
Text → Tokenization → Padding → Embedding → LSTM → Dense → Output
```

---

## 📌 Example

Input:

```
Congratulations! You won a free prize.
```

Output:

```
Phishing Email
```

---

## 🎓 Conclusion

This project demonstrates how NLP and deep learning can be used to detect phishing emails effectively.
The system improves email security and reduces manual effort.

---

## 🔮 Future Scope

* Use BERT/Transformers for higher accuracy
* Multilingual phishing detection
* Real-time email filtering system
* Integration with email services

---

## 👨‍💻 Author

* Pardhu
* Mahesh
* Raji Reddy

---

## 📄 License

This project is for academic purposes.
