import requests
url = "https://rainbow-f2f31-default-rtdb.asia-southeast1.firebasedatabase.app/rainbow.json"
#url = "https://earbuzz.vercel.app/"
res = requests.get(url)

data = res.json()
data = data["product"]
def db():
    return data

def itemdata(id):
    return data[id]
    return data[0]
