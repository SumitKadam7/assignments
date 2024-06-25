class Movie:
    def __init__(self, name, ticket_price):
        self.name = name
        self.ticket_price = ticket_price
        self.tickets_sold = 0
    
    def sell_tickets(self, quantity):
        if quantity <= 0:
            print("Invalid quantity. Please enter a positive number of tickets.")
            return 0

        self.tickets_sold += quantity
        return quantity * self.ticket_price
    
    def get_name(self):
        return self.name
    
    def get_ticket_price(self):
        return self.ticket_price
    
    def get_tickets_sold(self):
        return self.tickets_sold

def main():

    movies = [
        Movie("Avengers: Endgame", 500),                         
        Movie("Dr. Strange In The Multiverse of Madness", 450),                     
        Movie("Avatar: The Way of Water", 750),
        Movie("Interstellar", 1000)
    ]

    print("Welcome to the movie ticket service!")
    print("Available movies:")
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie.get_name()} - rs{movie.get_ticket_price()} per ticket")
        print()


    while True:
        try:
            choice = int(input("\nEnter the index value of the movie you want to buy tickets for: "))
            if choice < 1 or choice > len(movies):
                print("Invalid choice. Please enter a number within the range.")
                continue

            movie = movies[choice - 1]
            quantity = int(input(f"How many tickets do you want for {movie.get_name()}? "))
            
            total_cost = movie.sell_tickets(quantity)
            print(f"\nYou have purchased {quantity} ticket(s) for {movie.get_name()} for a total of rs{total_cost}.")
            print(f"Total tickets sold for {movie.get_name()}: {movie.get_tickets_sold()}")

            break    
        except ValueError:
            print("Invalid input. Please enter a valid number.")

main()

