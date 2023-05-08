from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello Chinmoy"}

@app.get("/contact")
def contact():
    return {"Chinmoy":"Intern at Knowledge Lens"}