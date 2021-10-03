from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Operación GET sencilla
@app.get("/")
async def root():
    return {'mesagge':'Hello'}

# Operación GET desde un archivo remoto
@app.get("/colors")
async def colors():
    df = pd.read_csv('https://gist.githubusercontent.com/JuanFeA98/ce470cf42a2b4449a314adef81211bf5/raw/d014b5d9cd080d99af363c2e511e16a84fc92cf3/CSS_colors.csv')
    return df

# Operación GET con parametros (Existe la opción de establecer el formato de los parametros)
@app.get("/items_num/{item_id}")
async def root(item_id: int):
    if int(item_id):
        return {f'item id {item_id}': item_id}
    else:
        return 'Esta ruta no esta disponible'



# Project key: b0jtn76s_u1PDhG44pYApJQAuHA3cjX1YHnnEYjL2
# Project Id: b0jtn76s