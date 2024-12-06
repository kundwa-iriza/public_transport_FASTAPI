from pydantic import BaseModel

# Owner model for API requests
class Owner(BaseModel):
    name: str

# Bus model for API requests
class Bus(BaseModel):
    plate_number: str
    owner_id: int
