from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time
import csv

csvfile = open("radio_station10.csv", 'w', newline='', encoding='utf-8')
c = csv.writer(csvfile)
c.writerow(['name', 'followers', 'genres', 'location'])


westpalm = "radio/West-Palm-Beach-Boca-Raton-r100047/"
orlando  = "radio/Orlando-r100038/"
miami =    "radio/Miami-Ft-Lauderdale-Hollywood-r100012/"
area_url = []
stations = []
cities = [westpalm, orlando, miami]
radio_stations = []


url_root = 'http://tunein.com/'

def get_area_urls(cities):
    for city in cities:
        offset_num = 0
        offset_str = str(offset_num)
        while offset_num < 106:
            # regex string "(?<=-r)(.)*(?=\/)" )  - it says, start: -r, end: /, get the middle
            result = re.search( "(?<=-r)(.)*(?=\/)" , city )
            city_rnum = str( result.group() )
            # print(city_rnum) # this will print only 3 numbers, 1 per city
            string = url_root + city + "?id=r" + city_rnum + "&page=true&filter=!p%3a!e&offset=" + offset_str
            # instead of printing, you would save the URLs to a list
            #print(string)
            area_url.append(string)
            offset_num += 7
            offset_str = str(offset_num)

get_area_urls(cities)

#--------------------------------------------------------

def get_stations(area_url):
    for url in area_url:
        new_url = url
        html = urlopen(url)
        bsObj = BeautifulSoup(html, "html.parser")
        tag_list = bsObj.findAll( "a", {"class":"_tooltip overlay-hover-trigger clearfix"} )
        for tag in tag_list:
            if 'href' in tag.attrs:
                stations.append(str(tag.attrs['href']))
            
        
get_stations(area_url)


def get_details(stations):
    for detail in stations:
        new_url2 = "http://tunein.com" + detail
        html = urlopen(new_url2)
        bsObj = BeautifulSoup(html, "html.parser")
        info_list = bsObj.find( "div", {"class": 'info clearfix'}).findAll('h1')
        for info in info_list:
             name = info.get_text() 
             #print (info.get_text())
        
             
        time.sleep(2)
        followers = bsObj.find('li', {'class': 'followed-by fl-l'}).findAll( "div", {"class": 'count'})
        for list in followers: 
             follow = list.get_text()
             #print (list.get_text())
        
        time.sleep(2)
             
        
        try: 
            genres = bsObj.find('li', {'class': 'dark-link'}).findAll('a')
            for type in genres: 
                #print (type.get_text())
                music = type.get_text()
            
                
        except:
            #print ( "None" )
            music = 'None'
            
        
        time.sleep(2)
        location = bsObj.findAll('span', {'itemprop': 'contentLocation'})
        for place in location:
             where = place.get_text()
             #print (place.get_text())
       
        time.sleep(2)
       
        
        radio_stations = [name, follow, music, where]
        row = []
            
            
        
        for stuff in radio_stations: 
                row.append(stuff)
                
        
                
    
        c.writerow(row)    
        time.sleep(1)
        
get_details(stations)
csvfile.close()



