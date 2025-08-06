
# 🤖 MoodMate: An AI-Powered Sentiment Companion

MoodMate is a lightweight, interactive sentiment analysis chatbot designed to detect a user's emotional tone and respond with motivational or mood-boosting messages. Built using Hugging Face's `transformers` library and deployed via Gradio, it aims to offer emotional support through simple conversations.

---

## 📌 Features

- 🔍 Real-time sentiment analysis (Positive or Negative)
- 💬 Auto-suggests encouraging replies based on mood
- 🌐 Web interface powered by Gradio
- 🧠 Uses pre-trained transformer model from Hugging Face
- 📁 Custom dataset of motivational messages (CSV-based)

---

## 🧱 Tech Stack

- Python 3.8+
- [Transformers (Hugging Face)](https://huggingface.co/docs/transformers)
- [Gradio](https://gradio.app/)
- CSV, random, collections modules

---

## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have Python 3.8+ installed. Install the required libraries:

```bash
pip install transformers gradio
```

### 📁 Project Structure

```
MoodMate/
│
├── custom_sentiment.csv       # CSV file with motivational messages
├── app.py                     # Main Python file for chatbot
├── README.md                  # Project documentation
```

### ▶️ Running the App

```bash
python app.py
```

This will launch the Gradio web interface locally.

---

## 📂 Dataset Format (`custom_sentiment.csv`)

The CSV file should have the following format:

| label    | text                       |
|----------|----------------------------|
| POSITIVE | Keep up the great work!    |
| NEGATIVE | Don't worry, better days are coming. |

Labels should be in **UPPERCASE**: `POSITIVE`, `NEGATIVE`.

---

## 📸 Screenshots

> *(Insert screenshots of the chatbot UI and example predictions here if needed)*

---

## 🧠 Model Info

The project uses Hugging Face's `pipeline("sentiment-analysis")`, which by default loads:

- **Model:** `distilbert-base-uncased-finetuned-sst-2-english`
- **Type:** Binary sentiment classifier (Positive/Negative)

---

## 🎯 Purpose

This project was developed as a capstone submission to demonstrate practical applications of NLP in offering emotional support and building empathetic AI systems.

---

## 📈 Future Improvements

- Support for multi-class sentiment (Neutral, Mixed, etc.)
- More human-like conversation with dialogue management
- Voice-based interaction
- Multilingual support

---

## 🔗 Links

- 💻 GitHub Repo: [https://github.com/Shashwat970/Moodmate](https://github.com/Shashwat970/Moodmate)  
- 🚀 Live Demo (Hugging Face): [https://huggingface.co/spaces/shake97/moodmate](https://huggingface.co/spaces/shake97/moodmate)

---

## 🙋‍♂️ Author

**Shashwat Srivastava**  
📧 ss6545@srmist.edu.in  
🎓 BCA Student, SRM University

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
