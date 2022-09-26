from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse

from pydantic import BaseModel, EmailStr

from function_JWT import write_token, validate_token

auth_routes = APIRouter()

class User(BaseModel):
    username: str
    email: EmailStr


@auth_routes.post('/login')
def login(user: User):
    if user.username == 'Prueba':
        return write_token(user.dict())
    else:
        return JSONResponse(content={'Message': 'User not found'}, status_code=404)

@auth_routes.post('/verify/token')
def verify_token(Authorization: str=Header(None)):
    print(Authorization)
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)