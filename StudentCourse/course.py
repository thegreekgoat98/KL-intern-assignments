from fastapi import FastAPI
from core.handler.st_handler import show,add,update,delete,home
from schema.models import Student

app = FastAPI()

@app.get("/") 
def fun():
    return home()
    
@app.get("/show_details")
def fun():
    return show()

@app.post("/add") 
def fun(student:Student):
    return add(student)
    
@app.put("/update/{roll}")
def fun(roll:int,student:Student):
    return update(roll,student)
    
@app.delete("/delete/{roll}")
def fun(roll:int):
    return delete(roll)


    
