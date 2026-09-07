movies = []
ratings = []

def add_movie(movie_name):
    if movie_name in movies:
        return f"Movie '{movie_name}' already exists!"
    
    movies.append(movie_name)
    ratings.append([])  
    return f"Movie '{movie_name}' added!"

def rate_movie(movie_name, rating):
    if movie_name not in movies:
        return f"Movie '{movie_name}' not found!"
    
    if rating < 1 or rating > 5:
        return "Invalid rating! Enter a number from 1 to 5."
    
 
    index = movies.index(movie_name)
    ratings[index].append(rating)
    return f"Rating added for '{movie_name}' {rating}"

def view_average_ratings():
    if len(movies) == 0:
        return "No movies added yet."
    
    output = "Average Ratings:\n"
    for index in range(len(movies)):
        movie_name = movies[index]
        movie_ratings = ratings[index]
        
        if len(movie_ratings) > 0:
            average = sum(movie_ratings) / len(movie_ratings)
            output += f"{movie_name}: {average}\n"
        else:
            output += f"{movie_name}: No ratings yet\n"
            
    return output.strip()


if __name__ == "__main__":
    while True:
        print("\n1. Add a Movie")
        print("2. Rate a Movie")
        print("3. View Average Ratings")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter the movie name: ")
            print(add_movie(name))
            
        elif choice == "2":
            name = input("Enter the movie name: ")
            score = float(input("Enter your rating (1-5): "))
            print(rate_movie(name, score))
            
        elif choice == "3":
            print(view_average_ratings())
            
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
            
        else:
            print("Invalid choice, try again.")
