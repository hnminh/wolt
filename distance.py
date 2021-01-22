import math

def degreeToRadian(degree):
    return degree*(math.pi/180)

# using haversine formula to calculate distance between 2 points
# more information can be found through this link
# http://www.movable-type.co.uk/scripts/latlong.html
def getDistanceFromLatLonInKm(lat1, lon1, lat2, lon2):
    earthRadius = 6371  # radius of the earth in km
    radLat1 = degreeToRadian(lat1)
    radLat2 = degreeToRadian(lat2)
    deltaLat = degreeToRadian(lat2 - lat1)
    deltaLon = degreeToRadian(lon2 - lon1)

    a = math.sin(deltaLat/2)**2 + math.cos(radLat1)*math.cos(radLat2)*(math.sin(deltaLon/2)**2)
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = earthRadius*c

    return d