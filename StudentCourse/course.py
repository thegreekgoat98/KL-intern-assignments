from fastapi import FastAPI
from core.handler.student_handler import handler
from schema.models import Student,email

app = FastAPI()

obj=handler()

@app.get("/") 
def fun():
    return obj.home()
    
@app.get("/show_details")
def show():
    return obj.show()

@app.post("/add") 
def add(student:Student):
    return obj.add(student)
    
@app.put("/update/{roll}")
def update(roll:int,student:Student):
    return obj.update(roll,student)
    
@app.delete("/delete/{roll}")
def delete(roll:int):
    return obj.delete(roll)

@app.post("/send_email")
def sendEmail(Email: email):
    return obj.send_email(Email)


    
