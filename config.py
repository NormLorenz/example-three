import os

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Set your OpenAI API key here
    DEBUG = True  # Set to False in production
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # Change this to a random secret key for production