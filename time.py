import urllib.request
import json
import codecs
import sys


def getTime(lng,lat):

    api ="http://www.earthtools.org/timezone/"+lng+"/"+lat
    response =str(urllib.request.urlopen(api).read())
    first = response.find("<localtime>", 0)
    last = response.find("</localtime>", 0)
    localtime = response[first:last].replace("<localtime>", "")
    print("  Local Time = " + localtime)
    print("---------------------------------------")
    print("\n")
    print("\n")

    return localtime

def getlonglat(query):
    query=query.replace(" ", "+")
    api = "http://maps.googleapis.com/maps/api/geocode/json?address="+query+"&sensor=false"
    response = urllib.request.urlopen(api)

    reader = codecs.getreader("utf-8")
    obj = json.load(reader(response))

    latlng = obj["results"][0]["geometry"]["location"]
    print("\n")
    print("\n")
    print("---------------------------------------")
    print("  Adress     = "+ obj["results"][0]["formatted_address"])
    print("---------------------------------------")

    return latlng


def main():
    if len(sys.argv) == 1:
        print("Usage time.py [Query]")
    elif sys.argv is None:
        print("Hello Time.py You can learn times of region this py.")
        print("Usage time.py [Query]")
    else :
        query = ""


        for i in sys.argv:
            query=query+i


        query = query.replace(sys.argv[0],"").replace("ö","o").replace("ü","u").replace("ı","i").replace("ş","s").replace("ğ","g").replace("ç","c")

        try:
            obj = getlonglat(query)
            lng = str(obj["lng"])
            lat = str(obj["lat"])

            print("  Longitude  = " + lng)
            print("  latitude   = "+lat)
            print("---------------------------------------")

            getTime(lng, lat)
        except Exception :
            print("\n")
            print("---------------------------------------")
            print("  City or state not found")
            print("---------------------------------------")
            print("\n")
            exit(0)

if __name__ == '__main__':
    main()








