from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return 'Hello World'

@app.get("/items/{item_id}")
def read_items(item_id):
    return {'item id': item_id}