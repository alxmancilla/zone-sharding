from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import random
import pymongo
import certifi
import threading
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# MongoDB connection details
# MongoDB connection details
username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")
host = os.getenv("MONGODB_HOST")
# host = "sephorapoc-atlasmanaged.z1llw.mongodb.net"
us_states = ["US-AZ","US-CA", "US-PA", "US-VA"]

mongodb_url = f'mongodb+srv://{username}:{password}@{host}/test?retryWrites=true&w=majority&appName=api'
connection = pymongo.MongoClient(mongodb_url, tlsCAFile=certifi.where())
db = connection.test
collection = db.records

class BirthDate(BaseModel):
    day: int
    month: int
    year: int

class Address(BaseModel):
    addressId: int
    line1: str
    line2: Optional[str] = None
    line3: Optional[str] = None
    city: str
    stateCode: str
    postalCode: str
    countryCode: str
    type: str
    status: str
    createDate: datetime
    updateDate: datetime
    isDefault: bool
    addressValidated: bool
    phoneNumber: str

class Record(BaseModel):
    clientId: int
    firstName: str
    lastName: str
    middleName: Optional[str] = None
    email: EmailStr
    digitalClientId: str
    cardNumber: str
    birthDate: BirthDate
    tenantId: str
    gender: str
    registrationSource: str
    status: str
    accountType: str
    signupStore: str
    country: str
    location: str
    preferredStoreId: int
    createDate: datetime
    updateDate: datetime
    riskStatus: str
    emailVerified: bool
    smsOptIn: bool
    addresses: List[Address]

@app.post("/insert", response_model=Record)
def insert_record(record: Record):
    record_dict = record.dict()
    collection.insert_one(record_dict)
    return record

@app.put("/update/{record_id}", response_model=Record)
def update_record(record_id: str, record: Record):
    result = collection.update_one({"_id": pymongo.ObjectId(record_id)}, {"$set": record.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Record not found")
    return record

@app.get("/query", response_model=List[Record])
def query_records(clientId: Optional[int] = None):
    query = {}
    if clientId:
        query["clientId"] = clientId
    records = list(collection.find(query))
    return records

@app.delete("/delete/{record_id}")
def delete_record(record_id: str):
    result = collection.delete_one({"_id": pymongo.ObjectId(record_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"message": "Record deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)