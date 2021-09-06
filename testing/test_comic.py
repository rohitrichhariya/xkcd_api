"""
Tests for Comic
"""

import unittest
from xkcd.comic import Comic
from testing import jpg_image
from testing import test_comic_record, test_comic_url


class TestComic(unittest.TestCase):

    def test_comic_ok(self):
        c = Comic(test_comic_record, test_comic_url)
        c.set_image(jpg_image)
        self.assertIsInstance(c, Comic)

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
