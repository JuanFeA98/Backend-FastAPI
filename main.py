from fastapi import FastAPI
import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/JuanFeA98/ce470cf42a2b4449a314adef81211bf5/raw/d014b5d9cd080d99af363c2e511e16a84fc92cf3/CSS_colors.csv')

app = FastAPI()

@app.get("/")
async def root():
    return {'mesagge':'Hello'}

@app.get("/colors")
async def root():
    return df