from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Yeah. I survive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def host():
    t = Thread(target=run)
    t.start()
