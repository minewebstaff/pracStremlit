from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get():
    return 'Hello World Fast API'