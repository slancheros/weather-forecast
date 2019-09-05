# weather-forecast
weather forecast service aggregation

The main idea was to have a central service written in python, acting as a gateway for the weather services. 

1. Main service running in 5000 port
2. openmap service running in port 5001 port
3. darksky(forecast.io) running in port 5002 port.


The main service uses a switcher to redirect to the right service.

The strategy to  implement a circuit breaker ( not implemented);
1. When the service requested is up, the retrieved information is sent to kafka.
2. When the service requested is down, the data from the date, and service was retrieved from kafka topic and date requested, instead.

For making it transparent and integrated in terms of message, the standard format of the weather information was like this:

{"city": "London", "query_date": "05/09/2019", "service": "openmap", "forecast": [{"day": 0, "temperature": 11.81}, {"day": 1, "temperature": 9.38}, {"day": 2, "temperature": 21.04}, {"day": 3, "temperature": 16.15}, {"day": 4, "temperature": 23.35}, {"day": 5, "temperature": 9.25}, {"day": 6, "temperature": 25.04}, {"day": 7, "temperature": 13.78}]}

The service from the central perspective received the following parameters:

1. service (openmap/darksky)
2.location ( city name)
3.units ( metric = °C / imperial = °F )

http://localhost:5000/weather-forecast/openmap/London/metric goes is an example of the call for main service, redirecting to openmap.
http://localhost:5001/openmap/London/imperial  to invoke directly the openmap service.
http://localhost:5002/darksky/London/imperial  to invoce directly the darksky service.


The only working one is openmap, and I was about to work with darksky, however it was cumbersome to check the daily structure to fit on the defined message. Same work to be performed by each forecast service: to unify according to the service contract described above.

The planned UI was Vue.js connected to the Python backend, sending the mentioned parameters above (not delivered)

Very basic test cases implemnted with pytest.

Containerization:  not completed. There were adjustments on libraries needed to perform.

The idea was to have a container running the python app for each service and a container running kafka.



