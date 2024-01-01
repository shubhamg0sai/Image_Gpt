import openai
import os
from PIL import Image
from apikey import api_data
import urllib.request

prompt = " "

def imgai(query):
    openai.api_key = api_data
    global prompt
    prompt=f'sir: {query}\n '
    print(prompt)
    response=openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    urllib.request.urlretrieve(image_url, "image.png")
    return image_url
