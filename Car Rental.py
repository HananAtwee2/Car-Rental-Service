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
        self.__rental_price_per_day = rental_price_per_day

    #display function
    def display_info(self):
        print()