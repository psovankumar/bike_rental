import datetime as dt


# TODO 1 - Create Bike Rental Class and initialize stock attribute
class BikeRental:
    def __init__(self, stock = 0):
        """Initializer for Bike Rental class"""
        self.stock = stock

    # TODO 2 - Create a method to display stock
    def display_stock(self):
        """Displays the bikes currently available for rent in the system"""
        print(f"We have currently {self.stock} bike's available in the system.")
        return self.stock

    # TODO 3 - Create a method to rent bike on hourly basis
    def rent_bike_on_hourly_basis(self, n):
        """Rent bike on hourly basis"""
        if n <= 0:
            print("The number of bike's should be a positive number.")
            return None
        elif n > self.stock:
            print(f"Sorry! We have only {self.stock} bike's available to rent.")
            return None
        else:
            now = dt.datetime.now()
            print(f"You have rented {n} bikes on hourly basis today at {now.hour}:{now.minute}:{now.minute}\n"
                  f"You will be charged $5 for each bike an hour\n"
                  f"We hope that you enjoy our service and have a safe ride.")
            self.stock -= n
            return now

    # TODO 4 - Create a method to rent bike on daily basis
    def rent_bike_on_daily_basis(self, n):
        """Rent bike on daily basis"""
        if n <= 0:
            print("The number of bike's should be a positive number.")
            return None
        elif n > self.stock:
            print(f"Sorry! We have only {self.stock} bike's available to rent.")
            return None
        else:
            now = dt.datetime.today()
            print(f"You have rented {n} bikes on daily basis today on {now}\n"
                  f"You will be charged $20 for each bike daily\n"
                  f"We hope that you enjoy our service and have a safe ride.")
            self.stock -= n
            return now

    # TODO 5 - Create a method to rent bike on weekly basis
    def rent_bike_on_weekly_basis(self, n):
        """Rent bike on weekly basis"""
        if n <= 0:
            print("The number of bike's should be a positive number only.")
            return None
        elif n > self.stock:
            print(f"Sorry! We have only {self.stock} bike's available to rent.")
            return None
        else:
            now = dt.datetime.today()
            print(f"You have rented {n} bikes on weekly basis today on {now}\n"
                  f"You will be charged $60 for each bike weekly\n"
                  f"We hope that you enjoy our service and have a safe ride.")
            self.stock -= n
            return now

    # TODO 6 - Create a method to return bike from the system
    def return_bike(self, request):
        """Accept a bike returned from the customer, increases the number of bikes and returns a bill"""
        return_time, return_basis, num_bikes = request
        bill = 0
        if return_time and return_basis and num_bikes:
            self.stock += num_bikes
            now = dt.datetime.now()
            return_period = now - return_time
            # hourly basis
            if return_basis == 1:
                bill = round(return_period.seconds / 3600) * 5 * num_bikes
            # daily bill calculation
            elif return_basis == 2:
                bill = return_period.days * 20 * num_bikes
            # weekly basis calculation
            elif return_basis == 3:
                bill = round(return_period.days / 7) * 60 * num_bikes
            if 3 <= num_bikes <= 6:
                print("You are eligible for family rental promotion which is 30%")
                bill = bill * 0.7
                print("Thanks for returning the bike. Hope you have enjoyed our service!")
                print(f"Your total bill is {bill}")
        else:
            print("Not correct credentials")
            return None


# TODO 7 - Create Customer Class and initialize attributes
class Customer:
    """Initializer for Customer class"""
    def __init__(self):
        self.bikes = 0
        self.rental_basis = 0
        self.rental_time = 0
        self.bill = 0

    # TODO 8 - Create a method to request bike from the system
    def request_bike(self):
        """Takes a request from customer for number of bikes"""
        bikes = input("Enter the number of bikes you would like to rent:")
        try:
            bikes = int(bikes)
        except ValueError:
            print("Invalid input: The number of bikes should be a positive integer!")
            return -1
        if bikes < 1:
            print("Invalid input: The number of bikes should be a positive integer!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    # TODO 9 - Create a method to return bike to the system
    def return_bike(self):
        """Allows customers to return their bikes to the rental shop"""
        if self.rental_time and self.rental_basis and self.bikes:
            return self.rental_time, self.rental_basis, self.bikes
        else:
            return 0, 0, 0







