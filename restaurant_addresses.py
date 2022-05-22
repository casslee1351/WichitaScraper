import webbrowser
import requests
import bs4

#webbrowser.open("https://www.google.com/search?q=vietnomnom", new=1)
r = requests.get("https://www.google.com/search?q=pho+cuong")
r.raise_for_status()

soup = bs4.BeautifulSoup(r.text, "html.parser")

spans = soup.find_all("span")
addr = soup.find("span", class_="BNeawe tAd8D AP7Wnd")
print(addr.text)
