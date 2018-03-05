#pip install pygeoip
#https://dev.maxmind.com/geoip/legacy/geolite/




import pygeoip
import re


ip_name = "input_IP_Data.txt"
geo_location_file = "geo_data_all.txt"
g = pygeoip.GeoIP('GeoLiteCity.dat')


with open(ip_name, 'r') as f, open(geo_location_file, 'w') as n:
    for line in f:
        ip = re.sub('[^a-zA-Z0-9_. ]+', '', line)
        #print ip
        n.write(str(g.record_by_addr(ip)))
        n.write('\n')


