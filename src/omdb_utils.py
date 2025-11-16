import requests

def get_movie_details(title, api_key):

    url = f"http://www.omdbapi.com/?t={title}&plot=full&apikey={api_key}"
    response = requests.get(url).json()# make request with the title that user enters
    if response.get("Response") == "True":
        result = response.get("Plot", "N/A"), response.get("Poster", "N/A")# extract Plot and Poster
        plot = result[0]
        poster = result[1]
        return plot, poster

    return "N/A", "N/A"