from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Simple FastAPI Page</title>
        </head>
        <body>
            <h1>Hello Avinash 👋</h1>
            <p>This is a simple HTML page served directly from FastAPI.</p>
        </body>
    </html>
    """
