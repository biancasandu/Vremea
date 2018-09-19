import requests

city= raw_input("Enter the city name: ")
city= city.title()
url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=21ff405208e1a89176374d0517de0ef7&units=metric".format(city)
info=requests.get(url)
read=info.json()
while True:
    try:
        print "City name:{}".format(read['name'])
        print "Temperature:{}C".format(read['main']['temp'])
        print "Humidity:{}".format(read['main']['humidity'])
        break
    except KeyError:
        print "That city does not exist in our database "
        break