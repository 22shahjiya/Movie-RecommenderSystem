import streamlit as st
import pickle
import pandas as pd
import requests


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


OMDB_API_KEY = "e1f84be"

def fetch_poster(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data.get("Response") == "True":
        return data.get("Poster")
    return "https://via.placeholder.com/150?text=No+Image"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(title))
    return recommended_movies, recommended_posters


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations, posters = recommend(selected_movie_name)
    st.write("### 🎥 Top 5 Recommendations:")
    for i in range(len(recommendations)):
        st.image(posters[i], width=150)  
        st.write(recommendations[i])
