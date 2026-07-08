# 🤖 Customer Feedback Analytics

## 📌 Project Overview

Customer Feedback Analytics is an AI-powered web application that analyzes customer reviews using a fine-tuned DistilBERT model. The application predicts whether a review is **Positive**, **Neutral**, or **Negative**, and displays the prediction confidence along with probability scores for all sentiment classes.

The application is built using **Flask** for the backend and provides a modern, responsive user interface with Light/Dark mode support.

---

## ✨ Features

- Fine-tuned DistilBERT model for sentiment analysis
- Predicts Positive, Neutral, and Negative sentiments
- Displays confidence score
- Shows probability distribution for each sentiment
- Responsive web interface
- Dark and Light mode
- Character counter
- Modern and user-friendly UI

---

## 🛠 Technologies Used

- Python
- Flask
- PyTorch
- Hugging Face Transformers
- DistilBERT
- Scikit-learn
- Pandas
- NumPy
- HTML5
- CSS3
- JavaScript

---

## 📂 Project Structure

```text
customer-feedback-analytics/
│
├── app.py
├── requirements.txt
├── README.md
├── models/
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html

```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/ShaikMadiha/customer-feedback-analytics.git
```

### Navigate to the project

```bash
cd customer-feedback-analytics
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000

```
If deployed, replace the local URL above with your live application URL.
---

## 🤖 Model Information

**Model:** Fine-tuned DistilBERT

**Task:** Sentiment Analysis

**Sentiment Classes:**

- Positive
- Neutral
- Negative

---

## 📊 Output

The application provides:

- Predicted sentiment
- Confidence score
- Probability for Positive, Neutral, and Negative classes


---
## 🤖 Model

The fine-tuned DistilBERT model is not included in this repository because the model file exceeds GitHub's 100 MB file size limit.

To run the application, place the trained model in the following directory:

```text
models/distilbert_model/
```

Similarly, the original dataset and intermediate processed datasets are not included in this repository to keep it lightweight.

---


## 👩‍💻 Author

**Shaik Madiha**

GitHub: https://github.com/ShaikMadiha
