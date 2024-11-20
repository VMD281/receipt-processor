# receipt-processor
# Receipt Processor API

This project is a RESTful web service for processing receipts, extracting data, and calculating reward points. The service exposes endpoints for submitting receipts and fetching reward points for processed receipts.

## Table of Contents
- [Installation](#installation)
- [Requirements](#requirements)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [POST /api/receipts/process](#post-apireceiptsprocess)
  - [GET /api/receipts/<id>/points](#get-apireceiptsidpoints)
- [Testing](#testing)
- [License](#license)

## Installation

### Clone the Repository
```bash
git clone https://github.com/VMD281/receipt-processor.git
cd receipt-processor
```
### Create a Virtual Environment
Ensure python3 and pip is installed and then create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### Install Dependencies
After activating the virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```
### Requirements
> Python 3.11 or higher
> Django 5.x or higher
> Django REST Framework
> Any other dependencies listed in requirements.txt
> Running the Application
> To start the development server, use the following command:

```bash

python manage.py runserver
```
This will start the server on http://0.0.0.0:8000/ or http://localhost:8000/.

### Apply Database Migrations


```bash
python manage.py migrate
```
### Create a Superuser (Optional)
If needed to access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```
### API Endpoints
The API exposes the following endpoints:
POST /api/receipts/process
This endpoint processes a receipt. Must send the receipt data in the request body in JSON format.

Request Body Example:
```json

{
  "store_name": "Store Name",
  "total_amount": 123.45,
  "date_of_purchase": "2024-11-20",
  "items": [
    {"name": "Item 1", "price": 50.00},
    {"name": "Item 2", "price": 73.45}
  ]
}
```
Response Example:
```json

{
  "message": "Receipt processed successfully.",
  "receipt_id": 123
}
```

GET /api/receipts/<id>/points
This endpoint retrieves the reward points for a processed receipt.

Request Example:
GET http://localhost:8000/api/receipts/123/points

Response Example:
```json

{
  "receipt_id": 123,
  "points": 25
}
```
### Testing
To run tests, use Django's test framework:

```bash

python manage.py test

```

