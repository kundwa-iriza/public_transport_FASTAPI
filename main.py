from fastapi import FastAPI, HTTPException
from database import initialize_db, get_connection
from models import Owner, Bus

app = FastAPI()

# Initialize the database
initialize_db()

@app.post("/owners/")
def create_owner(owner: Owner):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO owners (name) VALUES (%s) RETURNING id;",
            (owner.name,)
        )
        owner_id = cursor.fetchone()["id"]
        connection.commit()
        return {"id": owner_id, "name": owner.name}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        connection.close()

@app.post("/buses/")
def create_bus(bus: Bus):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO buses (plate_number, owner_id) VALUES (%s, %s) RETURNING id;",
            (bus.plate_number, bus.owner_id)
        )
        bus_id = cursor.fetchone()["id"]
        connection.commit()
        return {"id": bus_id, "plate_number": bus.plate_number, "owner_id": bus.owner_id}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        connection.close()

@app.get("/owners/")
def list_owners():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM owners;")
        owners = cursor.fetchall()
        return owners
    finally:
        cursor.close()
        connection.close()

@app.get("/buses/")
def list_buses():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM buses;")
        buses = cursor.fetchall()
        return buses
    finally:
        cursor.close()
        connection.close()

