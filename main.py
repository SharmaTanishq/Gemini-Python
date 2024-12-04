# from fastapi import FastAPI
# from dotenv import load_dotenv
# from pydantic import BaseModel
# from openai import OpenAI
# import google.generativeai as genai

# import os

# load_dotenv()
# app = FastAPI()

# genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# client = OpenAI(
#     api_key=os.environ.get("API_KEY"),  # This is the default and can be omitted
# )

# class Prompt(BaseModel):
#     prompt: str

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# @app.post("/generate")
# def generate_text(prompt: Prompt):
#     model = genai.GenerativeModel("gemini-1.5-flash")
#     response = model.generate_content(prompt.prompt)    
#     return {"generated_text": response.text}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}