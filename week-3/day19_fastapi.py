from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get('/info')
def info():
    current_time = datetime.now()
    name = 'Chang feng'
    return {"name": name, "time": current_time.isoformat()}

@app.get('/hello')
def hello():
    return {"message":"Hello World!"}