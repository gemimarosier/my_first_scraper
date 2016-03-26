# My very first scraper: Radio Stations

The purpose of this scraper is to get the information on radio stations of 3 major areas in Florida. I wanted to get the name of the radio station, the number of followers, the genre of music and where the station is located. 

First I had to construct the urls of the area pages of Orlando, West Palm Beach, and Miami with the function ***get_area_urls***. Then I scraped the urls of the individual station pages using the function ***get_stations***. With these scraped, I was able to use the function ***get_details*** to get the name, number of followers, genre and location of each radio station. 

I ran into a few problems: 

(1) The area pages contained all the links to the stations in a table that only showed 7 links at a time. When a user clicks to see more stations, the urls do not change. For a solution, I was guided to construct new urls from the HTML that gave me access to the all the stations!

(2) Some of the radio stations did not have a genre, so my script would throw an error and stop running. I was guided to insert an try/except statement to tell my script to write in 'None' if a genre category was not there. 

(3) When trying to store my data into a csv, I would either see the data wrapped in tags or 'None' written into all the cells. After a long session of trial and error, I found a solution!! For every detail I scraped, I stored the findings on a variable. Then I stored all the variables in a list radio_stations. Next, I created an empty array. Then, I  looped the items to populate row. Row was then written into the csv file-- with no tags attached! 