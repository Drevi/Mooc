# Write your solution here

def find_movies(database: list, search_term: str):
    filtered_list = []
    for movie in database:
        if search_term.lower() in movie["name"].lower():
            filtered_list.append(movie)
    return filtered_list
