import requests
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	key = "ec9a7d1d89e7dae8f87414c672318cf8"
	city = 'Jaipur'
	url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
	data = requests.get(url).json()
	cente = data['main']['temp']-273  # Jaipur
	description = data['weather'][0]['description'].title()  ## Description
	icon = data['weather'][0]['icon']  # icon
	humidity = data['main']['humidity']   # humidity
	country = data['sys']['country']    #country
	atmos_pressure = data['main']['pressure']  ##Atmospheric pressure
	cloudiness = data['clouds']['all']  ## Cloudiness, %
	dateTime = datetime.fromtimestamp(data['dt'])  # dateTime
	if request.method == 'POST':
		city = request.form.get('city').title()
		key = "ec9a7d1d89e7dae8f87414c672318cf8"
		url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
		data = requests.get(url).json()
		cente = data['main']['temp']-273  # Jaipur
		description = data['weather'][0]['description'].title()  ## Description
		icon = data['weather'][0]['icon']  # icon
		humidity = data['main']['humidity']   # humidity
		country = data['sys']['country']    #country
		atmos_pressure = data['main']['pressure']  ##Atmospheric pressure
		cloudiness = data['clouds']['all']  ## Cloudiness, %
		dateTime = datetime.fromtimestamp(data['dt'])  # dateTime


	weather = {
            'city' : city,
            'temp': round(cente),
            'description': description,
            'icon':icon,
            'humidity':humidity,
            'country':country,
            'atmos_pressure':atmos_pressure,
            'cloudiness':cloudiness,
            'dateTime':dateTime
        }

	return render_template('index.html', weather=weather)
	
	
	
if __name__ == "__main__" : 

	app.run("localhost",8088,debug=True)
