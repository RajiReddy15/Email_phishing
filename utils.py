import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from config import MAX_LEN

model = load_model("email_lstm_model.h5")
tokenizer = pickle.load(open("tokenizer.pkl","rb"))

def predict_phishing(text):

    seq = tokenizer.texts_to_sequences([text])
    pad = pad_sequences(seq, maxlen=MAX_LEN, padding="post")

    pred = model.predict(pad)[0][0]

    if pred > 0.5:
        return f"⚠️ Phishing ({pred:.2f})"
    else:
        return f"✅ Safe ({pred:.2f})"