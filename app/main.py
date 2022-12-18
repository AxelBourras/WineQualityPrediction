from fastapi import FastAPI

from api.endpoints import api
from api.endpoints import api

app = FastAPI()

app.include_router(api.router)

info = [
    {
        "route"    : "/api/predict", 
        "method"   : "POST",
        "params"   : "One wine",
        "response" : "Predict the quality of the wine input"
    },
    {
        "route"    : "/api/predict", 
        "method"   : "GET",
        "params"   : None,
        "response" : "Try to get the 'perfect wine'"
    },
    {
        "route"    : "/api/model",
        "method"   : "GET",
        "params"   : None,
        "response" : "Serialize the last created model"
    },
    { 
        "route"    : "/api/model/description",
        "method"   : "GET",
        "params"   : None,
        "response" : "Bring information about the last created model"
    },
    { 
        "route"    : "/api/model",
        "method"   : "PUT",
        "params"   : "One wine",
        "response" : "Add a wine to the model"
    },
    { 
        "route"    : "/api/model/retrain",
        "method"   : "POST",
        "params"   : None,
        "response" : "Train the model again"
    }
]

@app.get("/")
async def root():
    """
        Guide to use APIs on the welcome page
    """
    return {"Title": "Welcome on the wine quality prediction API!! Here you can see some information about it",
            "First, here are the different available APIs": info,
            "Then, let's use the docs to call APIs": "http://127.0.0.1:8000/docs",
            "It's your turn!": "Now you can use our API!"}
