from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.requests import HTTPConnection
from dataclasses import dataclass
# import motorcontrol # Motor control functions - unrelated to my dev branch

app = Starlette()

@app.route("/forward")
async def forward(request: HTTPConnection):
    print("go forward (eventually)")
    return JSONResponse({"moving": "forward"})

@app.route("/backward")
async def backward(request: HTTPConnection):
    print("go backward (eventually)")
    return JSONResponse({"moving": "backward"})

@dataclass
class movement:
    waitTime: int

    def init(self, func):
        func()
        return True
    
    def finish(self):
        # motorcontrol.stop()
        return True