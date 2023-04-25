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
            "https://te.legra.ph/file/d9e6eb7c455b3fbe7408d.mp4"
            "https://te.legra.ph/file/0e4ebae9b45da9234bcd1.mp4"
            "https://te.legra.ph/file/5e99a529405866a5838cb.mp4"
            "https://te.legra.ph/file/436bceb69f9b31bbaac79.mp4"
            "https://te.legra.ph/file/0b8cc2082ef13cbead1fd.mp4"
            "https://te.legra.ph/file/ece2a9bef9194eaeb2815.mp4"
            "https://te.legra.ph/file/4ce0b8c9c0ca2e9cbbe33.mp4"
            "https://te.legra.ph/file/01031fe726a39699e8a3d.mp4"
            "https://te.legra.ph/file/51e6fc6e611d716614c2c.mp4"
            "https://te.legra.ph/file/4aae4f4b396556e7bd972.mp4"
            "https://te.legra.ph/file/1a06cd971ba40872a432b.mp4"
            "https://te.legra.ph/file/83687b6a1310f7c8090e8.mp4"
            "https://te.legra.ph/file/8f846a6b96ff6abd7bba3.mp4"
            "https://te.legra.ph/file/bc8e5655c459d7357fde8.mp4"
            "https://te.legra.ph/file/e0d13eead0d43e695d616.mp4"
            "https://te.legra.ph/file/b49b82604bfc0b319d400.mp4"

           ]

SANJICOOK = [ 
             "https://graph.org/file/639514a0c538160de520f.mp4" 
            ]

@app.get("/waifuvid")
def pnude():
    pic = random.choice(WAIFUVID)
    return {"url" : GIF}

@app.get("/sanjicook")
def gnude():
    GIF = random.choice(SANJICOOK)
    return {"url" : GIF}
