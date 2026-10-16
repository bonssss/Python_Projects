
# 4) Movie Ticket Booking Simulation

# Simulate a movie theater booking system that:Shows a list of available movie titles, showtimes, and seat prices.
# Asks the user to choose a movie and number of tickets.
# Confirms total price and asks if they want to book another movie.
# Ends when they say “no” and displays total bookings and cost.

movies = {
    "Inception": {
        "showtimes": ("10:00 AM", "2:00 PM", "6:00 PM"),  
        "price": 12.0
    },
    "Avatar 2": {
        "showtimes": ("11:00 AM", "3:30 PM", "7:30 PM"),  
        "price": 15.0
    },
    "Toy Story": {
        "showtimes": ("1:00 PM", "4:00 PM"),              
        "price": 9.0
    }
}

def display_movies():
    print("\n--- Available Movies ---")
    #Convert the dictionary into a list for easy numbering
    movie_list = list(movies.keys())
    #to display each movies
    for index, title in enumerate(movie_list, start=1):
        details = movies[title]
        print(f"{index}. {title}")
        print(f"   Showtimes: {', '.join(details['showtimes'])}")
        print(f"   Price per ticket: ${details['price']:.2f}")
 
def main():
    total_bookings = 0
    total_cost = 0.0
    movie_list = list(movies.keys())

    while True:
        display_movies()
        
        # Ask user to choose a movie
        choice = input("\nEnter the number of the movie you want to book: ")
        
        # Validate if input is a digit and within range
        if choice.isdigit():
            choice_num = int(choice)
            
            if 1 <= choice_num <= len(movie_list):
                selected_movie = movie_list[choice_num - 1]
                movie_details = movies[selected_movie]
                
                print(f"\nYou selected: {selected_movie}")
                
                # Validate showtime
                while True:
                    showtime_input = input(f"Enter showtime ({', '.join(movie_details['showtimes'])}): ").strip()
                    
                    matched_showtime = None
                    for st in movie_details['showtimes']:
                        st_clean = st.lower().replace(" ", "")
                        inp_clean = showtime_input.lower().replace(" ", "")
                        hour_part = st.split(":")[0].strip()
                        time_part = st.split()[0].lower()
                        
                        if inp_clean in (st_clean, st.lower(), hour_part.lower(), time_part, f"{hour_part.lower()}pm", f"{hour_part.lower()}am"):
                            matched_showtime = st
                            break

                    # Also allow selecting by showtime index (1, 2, 3...)
                    if not matched_showtime and showtime_input.isdigit():
                        idx = int(showtime_input) - 1
                        if 0 <= idx < len(movie_details['showtimes']):
                            matched_showtime = movie_details['showtimes'][idx]

                    if matched_showtime:
                        showtime = matched_showtime
                        break
                    else:
                        print(f"Error: Invalid showtime. Please choose from: {', '.join(movie_details['showtimes'])}")

                # Ask for number of tickets
                while True:
                    tickets_input = input("Enter number of tickets: ").strip()
                    if tickets_input.isdigit() and int(tickets_input) > 0:
                        num_tickets = int(tickets_input)
                        break
                    else:
                        print("Error: Please enter a valid number of tickets (greater than 0).")
                
                # Calculate price
                cost = num_tickets * movie_details['price']
                
                print(f"\n--- CONFIRMATION ---")
                print(f"Movie: {selected_movie} at {showtime}")
                print(f"Tickets: {num_tickets} x ${movie_details['price']:.2f}")
                print(f"Total Price: ${cost:.2f}")
                
                confirm = input("Confirm booking? (yes/no): ").strip().lower()
                if confirm in ("yes", "y"):
                    total_bookings += num_tickets
                    total_cost += cost
                    print("Booking confirmed successfully!")
                else:
                    print("Booking cancelled.")
            else:
                print("Error: Invalid movie number selected.")
        else:
            print("Error: Please enter a valid digit.")
            
        # Ask if they want to book another movie
        again = input("\nDo you want to book another movie? (yes/no): ").strip().lower()
        if again in ("no", "n"):
            break # Exits the while loop

    # Final Summary
    print("\n=== FINAL BOOKING SUMMARY ===")
    print(f"Total Tickets Booked: {total_bookings}")
    print(f"Total Cost: ${total_cost:.2f}")
    print("Thank you for using the Movie Booking System!")

# Run the program
if __name__ == "__main__":
    main()
