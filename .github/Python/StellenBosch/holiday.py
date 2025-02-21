# Ask user to input fight destination from list of holiday destinations
# Cast users input to a variable (city_flight)
city_flight = input("""\nPlease select your holiday destination from the options below: 
1. Johannesburg
2. Cape Town
3. Polokwane
4. Durban
\nDestination: """)

# Ask user again to enter the number of nights they'll be staying at the chosen city
# Cast this input to integer and save it as variable (num_nights)
num_nights = int(input(f"\nHow many nights will you be staying at the hotel in {city_flight}: "))

# Ask user again to enter the number of days they'll be renting a car with the rental services
# Cast the input to integer and save as variable (rental_days)
rental_days = int(input("\nHow many days will you be using the car rental services: "))

# Define a new function called hotel_stay() with num_nights as argument
    # Multiply the number of days by 750 (which is the price of staying at the hotel per night)
    # Save this calculation under variable hotel_amount and return result to console
def hotel_stay(num_nights):
    hotel_amount = num_nights * 750
    return hotel_amount

# Define a second function called plane_cost() with the city_flight variable as argument
    # Write an if statement supported by elif statements where if city_flight is equal to known city
    # return price, or else flight_cost is equal to zero(0)
def plane_cost(city_flight):
    if city_flight == "Durban":
        flight_cost = 820
    elif city_flight == "Cape Town":
        flight_cost = 1250
    elif city_flight == "Polokwane":
        flight_cost = 900
    elif city_flight == "Johannesburg":
        flight_cost = 700
    else:
        flight_cost = 0
    return flight_cost

# Define a third function called car_rental() with the rental_days variable as an argument
    # Multiply the number of days by 176 (which is the price of renting a car per day)
    # Save this calculation under variable rental_amount and return result to console
def car_rental(rental_days):
    rental_amount = rental_days * 176
    return rental_amount

# Define the last function names holiday_cost that uses all three inputs as arguments
# ...num_nights, city_flight, and rental_days must all be valid
    # Create 4 variables, 3 for storing each of the functions and their arguments
    # And the forth variable should be the total cost, this variable sums the values of the other 3 variables
    # Finally return the value of total_cost to console
def holiday_cost(num_nights, city_flight, rental_days):
    hotel_cost = hotel_stay(num_nights)
    flight_cost = plane_cost(city_flight)
    rental_cost = car_rental(rental_days)
    total_cost = hotel_cost + flight_cost + rental_cost
    return total_cost

# To print out all the details about the holiday in a way that is easy to read.
# Use the print() function and start writing the functioanal details of the users booking details in the form of strings
# Use the '+' symbol to join the strings with variables containing flight informations
# Cast the functions containing the amounts and totals to integer for extration and display in the print() function
# Use print() function to confirm the booking process with the user
print("\nThe total cost of your holiday is" + " " + str(holiday_cost(num_nights, city_flight, rental_days)) + "," + 
" " + "and your details are as follows: "
"\nFlight Destination:\t" + city_flight +
"\nFlight Cost:\t" + "R" + str(plane_cost(city_flight)) +
"\nNumber of days for hotel booking:\t" + str(num_nights) + " " + "days" +
"\nYour cost for your hotel stay:\t" + "R" +  str(hotel_stay(num_nights)) +
"\nNumber of days for your car rental:\t" + str(rental_days) + " " + "days" +
"\nYour cost for car rental is:\t" + "R" + str(car_rental(rental_days))
)
print("\nThanks for booking with us!\n")