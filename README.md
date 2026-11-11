# Task Management API

## Project Description

A REST API built using Python and FastAPI
to manage daily tasks.

## Technologies Used

- Python
- FastAPI
- Pydantic
- SQLite
- Pytest

## Features

- Create tasks
- Retrieve all tasks
- Retrieve task by ID
- Update tasks
- Delete tasks
- Filter tasks by status
- Filter tasks by priority
- Input validation

## Installation

1. Clone the repository.

2. Create virtual environment.

3. Install dependencies.

pip install fastapi uvicorn pytest httpx

## Run Application

uvicorn main:app --reload

## API Documentation

http://127.0.0.1:8000/docs

## Run Tests

pytest -v