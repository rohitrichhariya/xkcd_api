
"""
xkcd Comic
"""


class Comic:
    """
    comic class represent a comic from xkcd
    """

    def __init__(self, xkcd_dict, comic_url):
        """
        Comic init
        Parameters
        ----------
        xkcd_dict : dict
            json obtained from xkcd API
        comic_url : str or None
            comic url
        """
        self.num = xkcd_dict.get('num')
        self.title = xkcd_dict.get('safe_title')
        self.alt = xkcd_dict.get('alt')
        self.image = None
        self.image_url = xkcd_dict.get('img')
        self.comic_url = comic_url

    def set_image(self, comic_image):
        """
        Parameters
        ----------
        comic_image :  bytes
            comic image binary
        """
        self.image = comic_image
