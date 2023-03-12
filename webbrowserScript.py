import webbrowser

import requests as requests

if __name__ == '__main__':
 pageurl = input("Podaj stronę internetową: ")
 for x in range(3):
  date = input("Podaj date: ")
  url = "http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date)
  response = requests.get(url)
  d = response.json()
  page = d["archived_snapshots"]["closest"]["url"]
  webbrowser.open(page)
print("Program zakonczyl petle")