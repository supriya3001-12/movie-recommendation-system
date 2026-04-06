# 🎬 Movie Recommendation System

## 📌 Overview
This project is a **Content-Based Movie Recommendation System** built using Python and Machine Learning.  
It recommends movies based on similarity in genres using cosine similarity.

---

## 🚀 Features
- Recommend movies based on selected movie
- Uses content-based filtering approach
- Fast and simple recommendation logic
- Clean and easy-to-understand implementation

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn

---

## 📂 Dataset
- MovieLens Latest Small Dataset
- Contains movie titles, genres, and ratings

---

## ⚙️ How It Works
1. Load movie dataset
2. Clean and preprocess data
3. Convert genres into numerical vectors using **CountVectorizer**
4. Calculate similarity using **Cosine Similarity**
5. Recommend top 5 similar movies

---

## ▶️ How to Run
1. Clone this repository
2. Install required libraries:
   ```bash
   pip install pandas numpy scikit-learn
