import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def read_func(filename):
    with open(filename, "r") as f:
        return f.read()

def summarize(text):
    prompt=f"""
    You are a smart agent which organises tasks, given a task list, categorize them into 3 tasks:
        - High priority
        - Medium priority
        - Low priority
    tasks: {text}
    Return response in this format: 
    High priority
        - task 1
        - task 2
    Medium Priority
        - task 1
        - task 2
    Low priority
        - task 1
        - task 2
"""

    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=prompt
    )
    print(response.text)

if __name__=="__main__":
    tasks=read_func("tasks.txt")
    summarize(tasks)