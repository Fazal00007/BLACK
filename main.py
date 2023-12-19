from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, FileResponse
import requests
import json
import secrets
from dateutil import parser
import random 
import requests
import httpx


app = FastAPI()
@app.get('/')
def root(request: Request):
    return {"root": request.url.hostname}


@app.get('/search')
async def search(query, page):
    query = query
    page = page  
    res = {
        "search_text": query,
        "tags":
            [],
        "brands":
            [],
        "blacklist":
            [],
        "order_by": 
            [],
        "ordering": 
            [],
        "page": page,
    }
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    x = requests.post("https://search.htv-services.com", headers=headers, json=res)
    rl = x.json()
    text = {
        "response": json.loads(rl'hits']),
        "page": rl['page']
    }
    return text

@app.get('/recent')
async def recent(page = 0):
    page = page
    url = "https://search.htv-services.com"
    res = {
        "search_text": "",
        "tags":
            [],
        "brands":
            [],
        "blacklist":
            [],
        "order_by": "created_at_unix",
        "ordering": "desc",
        "page": page,
    }
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    x = requests.post(url, headers=headers, json=res)
    rl = x.json()
    text = {
        "reposone": json.loads(rl['hits']),
        "page": rl['page']
    }
    return text

@app.get('/trending')
async def trending(time = "month",page = 0):
    time = time
    p = page
    headers = {"X-Signature-Version": "web2",
               "X-Signature": secrets.token_hex(32)}
    x = requests.get(f"https://hanime.tv/api/v8/browse-trending?time={time}&page={p}", headers=headers)
    rl = x.json()
    text = {
        "reposone": rl["hentai_videos"],
        "time": rl["time"],
        "page": rl["page"]
    }
    return text


@app.get('/details')
async def details(id):
    id = id
    x = f"https://hanime.tv/api/v8/video?id={id}"
    x = requests.get(x)
    rl = x.json()
    created_at = rl["hentai_video"]["created_at"] = parser.parse(
        rl["hentai_video"]["created_at"]).strftime("%Y %m %d")
    released_date = rl["hentai_video"]["released_at"] = parser.parse(
        rl["hentai_video"]["released_at"]).strftime("%Y %m %d")
    view = rl["hentai_video"]["views"] = "{:,}".format(
        rl["hentai_video"]["views"])
    tags = rl["hentai_video"]["hentai_tags"]    
    text = {
        "query": rl["hentai_video"]["slug"],
        "name": rl["hentai_video"]["name"],
        "poster": rl["hentai_video"]["cover_url"],
        "id": rl["hentai_video"]["id"],   
        "description": rl["hentai_video"]["description"],     
        "views": view,
        "brand": rl["hentai_video"]["brand"],
        "created_at": created_at,
        "released_date": released_date,
        "is_censored": rl["hentai_video"]["is_censored"],         
        "tags": [x["text"] for x in tags]         
    }
    return text


@app.get('/link')
async def hentai_video(id):
    url = f"https://hanime.tv/api/v8/video?id={id}" 
    x = requests.get(url, headers={
        "X-Session-Token": "PhzIzReFsg7g2GZi-tz9KVpR2LskgMP8-l_xJ0kmbwhSuBOcD3yZJeOoQKS-ND1w3qFCGj0Y2HzfJ4renU82W25BNSVI6KnmwfiN5e9lueyQOYbZ0RVKmS2Ek1fLKvMnS_3ktEUiFOTjSCezPusemw==(-(0)-)hDLS0eC_45mNW15pn3ZJYQ==",
    })   
    rl = x.json()   
    text = {
        "data": rl["videos_manifest"]["servers"][0]["streams"]
    }
    return text

@app.get('/play')
async def m3u8(link):
    x = f'''
    <DOCTYPE html>
    <html>
    <body>
    <video id="live"  autoplay controls>
        <source src="{link}" type="video/mp4">
        </video>
        </body>
        </html>
    '''
    return HTMLResponse(content=x, status_code=200)
            
# ---------- Cosplay ----------- #

WAIFUVID = [
            "https://graph.org/file/4aa0c68c9ff4df2a75790.mp4",
            "https://graph.org/file/ce4181abc0bda8c67ba71.mp4" ,
            "https://te.legra.ph/file/e14a90e57c83a98eb84d2.mp4",
            "https://te.legra.ph/file/d732ee927b8d619611739.mp4",
            "https://te.legra.ph/file/97926553a6687e6519f98.mp4",
            "https://te.legra.ph/file/62bdcd55a50a2cda06315.mp4",
            "https://te.legra.ph/file/047a3d44775eb65e8f5c3.mp4",
            "https://te.legra.ph/file/fb06af136e072dc8c2a66.mp4",
            "https://te.legra.ph/file/ca2239968b7c77573c8d9.mp4",
            "https://te.legra.ph/file/acfde58f3984e1ebca7e6.mp4",
            "https://te.legra.ph/file/2194ebde2ba6f241f03e1.mp4",
            "https://te.legra.ph/file/0413299180a773c2a5bc4.mp4",
            "https://te.legra.ph/file/b2bea52a49a1fa1fe3b61.mp4",
            "https://te.legra.ph/file/e837903062e4a688c8fb8.mp4",
            "https://te.legra.ph/file/46d851acc713dafd6f329.mp4",
            "https://te.legra.ph/file/4fd573b2036565add3070.mp4",
            "https://te.legra.ph/file/d01a4a03f911cb4e70fd8.mp4",
            "https://te.legra.ph/file/bd8e486867bd206cd5ed4.mp4",
            "https://te.legra.ph/file/d9e6eb7c455b3fbe7408d.mp4",
            "https://te.legra.ph/file/0e4ebae9b45da9234bcd1.mp4",
            "https://te.legra.ph/file/5e99a529405866a5838cb.mp4",
            "https://te.legra.ph/file/436bceb69f9b31bbaac79.mp4",
            "https://te.legra.ph/file/0b8cc2082ef13cbead1fd.mp4",
            "https://te.legra.ph/file/ece2a9bef9194eaeb2815.mp4",
            "https://te.legra.ph/file/4ce0b8c9c0ca2e9cbbe33.mp4",
            "https://te.legra.ph/file/01031fe726a39699e8a3d.mp4",
            "https://te.legra.ph/file/51e6fc6e611d716614c2c.mp4",
            "https://te.legra.ph/file/4aae4f4b396556e7bd972.mp4",
            "https://te.legra.ph/file/1a06cd971ba40872a432b.mp4",
            "https://te.legra.ph/file/83687b6a1310f7c8090e8.mp4",
            "https://te.legra.ph/file/8f846a6b96ff6abd7bba3.mp4",
            "https://te.legra.ph/file/bc8e5655c459d7357fde8.mp4",
            "https://te.legra.ph/file/e0d13eead0d43e695d616.mp4",
            "https://te.legra.ph/file/b49b82604bfc0b319d400.mp4",
            "https://te.legra.ph/file/983b3e7642e0bbc93e97f.mp4",
            "https://te.legra.ph/file/752799e7cfe4c12674f9d.mp4",
            "https://te.legra.ph/file/c06735e58f46e4b168a58.mp4",
            "https://te.legra.ph/file/796f4f46789bfaf75f538.mp4",
            "https://te.legra.ph/file/2ca09922b7deb6a95bd9e.mp4",
            "https://te.legra.ph/file/42f621d1d2c541599022b.mp4",
            "https://te.legra.ph/file/00cf3356f99f53190e55c.mp4",
            "https://te.legra.ph/file/b2eb0c7dc7894e5504758.mp4",
            "https://te.legra.ph/file/10a572143677c2d1591d0.mp4",
            "https://te.legra.ph/file/1b9b014bab8597903a162.mp4",
            "https://telegra.ph//file/9ffdd1d11fea1018281f5.mp4",
            "https://te.legra.ph/file/121b33804ca9af0ed46c5.mp4",
            "https://te.legra.ph/file/d2d24ec985cd58576086b.mp4",
            "https://te.legra.ph/file/925c8224d61ed4600b125.mp4",
            "https://te.legra.ph/file/ae2ae3453e637b28f4b55.mp4",
            ]

SANJICOOK = [ 
            "https://te.legra.ph/file/5084545bd4543e57ea681.mp4",
            "https://te.legra.ph/file/329e7f36ac854293e7201.mp4",
            "https://te.legra.ph/file/5b50287df09c61fd5fffb.mp4",
            "https://te.legra.ph/file/2bbf4a9f88d85aa45b2c7.mp4",
            "https://te.legra.ph/file/2bbf4a9f88d85aa45b2c7.mp4",
            "https://te.legra.ph/file/227b1523e9ea120b44d81.mp4",
            "https://te.legra.ph/file/2c5ac738509512f44f08e.mp4",
            "https://te.legra.ph/file/a20efe95011d3583261a7.mp4",
            "https://te.legra.ph/file/1b56a94e483b007b61b65.mp4",
            "https://te.legra.ph/file/7c7a2d810364ff7ca71d5.mp4",
            "https://te.legra.ph/file/c15e75f042f6da1065201.mp4",
            "https://te.legra.ph/file/769b727429e638bc69283.mp4",
            "https://te.legra.ph/file/329e7f36ac854293e7201.mp4",
            "https://te.legra.ph/file/2bbf4a9f88d85aa45b2c7.mp4",
            "https://te.legra.ph/file/5b50287df09c61fd5fffb.mp4",
            "https://te.legra.ph/file/227b1523e9ea120b44d81.mp4",
            "https://te.legra.ph/file/2c5ac738509512f44f08e.mp4",
            "https://te.legra.ph/file/a20efe95011d3583261a7.mp4",
            "https://te.legra.ph/file/1b56a94e483b007b61b65.mp4",
            "https://te.legra.ph/file/dd2ca97497b0f5e8df649.mp4",
            "https://te.legra.ph/file/895dc34ff370525d4037a.mp4",
            "https://te.legra.ph/file/8dcc9142f817ce7ab9802.mp4",
            "https://te.legra.ph/file/41502257d907078b73980.mp4",
            "https://te.legra.ph/file/37c6ee5846454852f23e8.mp4",
            "https://te.legra.ph/file/c0fccb2b7082fe07a2681.mp4",
            "https://te.legra.ph/file/d76f11c309071c53e1f26.mp4",
            "https://te.legra.ph/file/8f8f91a1fba97a00b4fd2.mp4",
            "https://te.legra.ph/file/803dfb44b3b4653ef3726.mp4",
            "https://te.legra.ph/file/d7900b41e1a8efdc8ac9e.mp4",
            "https://te.legra.ph/file/8f9ba34a8e3ce94d90832.mp4",
            "https://te.legra.ph/file/763695c84b17dc4c918f4.mp4",
            "https://te.legra.ph/file/78e88bca2aaa7936618b0.mp4",
            "https://te.legra.ph/file/cc81eb7b87d80ef4b18d3.mp4",
            "https://te.legra.ph/file/0f977f88c9c16c11d3607.mp4",
            "https://te.legra.ph/file/cf8d6c13cf38e63e77d83.mp4",
            "https://te.legra.ph/file/cc81eb7b87d80ef4b18d3.mp4", 
            ]

COSPLAY = [
    "https://telegra.ph/file/0dee95b727f2028ac1856.jpg",
    "https://telegra.ph/file/c296eb3d7603a31062159.jpg",
    "https://telegra.ph/file/baddf7835b291a7fd3cfd.jpg",
    "https://telegra.ph/file/dfbf2aaa731e1cf00a2e1.jpg",
    "https://telegra.ph/file/893a0c47cec218d449965.jpg",
    "https://telegra.ph/file/5d46622a69d528737ddb9.jpg",
    "https://telegra.ph/file/7adf385229b0169c02e34.jpg",
    "https://telegra.ph/file/78ddf57462f7fa6c42ff1.jpg",
    "https://telegra.ph/file/5e599e2c0c4d3bf9788a1.jpg",
    "https://telegra.ph/file/d785a58fd84d381d79f34.jpg",
    "https://telegra.ph/file/38fafa65e89166410e71b.jpg",
    "https://telegra.ph/file/cc00468d7f06ca9be64ad.jpg",
    "https://telegra.ph/file/7f65dc3eb6938dcabe57c.jpg",
    "https://telegra.ph/file/60473963519194738eac2.jpg",
    "https://telegra.ph/file/268d07b949b32da7535de.jpg",
    "https://telegra.ph/file/89295d505cafa7de1e8a2.jpg",
    "https://telegra.ph/file/3f0490a35ae8823f0faca.jpg",
    "https://telegra.ph/file/7d580f55a513bdac0e30d.jpg",
    "https://telegra.ph/file/90b029ea381302c89aa39.jpg",
    "https://telegra.ph/file/b7340cfda5e369b03df17.jpg",
    "https://telegra.ph/file/40b6205209bbe052c30ed.jpg",
    "https://telegra.ph/file/d95c170a0bb42f28f55fa.jpg",
    "https://telegra.ph/file/3347ff752fc1e99ed4f97.jpg",
    "https://telegra.ph/file/0b286c405bf999f858850.jpg",
    "https://telegra.ph/file/1c1e990e233d6f90b0298.jpg",
    "https://telegra.ph/file/2dd5ba58116101260b6f8.jpg",
    "https://telegra.ph/file/dcc3e2ab8f918b72a7e06.jpg",
    "https://telegra.ph/file/743ef4bc34d7a944b1ba7.jpg",
    "https://telegra.ph/file/8f3461fecf62b8d11823a.jpg",
    "https://telegra.ph/file/896ac9ab7486537facd5f.jpg",
    "https://telegra.ph/file/44ae9d0e02bff35850316.jpg",
    "https://telegra.ph/file/6e220b68546b1102f748f.jpg",
    "https://telegra.ph/file/9cd29b3dfb18f7c5d6d40.jpg",
    "https://telegra.ph/file/e7d8c97856a2c52711a14.jpg",
    "https://telegra.ph/file/4c1be9254126c2398322f.jpg",
    "https://telegra.ph/file/68bac98751716c36509ce.jpg",
    "https://telegra.ph//file/11f026a07d8cd95f0ced6.jpg",
    "https://telegra.ph//file/d603640eeeb3d9f37ff4e.jpg",
    "https://telegra.ph//file/85e0ed8e0ff625d303e8e.jpg",
    "https://telegra.ph//file/06e1d0a2d62c0b3b4760d.jpg",
    "https://telegra.ph//file/b637cdc5e457297ccc206.jpg",
    "https://telegra.ph//file/ccdd98afc033cabef8591.jpg",
    "https://telegra.ph//file/b171e3727f28d23725b4d.jpg",
    "https://telegra.ph//file/1291fb8933738dbcc6018.jpg",
    "https://telegra.ph//file/e66f615f10835f91ff783.jpg",
    "https://telegra.ph//file/c9e594d9bce2c30dc63bf.jpg",
    "https://telegra.ph//file/dc08d5e2574c15abb3338.jpg",
    "https://telegra.ph//file/5e7c4126c269db03c885c.jpg",
    "https://telegra.ph//file/7ba45283c30e4bb66c636.jpg",
    "https://telegra.ph//file/0fc05fae810f6baa662cd.jpg",
    "https://telegra.ph//file/d408ded1b8472f11911b9.jpg",
    "https://telegra.ph//file/8b2d2df4b19ff9a020bb8.jpg",
    "https://telegra.ph//file/07a8d41b3b505caa53f73.jpg",
    "https://telegra.ph//file/43e256b4c354d3ab242a5.jpg",
    "https://telegra.ph//file/d580b83c553ed20080425.jpg",
    "https://telegra.ph//file/c23c06c8da66f444e13ca.jpg",
    "https://telegra.ph//file/83b09b0485852c1e06bb8.jpg",
    "https://telegra.ph//file/64624f754d2bffdca5ba5.jpg",
    "https://telegra.ph//file/d2368f4e76a71cf6aacf7.jpg",
    "https://telegra.ph//file/2c917e9f6df95ef9661ca.jpg",
    "https://telegra.ph//file/a1ff2f8d56db81a8bc754.jpg",
    "https://telegra.ph//file/efab5260882bb30275994.jpg",
    "https://telegra.ph//file/daacfeabd253292698540.jpg",
    "https://telegra.ph//file/4ad7968c7d663946edf30.jpg",
    "https://telegra.ph//file/8ac518bfca4a2d6c17ad6.jpg",
    "https://telegra.ph//file/b260b84c2f90baa0dd128.jpg",
    "https://telegra.ph//file/4dfd68c9a6c4c063d75c1.jpg",
    "https://telegra.ph/file/820b698c2798157fa38ec.jpg",
    "https://telegra.ph/file/83037eff8b8aefef1ddfb.jpg",
    "https://telegra.ph/file/b7d94d61cdcd17527754e.jpg",
    "https://telegra.ph//file/33114792da7df9de9db6a.jpg",
    "https://telegra.ph//file/c2d85563889ba08825a7a.jpg",
    "https://telegra.ph//file/fee5a61f6bbe66fab1ac7.jpg",
    "https://telegra.ph//file/a2bd89edc88eff5ad34cf.jpg",
    "https://telegra.ph//file/e4ed06b647336c80b7753.jpg",
    "https://telegra.ph//file/3f37b5953be988df13f31.jpg",
    "https://telegra.ph//file/e344873074e4893500087.jpg",
    "https://telegra.ph//file/5d824de15f12ea5831e91.jpg",
    "https://telegra.ph//file/4c6cd70adea2cef98fbb1.jpg",
    "https://telegra.ph//file/1be22fd6a7cc7665e250a.jpg",
    "https://telegra.ph//file/28ba3ca8b1fd6cb2a299b.jpg",
    "https://telegra.ph//file/084f743f0b8170ece820e.jpg",
    "https://telegra.ph//file/c61474cef0541c3a6b950.jpg",
    "https://telegra.ph//file/6d8d37665a0ef9b54950a.jpg",
    "https://telegra.ph//file/65dd65e69450debc3c08c.jpg",
    "https://telegra.ph//file/43fc6b9c874e935e67820.jpg",
    "https://telegra.ph//file/8b684ff2bacb034cd682a.jpg",
    "https://telegra.ph//file/503900dace6537cb196f2.jpg",
    "https://telegra.ph//file/50803efdea20699432ef3.jpg",
    "https://telegra.ph//file/fde9358effc727275ee58.jpg",
    "https://telegra.ph//file/ec4d04789590fda8206f4.jpg",
    "https://telegra.ph//file/a3e7b3152c79597ae4ff6.jpg",
    "https://telegra.ph//file/e6aa9c4669ae174dd8aaa.jpg",
    "https://telegra.ph//file/e2109bcc98bcddcc18e79.jpg",
    "https://telegra.ph//file/e236f950309ef1ac55cd6.jpg",
    "https://telegra.ph//file/9b7e5cfbd07e1b45ba2b0.jpg",
    "https://telegra.ph//file/085f9fc166c1b07db26f5.jpg",
    "https://telegra.ph//file/6a39dcba729e8c4bae719.jpg",
    "https://telegra.ph//file/ac2099f12c7032107946b.jpg",
    "https://telegra.ph//file/f63c22851825586d323ab.jpg",
    "https://telegra.ph//file/ac5d01bd3afc12db83e7d.jpg",
    "https://telegra.ph//file/be2185adced00fe08260a.jpg",
    "https://telegra.ph//file/e6cdf986aa23adc33f6fa.jpg",
    "https://telegra.ph//file/24c270c10f7f65cd547e7.jpg",
    "https://telegra.ph//file/680bfae0e8be2bd2089e6.jpg",
    "https://telegra.ph//file/af1495c0c93be27282aad.jpg",
    "https://telegra.ph//file/19e81b1b4f5fdc24a4768.jpg",
    "https://telegra.ph//file/46f54a23f7ad3858e3b11.jpg",
    "https://telegra.ph//file/a38b3bfda2140582662eb.jpg",
    "https://telegra.ph//file/a02a11dc20a17693f2495.jpg",
    "https://telegra.ph//file/e3d00224700070c460249.jpg",
    "https://telegra.ph//file/e4f97d46f8d3dc4045878.jpg",
    "https://telegra.ph//file/9c2c0da3a08b6afb245a7.jpg",
    "https://telegra.ph//file/4cb3b6a214762bf7d7e41.jpg",
    "https://telegra.ph//file/b71e03680361fdc9bbe40.jpg",
    "https://telegra.ph//file/e1667b1b7a8922d1243fa.jpg",
    "https://telegra.ph//file/3ecc88c49323b5888bc88.jpg",
    "https://telegra.ph//file/f8d8cae1d450ef6e676fd.jpg",
    "https://telegra.ph//file/c9d87cf151f303b7ce587.jpg",
    "https://telegra.ph//file/8b6a936e2582c38fa01fb.jpg",
    "https://telegra.ph//file/520a49a3d5256b3f95f1b.jpg",
    "https://telegra.ph//file/99c49239f28ef52f2da52.jpg",        
            ]

@app.get("/waifuvid")
def pnude():
    GIF = random.choice(WAIFUVID)
    return {"url" : GIF}

@app.get("/sanjicook")
def gnude():
    GIF = random.choice(SANJICOOK)
    return {"url" : GIF}

@app.get("/cosplay")
def lnude():
    GIF = random.choice(COSPLAY)
    return {"url" : GIF}
