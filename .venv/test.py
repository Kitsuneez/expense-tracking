import requests

for i in range(497,0,-1):
    r = requests.get(f"https://thefappening.plus/photos/e/v/evawishx-1/1000/evawishx-1_0{i}_s.jpg").content
    with open(f"images/{i}.jpg", 'wb') as handler:
        handler.write(r)
    # print(i)
# raw = r.text
# print(raw)
# n=497
#https://thefappening.plus/photos/e/v/evawishx-1/1000/evawishx-1_0497_s.jpg