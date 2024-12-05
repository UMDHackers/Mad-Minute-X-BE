import fastapi from FastAPI

app = FastAPI()

@app.route('/')
def helloWorld():
  return "Hello world"
