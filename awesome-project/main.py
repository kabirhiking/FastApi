from fastapi import FastAPI,Path # type: ignore

app = FastAPI()

students = {
    1: {
        "name": "kabir",
        "age" : "23",
        "class": "year 2024"
    }
}

@app.get("/")
def index():
    return {"name": "First data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0, lt=3)):
    return students.get(student_id, {"error": "Student not found"})

# @app.get("/get-student/{student_id}")
# def get_student(stduent_id: int = Path(None, description= "The ID of the student you want to view", gt=0, lt=3)):
#     return students[stduent_id]


# //gt = getter than, lt = less than, ge = gatter than eques to , le = less than equesto