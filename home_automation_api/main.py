from fastapi import FastAPI
from device_service import DeviceService

app = FastAPI()
device = DeviceService()


@app.get("/")
def root():
    return {"message": "Home Automation API Running"}


@app.post("/light/on")
def light_on():
    return {"status": device.light_on()}


@app.post("/light/off")
def light_off():
    return {"status": device.light_off()}


if __name__ == "__main__":
    # Local development sys.path fix (lint ignore)
    import sys, os
    sys.path.append(os.path.dirname(__file__))
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
