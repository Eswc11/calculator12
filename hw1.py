import json
import os
def read_file():
    if os.path.exists('movies.json'):
        with open('movies.json') as f:
            movies = json.load(f)
            return movies
    else:
        return []
movies = read_file()
def write_file():
    with open('movies.json', 'w') as f:
        json.dump(movies, f)
def get_movie(name):
    for movie in movies:
        if movie["name"].capitalize() == name:
            return movie
def add_movie():
    new_movie = input('Enter movie name: ')
    movie = get_movie(new_movie)
    if movie not in movies:
        new_movie = {
            "name": new_movie,
            "rating": {}
        }
        movies.append(new_movie)
        write_file()
        print("Movie added")
def list_movie():
    for movie in movies:
        print(f"{movie['name'].capitalize()}:{' '*10} {movie['ratings']}")
def rate_movie():
    name_user = input('Enter username: ').capitalize()
    rate_user = int(input('Enter rating: '))
    movie_name = input('Enter movie name: ').capitalize()
    movie = get_movie(movie_name)
    if movie in movies:
        if rate_user > 0 and rate_user <= 10:
            ratings = movie['ratings']
            ratings[name_user] = rate_user
            write_file()
            print("Rating added")
        elif rate_user == 0:
            if name_user in movie['ratings']:
                del movie['ratings'][name_user]
                write_file()
                print("Rating removed")
            else:
                print("Movie not rated")
        else:
            print("Enter from 0 to 10")
    else:
        print("Does not exist")
def find_movie():
    movie = input('Enter movie name: ')
    a = get_movie(movie)
    if a in movies:
        print(f'{movie} find.')
    else:
        print(f'{movie} not found.')
def delete_movie():
    movie = input('Enter movie name: ')
    a = get_movie(movie)
    if a in movies:
        movies.remove(a)
        write_file()
        print(f"{movie} deleted")
    elif a not in movies:
        print(f"{movie} not found.")
commands = ["add", "delete", "list", "rate", "find", "exit"]
def main():
    for command in commands:
        print(command)
    while True:
        a = input("Enter command: ")
        if a == "add":
            add_movie()
        elif a == "list":
            list_movie()
        elif a == "rate":
            rate_movie()
        elif a == "find":
            find_movie()
        elif a == "exit":
            exit()
        else:
            print("Invalid command")
main()

first = [1,1,2,3,5,8,13,21,34,55,89]
