# Zone Sharding API

This project provides a FastAPI-based API for performing CRUD operations on a MongoDB database. The API supports inserting, updating, querying, and deleting records with a specific document structure.

## Prerequisites

- Python 3.8+
- MongoDB instance
- `pip` (Python package installer)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/zone-sharding.git
    cd zone-sharding
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file with your MongoDB connection details:
    ```env
    MONGODB_USERNAME=your_username
    MONGODB_PASSWORD=your_password
    MONGODB_HOST=your_host
    ```

## Running the API

1. Start the FastAPI server:
    ```sh
    uvicorn api:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Insert Record

- **Endpoint:** `/insert`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
      "clientId": 123456,
      "firstName": "John",
      "lastName": "Doe",
      "middleName": "A",
      "email": "john.doe@example.com",
      "digitalClientId": "DIG123456",
      "cardNumber": "1234-5678-9012-3456",
      "birthDate": {
        "day": 15,
        "month": 5,
        "year": 1990
      },
      "tenantId": "TENANT1",
      "gender": "Male",
      "registrationSource": "WEB",
      "status": "A",
      "accountType": "Premium",
      "signupStore": "S123",
      "country": "US",
      "preferredStoreId": 1001,
      "createDate": "2025-02-01T12:00:00Z",
      "updateDate": "2025-02-06T15:00:00Z",
      "riskStatus": "Low",
      "emailVerified": true,
      "smsOptIn": false,
      "addresses": [
        {
          "addressId": 987654,
          "line1": "123 Main St",
          "line2": "Apt 4B",
          "line3": null,
          "city": "New York",
          "stateCode": "NY",
          "postalCode": "10001",
          "countryCode": "US",
          "type": "Home",
          "status": "Active",
          "createDate": "2025-01-01T10:00:00Z",
          "updateDate": "2025-02-05T11:00:00Z",
          "isDefault": true,
          "addressValidated": true,
          "phoneNumber": "123-456-7890"
        },
        {
          "addressId": 876543,
          "line1": "456 Elm St",
          "city": "Los Angeles",
          "stateCode": "CA",
          "postalCode": "90001",
          "countryCode": "US",
          "type": "Work",
          "status": "Inactive",
          "createDate": "2024-12-01T09:00:00Z",
          "updateDate": "2025-01-15T14:00:00Z",
          "isDefault": false,
          "addressValidated": false,
          "phoneNumber": "987-654-3210"
        }
      ]
    }
    ```

### Update Record

- **Endpoint:** `/update/{record_id}`
- **Method:** `PUT`
- **Request Body:** Same as the insert record request body.

### Query Records

- **Endpoint:** `/query`
- **Method:** `GET`
- **Query Parameters:**
    - `clientId` (optional): Filter records by `clientId`.

### Delete Record

- **Endpoint:** `/delete/{record_id}`
- **Method:** `DELETE`

## Load Testing

A JMeter test plan (`LoadTest.jmx`) is included for load testing the API. Update the test plan to use random `clientId` and `location` values.

