from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Solucionar problemas de CORS
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return 'Hello World'

@app.get("/items/{item_id}")
def read_items(item_id):
    return {'item_id': item_id}

@app.get("/test")
def test():
    return {
        "saludo": "Probando",
        "numero": 13
    }