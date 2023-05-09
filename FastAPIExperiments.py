from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

l=[]
@app.get("/")
def root():
    return {"message": "Hello Chinmoy"}

@app.get("/contact")
def contact():
    return {"Chinmoy":"Intern at Knowledge Lens"}
#############################################################################
@app.post("/add")  # FOR ADDING ELEMENTS TO THE LIST
def add(name:str):
    l.append(name)
    return {"names":l}

@app.post("/delete")  # FOR DELETING ELEMENTS TO THE LIST
def delete(name:str):
    l.remove(name)
    return {"After Deletion names":l}

@app.get("/show")
def show():
    return {"The list is":l}

@app.put("/update")
def update(name:str):
    l[1]=name
    return {"Putt method":l}
#############################################################################
class Student(BaseModel):
    name:str
    roll:int
student_details=[]
@app.get("/show_details")
def show_detail():
    return {"List of Students ":student_details}

@app.post("/add_students")
def add_students(student:Student):
    student_details.append(student)
    return {"Adding student":"Successfull"}















