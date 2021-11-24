import os, io
from flask import Flask, request, url_for, render_template, send_file, redirect

app = Flask(__name__)

def generatePage(name, images):
  string = "<html><head><title>"+name+"</title></head><body>"
  for i in range(0,len(images)):
    p = os.path.join(os.getcwd(), 'static',  name + str(i) + '.png')
    with open(p,'wb') as ifile:
      ifile.write(images[i].read())
    img = url_for('static', filename=name+str(i)+'.png')
    string += "<img src=\""+img+"\"><br>"
  string += "</body></html>"
  return(string)

@app.route("/")
def hello():
  string = "<form method=\"POST\"><input name=\"text\"><input type=\"submit\"></form>"
  return(string)

@app.route("/", methods=['POST'])
def search():
  return redirect(url_for('say_hello', name = request.form['text']))

@app.route("/<string:name>/")
def say_hello(name):
  return name

if __name__ == "__main__":
  app.run()
