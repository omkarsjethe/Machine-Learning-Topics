# fastapi-patient-records
A FastAPI-based RESTful API to manage patient records with BMI and health verdict calculations.


# FastAPI Patient Management System

A RESTful API built using **FastAPI** to manage patient records including creation, retrieval, update, deletion, and BMI-based health classification.

## 🚀 Features

- Add new patients with details like age, gender, height, and weight.
- Automatically calculate **BMI** and determine health **verdict** (Underweight, Normal, Overweight, Obese).
- Retrieve, edit, delete patient records.
- Sort patients by `height`, `weight`, or `bmi`.
- JSON-based data storage.
- Full API validation using **Pydantic**.

## 🧰 Tech Stack

- FastAPI
- Pydantic
- Python 3
- JSON (as a database)

## API Endpoints
General
GET / – Welcome message.

GET /about – About the API.

Patients
GET /view – View all patients.

GET /patient/{id} – View a specific patient.

POST /create – Create a new patient.

PUT /edit{patient_id} – Update patient data.

DELETE /delete/{id} – Delete a patient.

Utilities
GET /sort?sort_by=bmi&order=asc – Sort patients by bmi, height, or weight



##  Running the API
uvicorn main:app --reload
Make sure patients.json file exists in the same directory. If not, create an empty JSON file:
{}

## 📦 Installation

```bash
git clone https://github.com/<your-username>/fastapi-patient-records.git
cd fastapi-patient-records
pip install -r requirements.txt'''








