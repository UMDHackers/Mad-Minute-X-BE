from fastapi import FastAPI

app = FastAPI()

@app.route('/')
def helloWorld():
  return "Hello world"
