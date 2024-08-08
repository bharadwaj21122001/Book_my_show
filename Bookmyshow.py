import json
import math
bookings = []
seats = []
def initialize_movies():
    movies = []
    f = open("C:/Users/acer/OneDrive/Desktop/CSPP/bookmyshow.json")
    data = json.load(f)
    for i in data:
        movies.append(i)
    # print(len(movies))
    return movies
# initialize_movies()
def roundof(n):
    m = n % 10
    seat = n + (10-m)
    return seat

def initialize_seating(movies, movieIndex):
    seat = movies[movieIndex]["seats"]
    seats = roundof(seat) #No of maximum capacity
    rows = math.ceil(seats/10) # I have taken 10 seats per each row as constant
    # print(rows)
    available_seats = []

    for i in range(rows):
        r = []
        for j in range(10):
            r.append(0)
        available_seats.append(r)
    return available_seats

def display_movies(movies):
    movie_list = []
    for i in range(len(movies)):
        movie_list.append(movies[i]["title"])
    for i in range(len(movie_list)):
        movie_list[i] = str(movie_list[i]).replace('[', '').replace(']', '').replace(',', '')
        print(f"{i}. {movie_list[i]}")
    print('')
    return movie_list

# movies = initialize_movies()
# print(display_movies(movies))

def display_seating(seating):
    # seating = initialize_seating(movies, movieIndex)
    for i in seating:
        i = str(i).replace('[', '').replace(']', '').replace(',', '')
        print(i)
    print('')
    available = 0
    booked = 0
    for i in seating:
        for j in i:
            if j == 0:
                available += 1
            else:
                booked += 1
    print(f"Available seats are = {available}")
    print(f"Booked seats are = {booked}")

# movies = initialize_movies()
# display_seating(movies, 1)

def book_seat(movies, seating, movie_index):
    # movie_index = int(input("Enter the movie index = "))
    row = int(input("Enter the row of the seat = "))
    col = int(input("Enter the column of the seat = "))
    if movie_index <= len(movies):
        if row <= len(seating) and col <= len(seating[row]):
            if seating[row][col] != 'B':
                seating[row][col] = 'B'
            else:
                seating[row][col] = 0
        bookings.append(movie_index)
    seats.append([row, col])
    # print(seats)
    for i in seating:
        i = str(i).replace('[', '').replace(']', '').replace(',', '')
        print(i)
    print('')
    return seating

# book_seat(movies)

def view_booking(movies, bookings, seats):
    for i in bookings:
        if i <= len(movies):
            movie = movies[i]["title"]
            print(f"The movie name is {movie}")
    for i in seats:
        seat = i
        print(f"Seat number = {seat}")
    return movie, seat

def main():
    print("Welcome! to book my show")
    movies = initialize_movies()
    movie = display_movies(movies)
    movie_index = int(input("Enter the movie index = "))
    seating = initialize_seating(movies, movie_index)
    while True:
        print('b. Check seat availability')
        print('c. Book a seat')
        print('d. View bookings')
        print('e. Exit')
        choose = input("Enter your choice = ")

        if choose == 'a':
            movie = display_movies(movies)
            print(movie)
        elif choose == 'b':
            display_seating(seating)
        elif choose == 'c':
            # movie_index = int(input("Enter the movie index = "))
            # seating = initialize_seating(movies, movie_index)
            book_seat(movies, seating, movie_index)
        elif choose == 'd':
            view_booking(movies, bookings, seats)
        elif choose == 'e':
            break

main()