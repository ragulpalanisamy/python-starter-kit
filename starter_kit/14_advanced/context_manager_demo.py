# Context Managers Demo
# Similar to try...finally or using-statements in other languages.

class DatabaseConnection:
    """A simple simulated DB connection using a Context Manager."""
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"Connecting to database: {self.db_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing database connection: {self.db_name}")
        if exc_type:
            print(f"An error occurred: {exc_val}")

def main():
    print("--- Context Manager Demo ---")
    
    # The 'with' statement handles setup (__enter__) and cleanup (__exit__)
    with DatabaseConnection("UserDB") as db:
        print("Executing query: SELECT * FROM users")
        # Uncomment the next line to see error handling
        # raise ValueError("DB Query Failed!")

if __name__ == "__main__":
    main()
