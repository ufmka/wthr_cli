import requests

city = input("напиши свой город на английском: ")
a = requests.get(f"https://wttr.in/{city}?format=2")

if a.status_code == 200:
    print("найдено!")
    print(a.text)

elif a.status_code == 404:
    print("not found")

else:
    print("not work")