import psycopg2
import random
import string

# Database connection parameters
db_params = {
    'dbname': 'premiert',
    'user': 'postgres',
    'password': 'kundwa',
    'host': 'localhost',
    'port': '5432'
}

# Connect to the database
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

def generate_plate_number():
    """Generates a random bus plate number"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def get_existing_owner_ids():
    """Fetch all existing owner ids from the owners table starting from 500013"""
    cur.execute("SELECT id FROM owners WHERE id >= 500013")
    result = cur.fetchall()
    return [row[0] for row in result]

def add_bus(bus_id, owner_id):
    """Insert a bus into the buses table"""
    plate_number = generate_plate_number()
    query = """
    INSERT INTO buses (id, plate_number, owner_id)
    VALUES (%s, %s, %s)
    """
    cur.execute(query, (bus_id, plate_number, owner_id))
    conn.commit()

def main():
    # Get a list of existing owner IDs (from 500013 onwards)
    owner_ids = get_existing_owner_ids()

    # Define how many buses you want to insert
    num_buses = 100000  # You can change this number

    # Generate buses for existing owner IDs
    for bus_id in range(1, num_buses + 1):
        owner_id = random.choice(owner_ids)  # Randomly select an existing owner_id
        add_bus(bus_id, owner_id)
        print(f"Bus with ID {bus_id} and Plate {generate_plate_number()} added with Owner ID {owner_id}")

    # Close the cursor and connection
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
