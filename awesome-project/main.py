from fastapi import FastAPI,Path,Query  
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

students = {
    1: {
        "name": "kabir",
        "age" : 23,
        "year": "year 2024"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None
  

@app.get("/")
def index():
    return {"name": "First API data"}

# Path parameters
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0, lt=3)):
    return students.get(student_id, {"error": "Student not found"})


# Query parameters
# @app.get("/get-by-name/{student_id}")
# def get_student(name: str):
#         for student_id in students:
#             if students[student_id] ["name"] == name:
#                 return students[student_id]
#         return {"Data": "Not found"}
            

#combing Path and Qurey Parameters
@app.get("/get-by-name/{student_id}")
def get_student(student_id: int = Path(..., description= "The ID of the student"), name: str = Query(None, descriptipon="The name of the student"), test: int = Query(..., description="Some test integer value")):
         if student_id in students:
            if students[student_id]["name"] == name:
                return {
                    "student": students[student_id],
                    "test": test  # Return the test value as well
            }
         return {"Data": "Not found"}
     
     
#Request Body and The PUT Methode
@app.post("/create-student/{stdudent_id}")
def create_student(studnet_id : int, student : Student):
    if studnet_id in students:
        return {"error": "Student already exists."}
    students[studnet_id] = student.dict()  # Store the Pydantic model as a dictionary
    return students[studnet_id]


#put methode(means allready exists methode for update)
@app.put("/update-stduent/{student_id}")
def update_student(student_id : int, student: UpdateStudent):
    if student_id not in students:
        return {"Error" : "Student doen not exitst"}
     # Only update the fields that are provided in the request body
    if student.name is not None:
        students[student_id]["name"] = student.name
    if student.age is not None:
        students[student_id]["age"] = student.age
    if student.year is not None:
        students[student_id]["year"] = student.year
    
    return {"Message": "Student updated successfully", "Student": students[student_id]}

# //gt = getter than, lt = less than, ge = gatter than eques to , le = less than equesto