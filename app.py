import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{'
                            '}?api_key=cc31facc2e000af2483bb0d562d5b7df&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/1E5baAaEse26fej7uHcjOgEE2t2.jpg" + data['poster_path']



def recommendation(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendation_movies = []
    recommendation_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].title
        recommendation_movies.append(movies.iloc[i[0]].title)
        recommendation_movies_posters.append(fetch_poster(movie_id))
        return recommendation_movies, recommendation_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movie Recommendation System')


selected_movie_name = st.selectbox(
    'Which movie would you like recommendations for?',
    movies['title'].values
)

if st.button('Get Recommendation'):
    names, posters = recommendation(selected_movie_name)

    for i in recommendation:
        names,posters = recommendation(selected_movie_name)

        col1, col2, col3, col4, col5 = st.beta_columns(5)
        with col1:
            st.text(names[0])
            st.image(posters[0])
        with col2:
            st.text(names[1])
            st.image(posters[1])
        with col3:
            st.text(names[2])
            st.image(posters[2])
        with col4:
            st.text(names[3])
            st.image(posters[3])
        with col5:
            st.text(names[4])
            st.image(posters[4])
