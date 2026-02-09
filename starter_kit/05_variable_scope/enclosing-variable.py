# Enclosing Variable

def cart():
    """Outer function"""
    discount = 10
    
    def discount_price():
        """Inner function"""
        print(f'Discount price is {discount}')

    discount_price()
    
cart()

# print(discount) # NameError: name 'discount' is not defined


