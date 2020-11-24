# JSON Web API app for METAR
This Project is focused on the retrival of the data in JSON format from the metar website.

## Installation
```bash
	pip install -r requirements.txt
```
Install Redis in the system.


## Steps
1. Create a Virtual Environment
```bash
	python -m venv venv
```
2. Run installations after activating the virtual environmnet.To activate venv
```bash
	source venv/Scripts/activate
```
3. Run the App
This runs the app on server on port 8000 by default.
```bash
	python manage.py runserver
```
4. Navigate to App

i. This runs the demo method.
```bash
	localhost:8000/metar/ping
```

ii. This runs and requests the app to respond the 'GET' request
```bash
	localhost:8000/metar/info?scode=KSGS
```
The parameter scode here is the station code. The data is extracted as the scode is sent as request to the method. If the 'scode' is as a id in cache the data is retrieved from the cache. If the 'scode' is not in the cache the data is retrieved from the website which is live. 

iii. Adding to the above request, The nocache parameter is used to reload from the website as the request 
```bash
	localhost:8000/metar/info?scode=KSGS&nocache=1
```
The nocache parameter here is used to request the data from the live website irrespective of the presence of the data in cache. This also allows the data present in the cache to refresh and set the new values for the id.

*Note: I have created this project on the windows 10. Please download the compatible redis software.