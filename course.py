from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Student(BaseModel):
    name:str
    course:str

course_details={}   

@app.get("/")    
def root():
    return {"This is for student registration into a course."}

@app.get("/show_details")    #{shows the data of courses and the student enrolled}
def show():
    return {"The data for all students ": course_details}

@app.post("/add/{roll}")   
def add(roll: int, student:Student):
   course_details[roll] = student.dict()
   return course_details
    
@app.put("/update/{roll}")
def update(roll:int,student: Student):
    if roll not in course_details.keys():
        return {"Cannot Update":"Student not present in any course."}
    else:
        course_details[roll] = Student
        return {"Success":"Updated the student in the course"}

@app.delete("/delete/{roll}")
def delete(roll:int):
    if roll not in course_details:
        return {"Cannot Delete":"Student not present in any course."}
    else:
        del course_details[roll]
        return {"Success":"Deleted the student from the course"}







