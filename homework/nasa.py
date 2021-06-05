import requests
def get_today():
  response = requests.get("https://api.nasa.gov/planetary/apod",
                          params={"api_key": "DEMO_KEY", "date": "2020-11-18"})
  print(response)
  #get the content/data
  content = response.json()
  #get the title of the day
  title = content["title"]
  print(title)
get_today()
def get_month():
  i = 1
  while i < 30:
    date = "2020-10-" + str(i)
    response = requests.get("https://api.nasa.gov/planetary/apod",
                            params={"api_key": "DEMO_KEY", "date": date})
    print(response.json()["title"])
    i += 1
get_month()

# nu ne mai lasa dupa cateva incercari sa rulam codul deoarece e demo mode