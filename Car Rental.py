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
        print()

    def calculate_rental_cost(self,days):
        return self.rental_price_per_day * days

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
        print()

#new derived class(bike inherited from Vehicle)    
class Bike(Vehicle):
    #constructor
    def __init__(self,brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity= engine_capacity
    #override
    def display_info(self):
        """display method updated with engine capacity"""
        print()

def show_vehicle_info(vehicle):
    vehicle.display_info()
    