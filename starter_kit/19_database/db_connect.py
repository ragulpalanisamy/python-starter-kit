# Database Connection Example with Secure Password

import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

def connect_to_db():
    db_user = os.getenv("DB_USER", "default_user")
    db_pass = os.getenv("DB_PASSWORD") # From .env
    
    if not db_pass:
        print("Error: DB_PASSWORD not found in environment!")
        return

    print(f"Connecting to database as {db_user}...")
    # Simulation of connection
    print("Connection successful! (Simulated)")

if __name__ == "__main__":
    # Create a dummy .env for testing if it doesn't exist
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write("DB_PASSWORD=secret_pass_123\nDB_USER=ragul_db")
    
    connect_to_db()
