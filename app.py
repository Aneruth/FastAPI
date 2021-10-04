from fastapi import Depends, FastAPI, Form,Path,Request
from fastapi.responses import HTMLResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import sys
from helper import response_format,log
import executer
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

print("", "Python Current Version:-", sys.version, "", sep="\n\n")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')

#For UI
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse("home.html",{"request":request} ) 
    pass


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    message = exc.detail
    log(message)
    return response_format(message, exc.status_code, False)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    error = exc.errors()[0]
    message = error["msg"]
    body = error["loc"]
    log(message+","+str(body))
    return response_format(message, 422, False, error=body)

@app.post("/users/")
async def create_user(name:str=Form(...),age:str=Form(...),others:str=Form(...)):
    await executer.create_user({'name':name,'age':age,'others':others})
    return response_format()

@app.post("/address/")
async def create_address(user_id:str=Form(...),line1:str=Form(...),line2:str=Form(None),city:str=Form(...),country:str=Form(...),zipcode:str=Form(...)):
    await executer.create_address({'user_id':user_id,'line1':line1,'line2':line2,'city':city,'country':country,'zipcode':zipcode})
    return response_format()

@app.get("/users/")
async def get_users(request: Request):
    result = await executer.get_users()
    return response_format(data=result)

@app.delete("/users/{id}/")
async def delete_user(id:str=Path(...)):
    await executer.delete_user({'id':id})
    return response_format()

@app.put("/users/{id}/")
async def update_user(id:str=Path(...),name:str=Form(None),age:str=Form(None),others:str=Form(None)):
    await executer.update_user({'id':id,'name':name,'age':age,'others':others})
    return response_format()

@app.get("/users/{id}/")
async def get_user(id:str=Path(...)):
    result  =await executer.get_address({'id':id})
    return response_format(data = result)

@app.get("/users/city/{city}/")
async def user_in_specific_city(city:str=Path(...)):
    result  =await executer.user_in_specific_city({'city':city})
    return response_format(data = result)

@app.delete("/address/{id}/")
async def delete_address(id:str=Path(...)):
    await executer.delete_address({'id':id})
    return response_format()