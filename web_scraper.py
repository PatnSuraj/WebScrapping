from bs4 import BeautifulSoup
import requests

# importing warnigs to ignore the depriciate warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

web_page = requests.get("https://weather.gc.ca/canada_e.html")
doc = BeautifulSoup( web_page.text, "html.parser")

# finding the table and its class for retrieving the content
table_content = doc.find('table', attrs={"class":'table table-hover table-striped table-condensed'})
weatherData = ""

# nested for loop to go through the tr and extract td elements from the web page.
for trs in table_content.find_all("tr"):
    tds = trs.find_all("td")
    for col in tds:
        # condition to get only the required cities.
        if (tds[0].text == "Calgary" or tds[0].text == "Halifax" or tds[0].text == "Montréal" or tds[0].text == "Toronto" or tds[0].text == "Vancouver"):
            res = ("City: "+tds[0].text+" Temperature:"+tds[2].text)
            if res not in weatherData:
                weatherData+=(res+"\n")

# Printing the temperature of the city in degree Celcius
print(weatherData)


# Reading and writing the extracted data to the "Weather.txt" file
with open("Weather.txt", "w") as fileWriter:
    fileWriter.write(weatherData)

with open("Weather.txt","r") as fileReader:
    fileReader.read()
