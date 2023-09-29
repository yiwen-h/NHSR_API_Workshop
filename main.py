from fastapi import FastAPI

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'ok': True}

# Adding endpoints
# @app.get('/potatoes')
# def potatoes():
#     return {'Ways to cook': ['Boil em', 'Mash em', 'Stick em in a stew']}

# @app.get('/hello')
# def hello(name):
#     return {'Obi-wan says':f'Hello there, {name}'}

# Coding together!
# @app.get('/simple_calc')
# def calc(num1, num2):
#     pass
