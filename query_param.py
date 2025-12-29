from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import Optional

app = FastAPI()

# HTML Response
@app.get("/add-html", response_class=HTMLResponse)
def add_numbers_html(num1: int, num2: int):
    return f"""
    <h2>Addition Result</h2>
    <p>{num1} + {num2} = <b>{num1 + num2}</b></p>
    """

# http://127.0.0.1:8000/add-html?num1=10&num2=30

# Defalut values
@app.get("/add-default")
def add(n1: int = 10, n2: int= 20):
    return n1+n2

# http://127.0.0.1:8000/add-default?n1=100&n2=200

@app.get("/add-optional")
def add_optional(n1: Optional[int] = 100, n2: Optional[int] = 200):
    return n1 + n2
# http://127.0.0.1:8000/add-optional  --> 300
# http://127.0.0.1:8000/add-optional?n1=500  --> 700
# http://127.0.0.1:8000/add-optional?n1=200&n2=700  --> 900



