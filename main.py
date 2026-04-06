import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# STEP 1: Load Data
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# STEP 2: Basic Info (Optional but good for understanding)
print("Movies Data:")
print(movies.head())

# STEP 3: Data Cleaning
movies.dropna(inplace=True)
movies.drop_duplicates(inplace=True)

# STEP 4: Feature Engineering (Clean genres)
movies['genres'] = movies['genres'].str.replace('|', ' ')

# STEP 5: Convert text to vectors
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['genres']).toarray()

# STEP 6: Cosine Similarity
similarity = cosine_similarity(vectors)

# STEP 7: Recommendation Function
def recommend(movie):
    if movie not in movies['title'].values:
        print("Movie not found in database ❌")
        return

    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    print(f"\nRecommendations for '{movie}':\n")
    for i in movie_list:
        print(movies.iloc[i[0]].title)

# STEP 8: Test the system
recommend("Toy Story (1995)")
recommend("Jumanji (1995)")
recommend("Grumpier Old Men (1995)")
recommend("Waiting to Exhale (1995)")
movie_name = input("Enter movie name: ")
recommend(movie_name)