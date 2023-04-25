import random
from fastapi import FastAPI

app = FastAPI()

WAIFUVID = [ 
            "https://graph.org/file/4aa0c68c9ff4df2a75790.mp4"
            "https://graph.org/file/ce4181abc0bda8c67ba71.mp4" 
           
           ]

SANJICOOK = [ 
             "https://graph.org/file/639514a0c538160de520f.mp4" 
            ]

@app.get("/waifuvid")
def pnude():
    pic = random.choice(WAIFUVID)
    return {"url" : pic}

@app.get("/sanjicook")
def gnude():
    GIF = random.choice(SANJICOOK)
    return {"url" : GIF}
