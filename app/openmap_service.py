import json
import pytest
from datetime import date
import requests
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/openmap/<location>/<units>')
def get_openmap(location,units):
    resp = requests.get(f'http://api.openweathermap.org/data/2.5/find?q={location}&units={units}&cnt=7&appid=dc94948d58feeb8dda8f18093f22bd6d')
    if resp.status_code != 200:
        return "error"
    else:
        week_forecast= resp.json()
        city = week_forecast['list'][0]['name']
        dayList =[]
        i=0;
        for element in week_forecast['list']:
          day= i
          temperature = element['main']['temp']
          day_dict = {"day":day,"temperature":temperature}
          dayList.append(day_dict)
          i=i+1

        message = { "city" : city, "query_date": date.today().strftime("%d/%m/%Y"),"service":"openmap","forecast": dayList }

        return json.dumps(message)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)


def test_get_openmap():
    assert isinstance(get_openmap('London','metric'), str)

def test_get_openmap_valid():
      content = get_openmap('London','metric')
      json_content = json.loads(content)
      assert  json_content
