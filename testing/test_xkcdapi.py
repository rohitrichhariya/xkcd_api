from unittest import TestCase
from testing import test_comic_url, comic_id, test_image_url
from xkcd.xkcdapi import XkcdAPI
import ast

"""
Tests for xkcd.XkcdAP
"""

class TestXkcdAPI(TestCase):

    def test_get_url(self):
        api = XkcdAPI()
        api_url = api.get_url(comic_id)
        self.assertEqual(api_url, test_comic_url)

    def test_get_response(self):
        api = XkcdAPI()
        api_response = api.get_response(test_comic_url)

        with open('xkcd_response_1.json', 'r') as xkcd_response_1:
            data = xkcd_response_1.read()

        test_response = ast.literal_eval(data)

        self.assertDictEqual(api_response, test_response)

    def test_get_image(self):
        api = XkcdAPI()
        api_response = api.get_image(test_image_url)

        with open('barrel_cropped_(1).jpg', 'rb') as xkcd_response_1:
            test_image = xkcd_response_1.read()

        self.assertEqual(api_response, test_image)
