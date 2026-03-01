# Movie Database Management System (MDMS) Dictionary 
# This module provides a dictionary of MDMS (Master Data Management System) related terms and their definitions.    

# Create a mdms_dic.py file to store the mdms dictionary

import json

movies = {
    "Ye Wondoch Guday": {
        "year": 2007,
        "genre": "Romantic Comedy",
        "director": "Henok Ayele",
        "actors": ["Admassu Kebede", "Rekik Teshome", "Shewit Kebede"]
    },
    "Teza": {
        "year": 2008,
        "genre": "Drama",
        "director": "Haile Gerima",
        "actors": ["Aaron Arefe", "Abiye Tedla", "Takelech Beyene"]
    },
    "Lambadina": {
        "year": 2015,
        "genre": "Drama",
        "director": "Messay Getahun",
        "actors": ["Rediat Amare", "Selam Tesfaye", "Yohannes Messele"]
    },
}

# Print out the movies and their information using square brackets syntax and .keys() and .values() methods
for movie in movies.keys():
        print(f"Movie: {movie}")
        for key, value in movies[movie].items():
            print(f"{key}: {value}")
        print() 

# Update an element in the dictionary
movies["Teza"]["year"] = 2009

# Delete an element from the dictionary
del movies["Lambadina"] 

# Get a value from the dictionary using the .get() 
genre = movies["Ye Wondoch Guday"].get("genre")
print(f"The genre of 'Ye Wondoch Guday' is: {genre}")   

# Requirement 

#Add a new movie to the dictionary
movies["Sost Maezen"] = {
    "year": 2010,
    "genre": "Drama",
    "director": "Messa Alemu",
    "actors": ["Mekdes Alemu", "Tigist Alemu", "Yohannes Alemu"]
}   
print("Added Sost Maezen to the movie database")

# Edit a movie's information in the dictionary
movies["Sost Maezen"]["director"] = "Messae"
print("Updated the director of Sost Maezen")    

#Delete a movie from the dictionary
del movies["Sost Maezen"]
print("Deleted Sost Maezen from the movie database")    

# View all movies in the dictionary
print("Current movies in the database:")
for movie in movies:
    print(movie)

# Search movies by title, genre, or director, release date, or actors
search_title = "Teza"
search_genre = "Drama"  
search_director = "Haile Gerima"
print(f"Searching for movies with title '{search_title}':")
for movie in movies:
    if search_title.lower() in movie:
        print(movie)
print(f"Searching for movies with genre '{search_genre}':")
for movie in movies:
    if movies[movie]["genre"] == search_genre:
        print(movie)    

print(f"Searching for movies directed by '{search_director}':")
for movie in movies:
    if movies[movie]["director"] == search_director:
        print(movie)    

# Save and load data to and from a file
# import json is already done at the top of the file

# Save the movies dictionary to a JSON file

with open("movies.json", "w") as f:
    json.dump(movies, f, indent=4) 

# Load the movies dictionary from a JSON file
with open("movies.json", "r") as f:
    loaded_movies = json.load(f)    
print("Loaded movies from file:")
for movie in loaded_movies:
    print(movie)    
    for key, value in loaded_movies[movie].items():
        print(f"{key}: {value}")    

# Use interface to interact with the movie database
def display_menu():
        print("Movie DB Management System") 
        print("1. View all movies")
        print("2. Add a new movie")
        print("3. Edit a movie's information")
        print("4. Delete a movie")
        print("5. Search for movies")
        print("6. Save movies to file")
        print("7. Load movies from file")
        print("8. Exit")    

def main():
    while True:
        display_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            print("All movies:")
            for movie in movies:
                print(movie)
        elif choice == "2":
            title = input("Title: ").strip()
            try:
                year = int(input("Year: ").strip())
            except ValueError:
                print("Invalid year.")
                continue
            genre = input("Genre: ").strip()
            director = input("Director: ").strip()
            actors = input("Actors (comma separated): ").split(",")
            actors = [a.strip() for a in actors if a.strip()]
            movies[title] = {"year": year, "genre": genre, "director": director, "actors": actors}
            print(f"Added {title}.")
        elif choice == "3":
            title = input("Title to edit: ").strip()
            if title in movies:
                field = input("Field to edit (year/genre/director/actors): ").strip()
                if field == "year":
                    try:
                        movies[title]["year"] = int(input("New year: ").strip())
                    except ValueError:
                        print("Invalid year.")
                elif field == "actors":
                    actors = input("Actors (comma separated): ").split(",")
                    movies[title]["actors"] = [a.strip() for a in actors if a.strip()]
                elif field in ("genre", "director"):
                    movies[title][field] = input(f"New {field}: ").strip()
                else:
                    print("Unknown field.")
                print("Updated.")
            else:
                print("Movie not found.")
        elif choice == "4":
            title = input("Title to delete: ").strip()
            if title in movies:
                del movies[title]
                print("Deleted.")
            else:
                print("Movie not found.")
        elif choice == "5":
            q = input("Search term (title/genre/director/actor): ").strip().lower()
            for movie in movies:
                info = movies[movie]
                if (q in movie.lower()
                        or q in str(info.get("year", "")).lower()
                        or q in info.get("genre", "").lower()
                        or q in info.get("director", "").lower()
                        or any(q in actor.lower() for actor in info.get("actors", []))):
                    print(movie)
        elif choice == "6":
            with open("movies.json", "w") as f:
                json.dump(movies, f, indent=4)
            print("Saved.")
        elif choice == "7":
            try:
                with open("movies.json", "r") as f:
                    loaded = json.load(f)
                movies.clear()
                movies.update(loaded)
                print("Loaded.")
            except FileNotFoundError:
                print("movies.json not found.")
        elif choice == "8":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")


# if __name__ == "__main__":
#     main()  


# Error handling and edge cases are included in the code, such as 
# handling invalid input for year and checking if a movie exists before 
# editing or deleting. The search functionality allows searching by title, genre, director, or actors. 
# The data is saved and loaded using JSON format for easy readability.
#The program should handle any input errors gracefully, d
# displaying appropriate messages to the user if any invalid input is entered. 
# The search functionality allows users to find movies based on various criteria, 
# and the save/load functionality ensures that the movie database can be persisted across sessions.  

import json
import os
import sys

try:
    # ---- MENU INPUT VALIDATION ----
    choice = input("Enter choice (1-8): ").strip()
    if choice not in ["1","2","3","4","5","6","7","8"]:
        print("Invalid choice. Please enter 1-8.")

    # ---- YEAR VALIDATION ----
    try:
        year = int(input("Year: ").strip())
        if year < 1800 or year > 2100:
            print("Year must be between 1800 and 2100.")
    except ValueError:
        print("Invalid year. Year Must be a number.")

    # ---- EMPTY INPUT VALIDATION ----
    title = input("Title: ").strip()
    if not title:
        print("Title field cannot be empty.")

    # ---- MOVIE EXISTENCE CHECK ----
    if title not in movies:
        print("Movie not found.")

    # ---- FILE SAVE ERROR HANDLING ----
    try:
        with open("movies.json", "w") as f:
            json.dump(movies, f, indent=4)
        print("Movies saved successfully.")
    except IOError:
        print("Error saving file.")

    # ---- FILE LOAD ERROR HANDLING ----
    if not os.path.exists("movies.json"):
        print("File does not exist.")
    else:
        try:
            with open("movies.json", "r") as f:
                loaded_movies = json.load(f)
            if isinstance(loaded_movies, dict):
                movies.clear()
                movies.update(loaded_movies)
                print("Movies loaded successfully.")
            else:
                print("Invalid file format.")
        except FileNotFoundError:
            print("movies.json not found.")
        except json.JSONDecodeError:
            print("File is corrupted or not valid JSON.")
        except Exception as e:
            print("Error loading file:", e)

except Exception as e:
    print("Unexpected error occurred:", e)

# Data validation is implemented for menu choices, year input, and empty fields.
# The program checks if the movie exists before editing or deleting, and it handles file I/O errors gracefully, providing feedback to the user in case of issues.       
# -------- DATA VALIDATION SECTION -------- #

# Validate menu choice
if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
    print("Invalid choice. Please enter a number between 1 and 8.")
    sys.exit(1)


# -------- TITLE VALIDATION -------- #
title = input("Title: ").strip()

if not title:
    print("Error: Title cannot be empty.")
    sys.exit(1)

if title in movies:
    print("Error: Movie already exists.")
    sys.exit(1)


# -------- YEAR VALIDATION -------- #
try:
    year = int(input("Year: ").strip())
except ValueError:
    print("Error: Year must be a number.")
    sys.exit(1)

if year < 1888 or year > 2100:
    print("Error: Year must be between 1888 and 2100.")
    sys.exit(1)


# -------- GENRE VALIDATION -------- #
genre = input("Genre: ").strip()

if not genre:
    print("Error: Genre cannot be empty.")
    sys.exit(1)


# -------- DIRECTOR VALIDATION -------- #
director = input("Director: ").strip()

if not director:
    print("Error: Director cannot be empty.")
    sys.exit(1)


# -------- ACTORS VALIDATION -------- #
actors_input = input("Actors (comma separated): ").strip()

if not actors_input:
    print("Error: Actors cannot be empty.")
    sys.exit(1)

actors = [a.strip() for a in actors_input.split(",") if a.strip()]

if not actors:
    print("Error: At least one actor is required.")
    sys.exit(1)


# -------- EDIT FIELD VALIDATION -------- #
field = input("Field (year/genre/director/actors): ").strip().lower()

if field not in ["year", "genre", "director", "actors"]:
    print("Error: Invalid field selection.")
    sys.exit(1)


# -------- SEARCH VALIDATION -------- #
query = input("Enter search term: ").strip().lower()

if not query:
    print("Error: Search term cannot be empty.")
    sys.exit(1)