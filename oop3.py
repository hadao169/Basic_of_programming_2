class Product:
    def __init__(self, name: str, price: float, product_id: int):
        self.__name = name  # Add dounle underscore before a variable or a method => encapsulation in OOP of python => made these variables private to the class
        self.__price = price
        self.__product_id = product_id
	
    def getPrice(self):
        return self.__price
    
    def setPrice(self, new_price):
        if new_price > 0.1 and new_price >= self.__price * 0.9:
            self.__price = new_price
    
    def __str__(self):
        return f"Product(name: {self.__name}, price: {self.__price}, product_id: {self.__product_id})"
  
def main():
    product_list = []
    
    # Example products with unique product IDs
    p1 = Product("Screw", 0.8, 1001)
    p2 = Product("Nut", 1.2, 1002)
    p3 = Product("Nail", 0.5, 1003)
  
    product_list.append(p1)
    product_list.append(p2)
    product_list.append(p3)
  
    # Print the list of products
    print("Product list:")
    for product in product_list:
        print(product)
  
if __name__ == "__main__":
    main()
