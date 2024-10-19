import requests
category = ["men", "product"]
url = f"https://rainbow-f2f31-default-rtdb.asia-southeast1.firebasedatabase.app/rainbow/{
    category[0]}.json"
# url = "https://earbuzz.vercel.app/"
res = requests.get(url)
firebase = res.json()
size = len(firebase)


def savedata():


    data = {

    "buy_price": 950,
    "details": {
        " cat": "saree",
        "colour": "Dark Green",
        "details": "details for the 0th prod Pure Katan Silk Mayura Border Super Soft & Premium Quality Gurranted Party Wear & Gloshy Collection All Total Dual Tone Colour Set 🍁With Banarasi Border Blouse Piece",
        "shipping": 120,
        "size": "none",
        "status": "in stock"
    },
    "image": "https://i.ibb.co/jvBDHSw/Whats-App-Image-2024-09-08-at-6-57-04-PM.jpg",
    "image1": "https://i.ibb.co/yRqCBHr/Whats-App-Image-2024-09-08-at-6-57-13-PM.jpg",
    "image2": "https://i.ibb.co/hx68RMZ/Whats-App-Image-2024-09-08-at-6-57-17-PM.jpg",
    "image3": "https://i.ibb.co/NtZmc1C/Whats-App-Image-2024-09-08-at-6-57-14-PM.jpg",
    "image4": "https://i.ibb.co/jvBDHSw/Whats-App-Image-2024-09-08-at-6-57-04-PM.jpg",
    "images": [
        "https://i.ibb.co/jvBDHSw/Whats-App-Image-2024-09-08-at-6-57-04-PM.jpg",
        "https://i.ibb.co/yRqCBHr/Whats-App-Image-2024-09-08-at-6-57-13-PM.jpg",
        "https://i.ibb.co/hx68RMZ/Whats-App-Image-2024-09-08-at-6-57-17-PM.jpg",
        "https://i.ibb.co/NtZmc1C/Whats-App-Image-2024-09-08-at-6-57-14-PM.jpg",
        "https://i.ibb.co/jvBDHSw/Whats-App-Image-2024-09-08-at-6-57-04-PM.jpg"
    ],
    "name": "KATAN SILK SAREE 0",
    "price": 1399,
    "size": [
            "S",
            "M",
            "L",
            "XL"
    ]
}

    saveurl = f'https://rainbow-f2f31-default-rtdb.asia-southeast1.firebasedatabase.app/rainbow/{
    category[0]}/{size}.json'
    saved = requests.put(saveurl, json=data)
savedata()