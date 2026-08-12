from fastapi import FastAPI

# create fastapi app
app = FastAPI()

# define a simple GET endpoint
@app.get("/")
def result():
    return {"message": "Hello world!!"}