"""FastAPI tutorial

In this tutorial I will learn how to use fastapi forms

"""

from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/language/")
async def language(name: str = Form(...), type: str = Form(...)):
    return {'name': name, "type": type}



