from fastapi import FastAPI
import uvicorn
import numexpr

app = FastAPI()

@app.get("/sum")
async def sum(a: int = 0, b: int = 0):
    return a + b

@app.get("/sub")
async def sub(a: int = 0, b: int = 0):
    return a - b

@app.get("/div")
async def div(a: int = 0, b: int = 0):
    return a / b

@app.get("/mult")
async def div(a: int = 0, b: int = 0):
    return a * b

@app.get("/calculate")
async def calculate(expression: str):
    return {"result": numexpr.evaluate(expression).item()}

if __name__ == "__main__":
    uvicorn.run("lab1:app", reload=True)