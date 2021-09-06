import requests
import json

"""
xkcd XkcdAPI
"""


class XkcdAPI:
    """
    XkcdAPI class contain the methods which require to interact with xkcd
    """

    def __init__(self):
        """
        initialize the xkcd api url
        """
        self._prefix_url = 'https://xkcd.com/{}{}'
        self._suffix_url = 'info.0.json'

    def get_url(self, comic_id):
        """
        Generate the xkcd URL for the given comic id
        Parameters
        ----------
        comic_id : int
            comic id
        Returns
        -------
        srt
            URL for comic id
        """
        return self._prefix_url.format(str(comic_id) + '/', self._suffix_url)

    def get_response(self, comic_url):
        """
        fetch http response from xkcd API for given URL
        Parameters
        ----------
        comic_url : string
            comic url to send http request
        Returns
        -------
        str
            json response as str
        Raises
        ------
        Exception
            If an http code not equal to 200
        """
        xkcd_response = requests.get(comic_url)
        if xkcd_response.status_code != 200:
            raise Exception('Error, xkcd return HTTP status_code :{}, for url :{}, reason :{}'
                            .format(xkcd_response.status_code, comic_url, xkcd_response.reason))
        return json.loads(xkcd_response.text)

    def get_image(self, image_url):
        """
        get comic image requests
        Parameters
        ----------
        image_url : str
            image url
        Returns
        -------
        bytes
            comic image binary
        """
        image_response = requests.get(image_url)
        if image_response.status_code != 200:
            raise Exception('Error, xkcd return HTTP status_code :{}, for url :{}, reason :{}'
                            .format(image_response.status_code, image_url, image_response.reason))
        return image_response.content
