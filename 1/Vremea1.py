import requests

city= raw_input("Enter the city name: ")
url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=21ff405208e1a89176374d0517de0ef7&units=metric".format(city)
info=requests.get(url)
read=info.json()
print "City name:{}".format(read['name'])
print "Temperature:{}C".format(read['main']['temp'])
print "Humidity:{}".format(read['main']['humidity'])