
# WEB SCRAPING

For web scraping we are using the popular python library Beautiful Soup. 

First, the web scraper will be given one or more URLs to load before scraping.
The scraper then loads the entire HTML code for the page in question. 
Then it will either extract all the data on the page or specific data selected before the project is run.
Ideally, we will go through the process of selecting the specific data we want from the page. For example, in our case, the important data in the webpage is the private equity news. So we will precise in the code that we only want the news section. 
Lastly, the web scraper will output all the data that has been collected into a text format. Most web scrapers will output data to a CSV or Excel spreadsheet, however for me I wanted them in a .txt format. 
This code has the ability to scrap the webpage for a specific date given by the users, or it can scrap the news in a period of time, for example, two months. It will save all the articles in the specific folder related to the website that they have been scraped from. 



## Libraries

`Beautifulsoup`

`requests`
