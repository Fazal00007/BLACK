import random
from fastapi import FastAPI

app = FastAPI()

WAIFUVID = [ 
            "" 
           ]

SANJICOOK = [ 
             "" 
            ]

@app.get("/waifuvid")
def pnude():
    pic = random.choice(WAIFUVID)
    return {"url" : pic}

@app.get("/sanjicook")
def gnude():
    GIF = random.choice(SANJICOOK)
    return {"url" : GIF}
