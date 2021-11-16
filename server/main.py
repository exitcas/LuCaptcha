#!/usr/bin/env python
from captcha.image import ImageCaptcha
from random import *
#import os
from flask import Flask, jsonify, render_template, request, send_from_directory
app = Flask("LuCaptcha", template_folder="website")
image = ImageCaptcha(fonts=["fonts/bebas_neue/BebasNeue-Regular.otf", "fonts/poppins/Poppins-Regular.otf"])
chars = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    ":", ",", "-"
]

@app.route("/api")
def api():
  base_url = request.base_url
  url = base_url.replace("api", "static/")
  text = chars[randint(0, 64)] + chars[randint(0, 64)] + chars[randint(0, 64)] + chars[randint(0, 64)] + chars[randint(0, 64)]
  image_name = str(randint(0, 9999999999999))
  json_name = str(randint(0, 9999999999999))
  image.write(text, "static/" + image_name + ".png")
  json = open("static/" + json_name + ".json", "w+")
  json.write('{"permanent_url":"'+url+json_name+'.json","text":"'+str(text)+'","url":"'+url+str(image_name)+'.png"}')
  return jsonify({"permanent_url": f"{url}{json_name}.json", "text": str(text), "url": f"{url}{str(image_name)}.png"})

@app.route("/")
def rindex():
  return '<meta http-equiv="refresh" content="0;url=/w">'
@app.route("/w")
def index():
  return render_template("index.html")
@app.route("/w/")
def iindex():
  return render_template("index.html")

@app.route("/w/<path:asdf>")
def web_files(asdf):
  return send_from_directory('w', asdf)

if __name__ == "__main__":
  client = app.run(debug=False, host="0.0.0.0", port="5000")
