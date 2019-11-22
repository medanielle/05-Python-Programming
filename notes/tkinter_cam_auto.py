import tkinter as tk

# Produt class to store product and checkbutton information
class Product:
    def __init__(self, name, price):
        self.name = str(name)
        self.price = float(price)
        self.checked = tk.BooleanVar()


class Shop(tk.Tk):
    def __init__(self, initial_products, initial_discounts):
        super().__init__()
        # keep all the window information inside the class to make it easily portable
        self.title('Joe\'s Automotive Shop')
        self.geometry('400x500')

        # generate a list of Product objects
        self.products = [Product(name, price) for name, price in initial_products.items()]

        # build the product checkbuttons then place them in the window
        self.product_buttons = self.create_product_buttons(self.products)
        for product in self.product_buttons:
            product.pack(fill=tk.X)

        self.total_price = 0.00
        self.total_price_with_discount = 0.00

        # build the total price label then place it in the window
        self.total_price_label = tk.Label(self, text=f"With no discount your total is ${self.total_price:.2f}", pady=10)
        self.total_price_label.pack(fill=tk.X)

        # build the discounts and which one is selected
        self.discounts = [discount_entry for discount_entry in initial_discounts]
        self.discount_selected = tk.IntVar()

        # build the discount radiobuttons and place them in the window
        self.discount_radiobuttons = self.create_discount_radiobuttons(self.discounts)
        for discount_radiobutton in self.discount_radiobuttons:
            discount_radiobutton.pack(fill=tk.X)


    # use a function to help cut down on repetition
    def create_discount_radiobuttons(self, discounts):
        discount_radiobuttons = []
        # i need not only the discount dict but the index it was at in the list
        for index, discount in enumerate(discounts):
            # cool trick to unpack a 1 item dict
            (who, amount), = discount.items()
            discount_radiobuttons.append(tk.Radiobutton(
                anchor='w',
                command=self.calculate_discount,
                text=f"{who} discount: {amount * 100:.0f}%",
                variable=self.discount_selected,
                value=index
            ))
        return discount_radiobuttons

    # i should probably combine calculate_price() and calculate_discount(), i should...
    def calculate_price(self):
        # sum up the list of all the checked product's prices
        self.total_price = sum([product.price for product in self.products if product.checked.get()])
        if self.discount_selected.get():
            self.calculate_discount()
        else:
            self.total_price_label.configure(text=f"With no discount your total is ${self.total_price:.2f}")

    def calculate_discount(self):
        # unpack the appropriate discount based on the self.discount_select.get() value
        # actually i hate this trick and should of just had a better initial data type
        (who, discount_amount), = self.discounts[self.discount_selected.get()].items()
        new_total_price = self.total_price - (self.total_price * float(discount_amount))
        self.total_price_with_discount = new_total_price
        # discount ordering is important, first discount should always be no discount
        if self.discount_selected.get():
            self.total_price_label.configure(text=f"With the {who} discount your total is new total is ${self.total_price_with_discount:.2f}")
        else:
            self.total_price_label.configure(text=f"With no discount your total is ${self.total_price:.2f}")

    # nothing special here, just a comment for comment sake
    def create_product_buttons(self, products):
        product_buttons = []
        for product in products:
            product_buttons.append(tk.Checkbutton(
                anchor='w',
                bg='lightgrey',
                command=self.calculate_price,
                fg='black',
                pady=10,
                text=f"{product.name} (${product.price:.2f})",
                relief='raised',
                variable=product.checked))
        return product_buttons
    

if __name__ == "__main__":
    initial_products = {
        'Piston Return Springs': 49.99,
        'Muffler Bearing': 12.95,
        'Blinker Fluid': 15.99,
        'Suspension Hook': 38.98,
        'Radiator Springs': 149.99,
        'Johnson Rods': 89.95,
        'Flux Capacitor': 249.99,
        'Easy2Math Product': 100.00
    }
    # should probably use an OrderedDict() here.
    # disregard, OrderedDict()s do not do what i thought.
    # https://stackoverflow.com/questions/27726245/getting-the-key-index-in-a-python-ordereddict
    initial_discounts = [
        # first discount should always be no discount
        {'No': 0.0},
        {'Dependent': 0.1},
        {'Military': 0.2},
        {'Clown': -0.1}
    ]
    shop = Shop(initial_products, initial_discounts)
    shop.mainloop()
