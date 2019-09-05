import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/weather-forecast/<service>/<location>/<units>')
def get_weather_info( service, location,units):

     service_url = get_service_url(service)

     if service_url is None or not service_url:
         return "error: service not provided"
     else:

         resp = requests.get(service_url+'/'+location+'/'+units)
         #resp =requests.get(service_url,params={location:location,units:units})

         if resp.status_code != 200:
             ##TODO; add the cache strategy
            return "error"
         else:
            return resp.json()



def get_service_url( service):
    switcher ={
        "openmap": "http://localhost:5001/openmap",
        "darksky": "http://localhost:5002/darksky/"
    }
    return switcher.get(service, "")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)