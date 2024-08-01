from colorama import Fore

logo = """
 ██████╗ ██████╗  ██████╗  ██████╗███████╗██████╗ ██╗   ██╗██╗  ██╗ █████╗ ██╗     ██╗     
██╔════╝ ██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██║  ██║██╔══██╗██║     ██║     
██║  ███╗██████╔╝██║   ██║██║     █████╗  ██████╔╝ ╚████╔╝ ███████║███████║██║     ██║     
██║   ██║██╔══██╗██║   ██║██║     ██╔══╝  ██╔══██╗  ╚██╔╝  ╚════██║██╔══██║██║     ██║     
╚██████╔╝██║  ██║╚██████╔╝╚██████╗███████╗██║  ██║   ██║        ██║██║  ██║███████╗███████╗
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚══════╝╚═╝  ╚═╝   ╚═╝        ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
  by Özkan Aytuğ Gözaçan                                                                                          
 """

class Product:
    """Class to represent a product:
       Via this class the object "Product" will be created with attributes of ID, name, quantity, purchasing price and selling price.
       ID is necessery to identify the product numerically.
       Name is necessary to identify the product qualitatively.
       Quantity is necesseaty to track how many product is object to related function. 
       Purchasing price is necessary to identify the cost of the product.
       Selling price is necessary to identify the revenue from the product in case of it is sold. 
    """

    """
    Following __init__ function has been used to set the product with mentioned attributes.
    """
    def __init__(self, id, name, quantity, purchasing_price, selling_price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.purchasing_price = purchasing_price
        self.selling_price = selling_price

    """
    Following __str__ function has been used to create a line of string to make understandtable statement on attributes of the product when it is called.
    """
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Quantity: {self.quantity}, Purchasing Price: {self.purchasing_price}, Selling Price: {self.selling_price}"
    
    """
    Following two funtions are "Getter" and "Setter" functions of the attribute ID.
    They have been designed for ensure all product have an ID and all the IDs are intergers.
    """
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if not id:
            raise ValueError("All products must have an ID!")
        if type(id) is not int:
            raise TypeError("ID has to be an integer!")
        self._id = id
    

    """
    Following two funtions are "Getter" and "Setter" functions of quantity attribute.
    They have been designed for set a default value of 0 to products which has no quantity attributes, and ensure all quantity values are integers.
    """
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity is None:
            quantity = 0
        if type(quantity) is not int:
            raise TypeError("Quantity has to be an integer!")
        self._quantity = quantity

    """
    Following two funtions are "Getter" and "Setter" functions of purchasing price attribute.
    They have been designed for ensure all product have an purchasing price and all the purchasing prices are floats.
    """
    @property
    def purchasing_price(self):
        return self._purchasing_price

    @purchasing_price.setter
    def purchasing_price(self, purchasing_price):
        if purchasing_price is None:
            raise ValueError("Purchasing price must be stated!")
        if type(purchasing_price) is not float:
            raise TypeError("Purchasing price has to be a float!")
        self._purchasing_price = purchasing_price

    """
    Following two funtions are "Getter" and "Setter" functions of selling price attribute.
    They have been designed for ensure all product have an selling price and all the selling prices are floats.
    """
    @property
    def selling_price(self):
        return self._selling_price

    @selling_price.setter
    def selling_price(self, selling_price):
        if selling_price is None:
            raise ValueError("Selling price must be stated!")
        if type(selling_price) is not float:
            raise TypeError("Selling price has to be a float!")
        self._selling_price = selling_price



class InventorySystem:
    """Class to manage inventory and transactions:
         Via this class the inventory system has been created as an object with the attributes of inventory, transactions, revenue and costs. 
         - Inventory is an list which will consist existing Product objects which has ben defined above.
         - Transactions attribute is also a list to keep track of the what have be done.
         - Revenue is a numerical value to keep track of how much is earned from selling product. 
         - Costs is a numerical value to keep track of how much is spent from buying product.

         Also, via class functions the program has been enable to make transaction in the inventory.
         - The function add_product: Adds a new product to inventory.
         - The function restock_product: Restocks an existing product in inventory.
         - The function sell_product: Sells a product from inventory.
         - The function show_inventory: Displays current inventory sorted by ID in ascending order.
         - The function show_transactions: Displays last transactions.
         - The function calculate_total: Calculate total revenue, costs, profit, or value of inventory.
    """

    """
    Following __init__ function has been used to set the inventory system with mentioned attributes.
    """
    def __init__(self):
        self.inventory = []
        self.transactions = []
        self.revenue = 0
        self.costs = 0

    def add_product(self, product):
        """ Add a new product to inventory.

            Parameters:
            - product (Product): The product object to be added to the inventory.

            How it works:
            - This function adds a new product to the inventory.
            - It takes a product object as input.
            - First, it checks if the product ID is already in use in the inventory.
            - If the ID is not already in use, the product is appended to the inventory list.
            - It then adds a transaction to the transactions list indicating the addition of the new product.
            - The total costs are updated by adding the cost of the new product (purchasing price * quantity) to the existing costs.
            - Prints a message to make visible the outcome of the funtion to the user.
            - If the ID is already in use, it prints a message indicating that a unique ID should be used. """
        
        # Check if the product ID is already in use
        if any(item.id == product.id for item in self.inventory):
            print("Product ID already exists. Please use a unique ID.")
            return
       
        # Add the product to the inventory if the ID is unique
        self.inventory.append(product)
        self.transactions.append(f"Added {product.quantity} {product.name}(s) to inventory.")
        self.costs += product.quantity * product.purchasing_price
        print(f"Added {product.quantity} {product.name}(s) to inventory. (id number: {product.id})" )

    def restock_product(self, product_id, quantity):
        """Restock an existing product in inventory     
        Parameters:
        - product_id (int): The ID of the product to restock.
        - quantity (int): The quantity of the product to add to the inventory."""

        """ Following for loop works as:
            - The function takes two parameters: product_id and quantity.
            - It searches for the product with the given product_id in the inventory.
            - If the product is found, the quantity of the product in the inventory is increased by the given quantity.
            - The function adds a transaction indicating the restocking action to the transactions list.
            - It updates the total costs by adding the cost of restocking the product (purchasing price * quantity).
            - Prints a message to make visible the outcome of the funtion to the user.
            - If the product is not found in the inventory, a message is printed indicating that the product was not found."""
        for product in self.inventory:
            if product.id == product_id:
                product.quantity += quantity
                self.transactions.append(f"Restocked {quantity} {product.name}(s) in inventory.")
                self.costs += quantity * product.purchasing_price
                print(f"Restocked {quantity} {product.name}(s) in inventory. (id number: {product_id})")
                return
        print("Product not found in inventory.")

    def sell_product(self, product_id, quantity):
        """
         Sell a product from inventory.

          Parameters:
          - product_id (int): The ID of the product to sell.
          - quantity (int): The quantity of the product to sell. """

        """ How it works:
          -  The function takes two parameters: product_id and quantity.
          - It searches for the product with the given product_id in the inventory with using for loop.
          - If the product is found and its quantity is sufficient, the specified quantity is deducted from the inventory.
          - The function adds a transaction indicating the sale action to the transactions list.
          - It updates the total revenue by adding the revenue generated from the sale (selling price * quantity).
          - Prints a message to make visible the outcome of the funtion to the user.
          - If the product is not found in the inventory, a message is printed indicating that the product was not found.
          - If the quantity requested for sale exceeds the available quantity in the inventory, a message is printed indicating insufficient quantity."""
        for product in self.inventory:
            if product.id == product_id:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    self.transactions.append(f"Sold {quantity} {product.name}(s).")
                    self.revenue += quantity * product.selling_price
                    print(f"Sold {quantity} {product.name}(s). (id number: {product_id})")
                    return
                else:
                    print("Insufficient quantity in inventory.")
                    return
        print("Product not found in inventory.")

    def show_inventory(self):
        """Display current inventory sorted by ID in ascending order"""
        """ How it works:
        - This function displays the current inventory sorted by product ID in ascending order.
        - It first sorts the inventory list based on the ID attribute of each product using the sorted function.
        - It then iterates over the sorted inventory list and prints information about each product. """
        sorted_inventory = sorted(self.inventory, key=lambda x: x.id)
        for product in sorted_inventory:
            print(product)

    def show_transactions(self):
        """ Display last transactions.

            How it works:
            - This function displays the last transactions recorded in the transactions list.
            - It retrieves the last 5 transactions by slicing the transactions list with [-5:].
            - It then iterates over the last transactions and prints each transaction. 
            - Also, uses a clarifcation message and dashes before and the after the showed transactions to prevent confusion with other outputs."""
        print("The last 5 transations are as follows:")
        print("----------")
        for transaction in self.transactions[-5:]:
            print(transaction)
        print("----------")

    def calculate_total(self, option):
        """ Calculate total revenue, costs, profit, or inventory value.

            Parameters:
            - option (str): The option to specify which total to calculate ('revenue', 'costs', 'profit', or 'inventory value').

            How it works:
            - This function calculates and displays the total revenue, costs, profit, or inventory value based on the specified option.
            - It takes the option parameter to determine which total to calculate.
            - If the option is 'revenue', it calculates and prints the total revenue.
            - If the option is 'costs', it calculates and prints the total costs.
            - If the option is 'profit', it calculates and prints the total profit (revenue - costs).
            - If the option is 'inventory value', it calculates and prints the total value of the inventory (sum of quantity * purchasing price for each product).
            - If the option is invalid, it prints a message indicating that the option is invalid. """
        
        if option == "revenue":
            print(f"Total Revenue: {self.revenue}")
        elif option == "costs":
            print(f"Total Costs: {self.costs}")
        elif option == "profit":
            print(f"Total Profit: {self.revenue - self.costs}")
        elif option == "inventory value":
            total_value = sum(product.quantity * product.purchasing_price for product in self.inventory)
            print(f"Total Inventory Value: {total_value}")
        else:
            print("Invalid option.")

    def clear_all(self):
        """Clear all inventory, transactions, costs, and revenue."""

        # Ask for confirmation from the user
        confirmation = input("Are you sure you want to clear all data? (yes/no): ").lower()

        if confirmation == "yes":
            # Clear inventory, transactions, costs, and revenue
            self.inventory = []
            self.transactions = []
            self.costs = 0
            self.revenue = 0
            print("All data cleared.")
        elif confirmation == "no":
            print("Operation canceled.")
        else:
            print("Invalid input. Operation canceled.")



# Main program loop
if __name__ == "__main__":
    
    #Display logo
    print(logo)

    #An inventory system variable will be created as a InventorySystem object
    inventory_system = InventorySystem()

    while True:
        # Display options to the user
        print("\nWhat would you like to do?")
        print("1. Add a new product")
        print("2. Restock a product")
        print("3. Sell a product")
        print("4. Show inventory")
        print("5. Show last transactions")
        print("6. Calculate total revenue")
        print("7. Calculate total costs")
        print("8. Calculate total profit")
        print("9. Calculate total inventory value")
        print("10. Exit")
        print("99. Clear All")

        # Prompt user for input
        choice = input("Enter your choice: ")

        # Execute the selected option
        if choice == "1":
            """ Add a new product to inventory
                Prompt user for product details and create a new product object.
                Then the created "product" according to users' input, will be used as parameter of the add_product function to add it to inventory.
                Also to catch exceptions try except body is used, and unexpected values directed into a ValueError"""
            try:
                id = int(input("Enter product ID: "))
                name = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))
                purchasing_price = float(input("Enter purchasing price: "))
                selling_price = float(input("Enter selling price: "))
                product = Product(id, name, quantity, purchasing_price, selling_price)
                inventory_system.add_product(product)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            """Used again try except body to catch ValueErrors"""
            try:
                """Restock an existing product in inventory
                Prompt user for product ID and quantity to restock"""
                product_id = int(input("Enter product ID to restock: "))
                quantity = int(input("Enter quantity to restock: "))
                # Restock the product
                inventory_system.restock_product(product_id, quantity)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            """Used again try except body to catch ValueErrors"""
            try:
                """Sell a product from inventory
                Prompt user for product ID and quantity to sell"""
                product_id = int(input("Enter product ID to sell: "))
                quantity = int(input("Enter quantity to sell: "))
                # Sell the product
                inventory_system.sell_product(product_id, quantity)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            # Display current inventory
            inventory_system.show_inventory()
        elif choice == "5":
            # Display last transactions
            inventory_system.show_transactions()
        elif choice == "6":
            # Calculate and display total revenue
            inventory_system.calculate_total("revenue")
        elif choice == "7":
            # Calculate and display total costs
            inventory_system.calculate_total("costs")
        elif choice == "8":
            # Calculate and display total profit
            inventory_system.calculate_total("profit")
        elif choice == "9":
            # Calculate and display total inventory value
            inventory_system.calculate_total("inventory value")
        elif choice == "10":
            # Exit the program
            print("Exiting...")
            break
        elif choice == "99":
            inventory_system.clear_all()

        else:
            # Handle invalid input
            print("Invalid choice. Please enter a number between 1 and 10.")

