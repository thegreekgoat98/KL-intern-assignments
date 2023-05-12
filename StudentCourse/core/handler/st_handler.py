from core.db.mongodb import myDB
from schema.models import Student

def home():
    return {"This is for student registration into a course."}

def show():
    result = list(myDB.find({}))
    final_list = []
    for stud in result:
        del stud["_id"]
        final_list.append(stud)
    return {"The data for all students ": final_list}

def add(student:Student):
    if list(myDB.find({"roll":student.roll})) == []:
       myDB.insert_one(student.dict())
       return {"Success":"Added student in the course successfully"}
    else:
       return {"Error":"Cannot add student, already enrolled in a course"}
    
def update(roll:int,student: Student):
    if list(myDB.find({"roll":roll})) == []:
        return {"Error":"Student not enrolled in any course"}
    else:
        myDB.update_one({"roll":roll},{"$set":student.dict()})
        return {"Success":"Updated succesfully"}
    
def delete(roll:int):
    if list(myDB.find({"roll":roll})) == []:
        return {"Error":"Student has not enrolled in any course till now"}
    # del course_details["roll"]
    myDB.delete_one({"roll":roll})
    return {"Success":"Deleted the student from the course"}