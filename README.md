# Vehicle Inventory & Booking API

## Project Overview

The Vehicle Inventory & Booking API is a RESTful backend application developed using Python, Django and Django REST Framework.

It allows users to manage vehicle inventory and create vehicle bookings with automatic price calculation and booking validation.

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- python-dotenv

## Features

### Vehicle Management
- Create a vehicle.
- Retrieve all vehicles.
- Retrieve vehicle details by ID.
- Update vehicle information.
- Delete a vehicle.
- Filter vehicles by brand, fuel type and availability.

### Booking Management
- Create a booking.
- Retrieve all bookings.
- Retrieve booking details by ID.
- Automatically calculate the total booking amount.
- Prevent overlapping bookings for the same vehicle.
- Validate customer phone numbers.
- Prevent bookings with past start dates.
- Validate booking date ranges.

## Project Structure

```text
vehicle_system/
│
├── inventory/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── vehicle_system/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── .env
├── .env.example
├── .gitignore
├── db.sqlite3
├── manage.py
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd vehicle_system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install django==3.2.25 djangorestframework python-dotenv
```

### 5. Configure environment variables

Create a `.env` file in the project root.

Add:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Use your own generated secret key. Do not upload `.env` to GitHub.

### 6. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

The API will be available at:

http://127.0.0.1:8000/

## API Endpoints

### Vehicle APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/vehicles/` | List all vehicles |
| POST | `/api/vehicles/` | Create a vehicle |
| GET | `/api/vehicles/<id>/` | Retrieve vehicle details |
| PUT | `/api/vehicles/<id>/` | Update vehicle |
| DELETE | `/api/vehicles/<id>/` | Delete vehicle |

### Booking APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/bookings/` | List all bookings |
| POST | `/api/bookings/` | Create a booking |
| GET | `/api/bookings/<id>/` | Retrieve booking details |

## Vehicle Filtering

Vehicles can be filtered using query parameters.

Examples:

```text
/api/vehicles/?brand=Toyota
/api/vehicles/?fuel_type=Diesel
/api/vehicles/?is_available=true
```

## Sample API Requests

### Create a Vehicle

POST `/api/vehicles/`

```json
{
    "name": "Fortuner",
    "brand": "Toyota",
    "year": 2022,
    "price_per_day": "3000.00",
    "fuel_type": "Diesel",
    "is_available": true
}
```

### Create a Booking

POST `/api/bookings/`

```json
{
    "vehicle": 2,
    "customer_name": "Test Customer",
    "customer_phone": "9876543210",
    "start_date": "2026-11-10",
    "end_date": "2026-11-12"
}
```

The total amount is calculated automatically based on the number of booking days and the vehicle's daily rental price.

## Booking Validation Rules

- Customer phone number must contain exactly 10 digits.
- Booking start date cannot be in the past.
- End date must be after start date.
- The same vehicle cannot have overlapping bookings.
- Total booking amount is calculated automatically.
- Vehicle availability is updated after a successful booking.

## Example Booking Calculation

Vehicle price per day: ₹3,000

Booking duration: 2 days

Total amount: ₹6,000

## Running Tests

Run Django's system checks:

```bash
python manage.py check
```

Run application tests:

```bash
python manage.py test
```

## Developer

Developed as a Django REST Framework backend project.
