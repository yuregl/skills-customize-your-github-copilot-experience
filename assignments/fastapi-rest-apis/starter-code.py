"""
Starter code for building a REST API with FastAPI
This template provides a basic structure for creating a REST API
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Initialize FastAPI application
app = FastAPI(
    title="Student Management API",
    description="A simple API for managing student records",
    version="1.0.0"
)

# Pydantic models for data validation
class StudentBase(BaseModel):
    name: str
    email: str
    grade: float
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "João Silva",
                "email": "joao@example.com",
                "grade": 8.5
            }
        }

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Sample in-memory database (replace with real database in production)
students_db: List[dict] = [
    {
        "id": 1,
        "name": "Alice Santos",
        "email": "alice@example.com",
        "grade": 9.0,
        "created_at": datetime.now()
    },
    {
        "id": 2,
        "name": "Bob Costa",
        "email": "bob@example.com",
        "grade": 7.5,
        "created_at": datetime.now()
    }
]

next_id = 3

# Root endpoint
@app.get("/")
def read_root():
    """Root endpoint that returns a welcome message"""
    return {
        "message": "Welcome to Student Management API",
        "docs": "/docs"
    }

# GET all students
@app.get("/students", response_model=List[Student])
def get_students():
    """Retrieve all students from the database"""
    return students_db

# GET a specific student by ID
@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    """Retrieve a specific student by their ID"""
    student = next((s for s in students_db if s["id"] == student_id), None)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# POST - Create a new student
@app.post("/students", response_model=Student, status_code=201)
def create_student(student: StudentCreate):
    """Create a new student record"""
    global next_id
    new_student = {
        "id": next_id,
        "name": student.name,
        "email": student.email,
        "grade": student.grade,
        "created_at": datetime.now()
    }
    students_db.append(new_student)
    next_id += 1
    return new_student

# PUT - Update an existing student
@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student_update: StudentCreate):
    """Update an existing student record"""
    student = next((s for s in students_db if s["id"] == student_id), None)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student.update({
        "name": student_update.name,
        "email": student_update.email,
        "grade": student_update.grade
    })
    return student

# DELETE - Remove a student
@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    """Delete a student record"""
    global students_db
    original_length = len(students_db)
    students_db = [s for s in students_db if s["id"] != student_id]
    
    if len(students_db) == original_length:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return None

# To run this API, use:
# uvicorn starter-code:app --reload
