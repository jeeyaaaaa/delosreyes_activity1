from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/factorial/{starting_number}")
async def compute_factorial(starting_number: int):
    if starting_number < 0:
        raise HTTPException(status_code=400, detail="Input must be a non-negative integer")
    
    if starting_number == 0:
        return {"result": False}
    
    factorial = 1
    count = starting_number
    
    while count > 1:
        factorial *= count
        count -= 1
    
    return {"result": factorial}
