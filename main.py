import random
import requests
import httpx
from fastapi import FastAPI , Request

app = FastAPI()

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

@app.get("/waifuvid")
def pnude():
    GIF = random.choice(WAIFUVID)
    return {"url" : GIF}

@app.get("/sanjicook")
def gnude():
    GIF = random.choice(SANJICOOK)
    return {"url" : GIF}

@app.get("/gif")
async def tenor(request: Request, q: str = None):
    alpha = request.query_params.get('q', '')
    api_key = "AIzaSyDLY6gywwY_MswUJDdwe_BjtBvE2JZhpMA"
    lmt = 50
    ckey = "alpha_coder"
    url = f"https://tenor.googleapis.com/v2/search?q={alpha}&key={api_key}&client_key={ckey}&limit={lmt}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            gif_url = data['results'][0]['media_formats']['tinygif']['url']
            return {'gif_url': gif_url}
        else:
            return {'error': 'Failed to fetch the GIF URL.'}
