import requests

#simple api app that checks your location's coordinates

def locate_me():

    
    city= raw_input("Enter your country:")
    country= raw_input("Enter your City:")

    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + city+ ',+' + country + '&key=AIzaSyDlkTiZbPLeE6hCsUT8hvFyhDEotUwqrv4'
    maps_response = requests.get(url)
    maps_data = maps_response.json()

    latitude = maps_data['results'][0]['geometry']['location']['lat']
    longitude = maps_data['results'][0]['geometry']['location']['lng']

    print ("your location is latitude %s and longitude %s" %(latitude,longitude))
    
   


   


