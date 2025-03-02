class Vehicle:
    brand=" "
    model=" "
    year=0
    rental_price_per_day=0
    
    #Constructor
    def _init_(self, brand,model, year, rental_price_per_day):
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