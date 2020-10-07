import requests
url="https://www.google.com/search?q=hello+world&oq=hello+wo&aqs=chrome.1.69i57j0l7.7251j1j15&sourceid=chrome&ie=UTF-8"
sh_url=requests.get(f"https://da.gd/s?url={url}").text
print (sh_url)
