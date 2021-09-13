import requests

jpg_image = requests.get("https://imgs.xkcd.com/comics/barrel_cropped_(1).jpg")

test_comic_record = {
    'num': 1,
    'safe_title': 'Barrel - Part 1',
    'alt': 'Don''t we all',
    'img': 'https://imgs.xkcd.com/comics/barrel_cropped_(1).jpg',
    'comic_url': 'https://xkcd.com/1/info.0.json'
}

test_comic_url = 'https://xkcd.com/1/info.0.json'
test_image_url = 'https://imgs.xkcd.com/comics/barrel_cropped_(1).jpg'

comic_id = 1

test_image = None
with open('barrel_cropped_(1).jpg', 'rb') as xkcd_response_1:
    test_image = xkcd_response_1.read()
