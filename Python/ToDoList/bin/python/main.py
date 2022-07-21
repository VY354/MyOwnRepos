import uvicorn

from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# contain functions to get data, insert and delete
import dbManaging
# contain task card class
import requestObjects

# ======================================== objects =====================================

api = FastAPI()

# mounting css and js file in folder "static"
api.mount('/static', StaticFiles(directory='../static'), name='static')

# create templates object. Have only 2 templates: index.html and taskCreator.html
temp = Jinja2Templates(directory='../html')


# ======================================== get requests ========================================

# get index.html page
@api.get(path='/index.html', response_class=HTMLResponse)
async def index(r: Request):
    context = {'request': r}
    # create 'cards' objects from selected data to pass in html template
    cardObjs = [requestObjects.Task(**x) for x in dbManaging.getTaskCards()]
    context.update({'Cards': cardObjs})

    return temp.TemplateResponse(name='index.html', context=context)


# get taskCreator.html page
@api.get(path='/taskCreator.html', response_class=HTMLResponse)
async def taskCreatorPage(r: Request):
    context = {'request': r}
    return temp.TemplateResponse(name='taskCreator.html', context=context)


# ======================================== post requests ========================================


# go here when click 'add new task' button in taskCreator.html
@api.post(path='/taskCreator.html/add', response_class=RedirectResponse)
async def addTask(r: Request):
    # get form data (button data is not presented)
    dataDict = dict((await r.form()).items())
    # passing card data to db manager
    dbManaging.insertTaskCard(dataDict)

    # redirecting to main page (if return html template, URL will not be changed)
    return RedirectResponse(url='/index.html', status_code=status.HTTP_303_SEE_OTHER)


# go here when cick 'done' button on sidebar menu of card; passing card id as path parameter
@api.post(path='/index.html/done/{id}', response_class=RedirectResponse)
async def doneTask(id: int):
    # delete query to db by card id
    dbManaging.removeTaskCard(id)
    return RedirectResponse(url='/index.html', status_code=status.HTTP_303_SEE_OTHER)


# go here when cick 'done' button on sidebar menu of card; passing card id as path parameter (same as doneTask())
@api.post(path='/index.html/remove/{id}', response_class=RedirectResponse)
async def removeTask(id: int):
    # delete query to db by card id
    dbManaging.removeTaskCard(id)
    return RedirectResponse(url='/index.html', status_code=status.HTTP_303_SEE_OTHER)


# ======================================== ... ========================================


# server settings
app = 'main:api'
host = '127.0.0.1'
port = 8000
reload = True


def main():
    uvicorn.run(app, host=host, port=port, reload=reload)


if __name__ == '__main__':
    main()
