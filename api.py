from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from starlette.middleware.cors import CORSMiddleware
#from pydantic import BaseModel

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    #allow_credentials=False,
    #allow_methods=["*"],
    allow_headers=['*'],
)

@app.get('/api/v1/about')
async def about() -> dict:
    return {'slackusername': "Musawakiliml",
            'backend': True,
            'age': 26,
            'bio': "Hey, there i am an aspiring Machine Learning Engineer. A Python Developer with a zeal to become a grey haired programmer."}
