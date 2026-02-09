# ordering food from swiggy

delivery_partner = "swiggy" # global variable

def order_food():
    food = "ice briyani" # Enclosing variable
    
    def total_quantity():
        quantity = 2 # local variable
        print(f'Ordering {quantity} {food} from {delivery_partner}')
    
    total_quantity()

order_food()

# built-in
print(__file__)