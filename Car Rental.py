class Vehicle:
    brand=" "
    model=" "
    year=0
    rental_price_per_day=0
    
    #Constructor
    def __init__(self, brand,model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day #private

    #display function
    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.get__rental_price()}/day")

    def calculate_rental_cost(self,days):
        return self.get_rental_price() * days

    #getter
    def get_rental_price(self):
        return self.__rental_price_per_day

    #setter
    def set_rental_price(self,new_price):
        if new_price > 0:
            self.__rental_price_per_day = new_price
        else:
            print("Price must be positive.")


#new class (inherits from Vehicle)            
class Car(Vehicle):

    #constructor
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity
    
    #display method overrided
    def display_info(self):
        """overrides diplay_info to include capacity"""
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.get_rental_price()}/day")

#new derived class(bike inherited from Vehicle)    
class Bike(Vehicle):
    #constructor
    def __init__(self,brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity= engine_capacity
    #override
    def display_info(self):
        """display method updated with engine capacity"""
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price: ${self.get_rental_price()}/day")

def show_vehicle_info(vehicle):
    vehicle.display_info()

#create objects
car1=Car("Toyota","Corolla",2020,50,5)
bike1=Bike("Yamaha","R1",2019,30,998)

#display their details
show_vehicle_info(car1)
show_vehicle_info(bike1)

# Calculate rental costs
print(f"Rental cost for {car1.brand} {car1.model} for 3 days: {car1.calculate_rental_cost(3)} $")
print(f"Rental cost for {bike1.brand} {bike1.model} for 5 days: {bike1.calculate_rental_cost(5)} $")

#Calculate updated rental price 


