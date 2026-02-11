class Person:
    def __init__(self, name, age):
        self.name = name          # Public attribute
        self._age = age           # Protected attribute (convention)
        self.__id = "123456"      # Private attribute (name mangling)

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}")
        print(f"Internal ID: {self.__id}") # Accessible within the class

def main():
    p = Person("Ragul", 25)
    print(f"Public access: {p.name}")
    print(f"Protected access (possible but discouraged): {p._age}")
    
    try:
        print(p.__id) # This will raise an AttributeError
    except AttributeError:
        print("Private access failed as expected!")

if __name__ == "__main__":
    main()
