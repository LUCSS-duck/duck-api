from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.requests import HTTPConnection

app = Starlette()

@app.route("/forward")
async def forward(request: HTTPConnection):
    print("go forward (eventually)")
    return JSONResponse({"moving": "forward"})

@app.route("/backward")
async def backward(request: HTTPConnection):
    print("go backward (eventually)")
    return JSONResponse({"moving": "backward"})
