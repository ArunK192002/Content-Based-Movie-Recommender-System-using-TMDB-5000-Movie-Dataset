import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    else:
        full_path = "https://via.placeholder.com/500x750?text=No+Image"
    return full_path

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies_df.iloc[i[0]].movie_id  # Assuming 'movie_id' is in the DataFrame
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_posters

st.title('Movie Recommender System')

# Load movies list
movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie_name = st.selectbox('Select a movie', movies_list)

if st.button('Recommend'):
    recommended_movies, recommended_posters = recommend(selected_movie_name)
    
    cols = st.columns(5)  # Create 5 columns
    for col, movie, poster in zip(cols, recommended_movies, recommended_posters):
        with col:
            st.image(poster, width=100)
            st.write(movie)
