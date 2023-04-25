import random
from fastapi import FastAPI

app = FastAPI()

WAIFUVID = [
 
            "https://graph.org/file/4aa0c68c9ff4df2a75790.mp4"
            "https://graph.org/file/ce4181abc0bda8c67ba71.mp4" 
            "https://te.legra.ph/file/e14a90e57c83a98eb84d2.mp4"
            "https://te.legra.ph/file/d732ee927b8d619611739.mp4"
            "https://te.legra.ph/file/97926553a6687e6519f98.mp4"
            "https://te.legra.ph/file/62bdcd55a50a2cda06315.mp4"
            "https://te.legra.ph/file/047a3d44775eb65e8f5c3.mp4"
            "https://te.legra.ph/file/fb06af136e072dc8c2a66.mp4"
            "https://te.legra.ph/file/ca2239968b7c77573c8d9.mp4"
            "https://te.legra.ph/file/acfde58f3984e1ebca7e6.mp4"
            "https://te.legra.ph/file/2194ebde2ba6f241f03e1.mp4"
            "https://te.legra.ph/file/0413299180a773c2a5bc4.mp4"
            "https://te.legra.ph/file/b2bea52a49a1fa1fe3b61.mp4"
            "https://te.legra.ph/file/e837903062e4a688c8fb8.mp4"
            "https://te.legra.ph/file/46d851acc713dafd6f329.mp4"
            "https://te.legra.ph/file/4fd573b2036565add3070.mp4"
            "https://te.legra.ph/file/d01a4a03f911cb4e70fd8.mp4"
            "https://te.legra.ph/file/bd8e486867bd206cd5ed4.mp4"
           
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
