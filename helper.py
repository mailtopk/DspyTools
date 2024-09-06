import dspy
import os
from dotenv import load_dotenv

load_dotenv()

def lm():
    OPEN_API_KEY = os.getenv("OPEN_API_KEY")
    gpt_4o = dspy.OpenAI(model="gpt-4o", api_key=OPEN_API_KEY)
    return gpt_4o
