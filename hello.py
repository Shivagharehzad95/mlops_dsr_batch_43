from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def read_root():
    return{"hello": "world"}

@app.get('/joon')
def read_root():
    return{'jana'}