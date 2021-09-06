from unittest import TestCase
from xkcd.comic import Comic
from testing import jpg_image
from testing import test_comic_record, test_comic_url, comic_id
from xkcd import comicrequest as cr

"""
Tests for xkcd.ComicRequest
"""


class TestComicRequest(TestCase):

    def test_get_comic(self):
        c = Comic(test_comic_record, test_comic_url)
        c.set_image(jpg_image)
        comic_request = cr.ComicRequest()
        my_comic = comic_request.get_comic(comic_id)
        self.assertIsInstance(my_comic, Comic)

        # num
        self.assertEqual(c.num, test_comic_record.get('num'))

        # title
        self.assertEqual(c.title, test_comic_record.get('safe_title'))

        # alt
        self.assertEqual(c.alt, test_comic_record.get('alt'))

        # image
        self.assertEqual(c.image, jpg_image)

        # image_url
        self.assertEqual(c.image_url, test_comic_record.get('img'))

        # comic_url
        self.assertEqual(c.comic_url, test_comic_url)

    def test_get_comic_without_image(self):
        c = Comic(test_comic_record, test_comic_url)
        comic_request = cr.ComicRequest()
        my_comic = comic_request.get_comic_without_image(comic_id)
        self.assertIsInstance(my_comic, Comic)

        # num
        self.assertEqual(c.num, test_comic_record.get('num'))

        # title
        self.assertEqual(c.title, test_comic_record.get('safe_title'))

        # alt
        self.assertEqual(c.alt, test_comic_record.get('alt'))

        # image
        self.assertEqual(c.image, None)

        # image_url
        self.assertEqual(c.image_url, test_comic_record.get('img'))

        # comic_url
        self.assertEqual(c.comic_url, test_comic_url)
