from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get('/api/v1/about')
async def about() -> dict:
    return {'slackusername': "Musawakiliml",
            'backend': True,
            'age': 26,
            'bio': "Hey, there i am an aspiring Machine Learning Engineer. A Python Developer with a zeal to become a grey haired programmer."}
