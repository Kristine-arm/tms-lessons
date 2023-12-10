# Define the function to add favorite movie to JSON file
import json
def add_favorite_movie_to_json(movie_title):
    file_path = "file.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    data["favorite_movie"] = movie_title

    with open(file_path, "w") as file:
        json.dump(data, file)

# Call the function and pass your favorite movie title as an argument
favorite_movie_title = "Your Lovely Movie Title"  # Replace this with your favorite movie title
add_favorite_movie_to_json(favorite_movie_title)
