from __init__ import *
from langfuse.decorators import observe
from langfuse.openai import openai # OpenAI integration
 
@observe()
def story():
    return openai.chat.completions.create(
        model="Qwen/Qwen1.5-72B-Chat",
        max_tokens=100,
        messages=[
          {"role": "system", "content": "You are a great storyteller."},
          {"role": "user", "content": "Once upon a time in a galaxy far, far away..."}
        ],
    ).choices[0].message.content
 
@observe()
def main():
    return story()
 
main()