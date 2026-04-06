# 🎬 Movie Recommendation System

This project is a content-based movie recommendation system built using Python and basic machine learning techniques. It suggests movies similar to a given input movie by analyzing genre information and computing similarity scores.

The system uses the MovieLens (ml-latest-small) dataset, which contains movie titles, genres, and ratings. The genres are preprocessed and converted into numerical format using CountVectorizer, and similarity between movies is calculated using cosine similarity. Based on this, the system recommends the top 5 most similar movies.

### 🚀 Features
- Recommends top 5 similar movies based on input  
- Uses content-based filtering approach  
- Simple, fast, and efficient implementation  
- Works on real-world dataset (MovieLens)  

### 🛠️ Technologies Used
Python, Pandas, NumPy, Scikit-learn  

### ⚙️ How It Works
The project follows these steps:
1. Load the dataset (movies and ratings)  
2. Clean and preprocess the data  
3. Convert genre text into numerical vectors using CountVectorizer  
4. Compute similarity between movies using cosine similarity  
5. Recommend movies with highest similarity scores  

### ▶️ How to Run the Project
1. Clone this repository  

2. Install required libraries:pip install pandas numpy scikit-learn
3. Run the Python file:python main.py
4. Enter a movie name when prompted  

### 💡 Example
Input:
Toy Story (1995)

Output:
Antz (1998)  
Toy Story 2 (1999)  
Monsters, Inc. (2001)  
Adventures of Rocky and Bullwinkle, The (2000)  
Emperor's New Groove, The (2000)  

### 📈 Future Improvements
- Use ratings for collaborative filtering  
- Improve recommendation accuracy  
- Build a web interface using Flask  

### 👩‍💻 Author
Supriya Shelke
