import requests

x = requests.post('https://w3schools.com/python/demopage.htm')
#x = requests.get("https://www.youtube.com")

f = open("myfile.html", "x")
f = open("myfile.html", "w")
f.write(x.text)
f.close()