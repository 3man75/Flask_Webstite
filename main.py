import shutil
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import requests
import json
import urllib


app = Flask(__name__)

#create flask aplication called app
def create_app():

    print(app)

    return returned_dict

#first page of our website
@app.route("/")
def hello():
    return render_template('dogs.html')

@app.route("/images", methods=["GET","POST"])
def get_dog_images():

    #url for the dog API
    URL_Request = requests.get('https://dog.ceo/api/breeds/image/random')
    
    print(URL_Request)

    dog_image = Image.open(urllib.request.urlopen(image_URL))
    
    dog_image = image.resize((300,300))
    
    dog_image.save('static/dog/jpg')

    return render_template('wbs.html')
     
if __name__ == '__main__':

    get_dog_images()

    app.run(host="0.0.0.0")
    
