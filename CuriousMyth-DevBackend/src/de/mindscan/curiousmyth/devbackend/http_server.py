'''
Created on 06.03.2022

MIT License

Copyright (c) 2019 Maxim Gansert

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

@author: Maxim Gansert, Mindscan
'''

from fastapi import FastAPI

app = FastAPI();

@app.get("/")
async def root():
    return {"message": "It works. Please go away now."}

@app.post("/entity/create")
async def create_entity():
    # an entity can be an event, an entity(corporation), a person, a collection of facts, a date, a timespan
    return {}

@app.get("/image/raw/{uuid}")
async def get_image_raw( uuid:str ):
    return {}

@app.get("/image/info/{uuid}")
async def get_image_info( uuid:str ):
    return {}

# TODO: upload_image