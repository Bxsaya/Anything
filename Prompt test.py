import numpy as np
import openai
import pandas as pd
import pickle
import tiktoken

COMPLETIONS_MODEL = "text-davinci-003"
EMBEDDING_MODEL = "text-embedding-ada-002"

prompt = "Where can we find pilau in Diani??"

openai.Completion.create(
    prompt=prompt,
    temperature=0,
    max_tokens=300,
    model=COMPLETIONS_MODEL
)["choices"][0]["text"].strip(" \n")