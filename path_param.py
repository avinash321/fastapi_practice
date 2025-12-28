from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Single Param
@app.get("/{name}", response_class=HTMLResponse)
def home(name: str):
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Simple FastAPI Page</title>
        </head>
        <body>
            <h1>Hello {name} 👋</h1>
            <p>This is a simple HTML page served directly from FastAPI.</p>
        </body>
    </html>
    """


# Multiple Params with html response
@app.get("/add/{num1}/{num2}", response_class=HTMLResponse)
def add_two_nums(num1: int, num2: int):
    result = num1 + num2

    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Addition Result</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 50px;
                }}
                .box {{
                    border: 1px solid #ccc;
                    display: inline-block;
                    padding: 20px 30px;
                    border-radius: 8px;
                }}
            </style>
        </head>
        <body>
            <div class="box">
                <h2>Addition Result</h2>
                <p>{num1} + {num2} = <b>{result}</b></p>
            </div>
        </body>
    </html>
    """

# Three Consecutive params
@app.get("/add_three_nums/{num1}/{num2}/{num3}")
def add_two_nums(num1: int, num2: int, num3: int):
    return num1 + num2 + num3

# Params with in hard paths
@app.get("/add_nums/{num1}/{num2}/test/{num3}")
def add_two_nums(num1: int, num2: int, num3: int):
    return num1 + num2 + num3

