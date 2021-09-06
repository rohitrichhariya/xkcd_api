from xkcd.xkcdapi import XkcdAPI
from xkcd.comic import Comic

"""
xkcd ComicRequest
"""


class ComicRequest:
    """
    XkcdAPI class contain the methods which require to get the comic details
    and image with the help of XkcdAPI class from xkcd
    """

    def get_comic(self, comic_id):
        """
        get the comic details and image with the help of XkcdAPI class method
        Parameters
        ----------
        comic_id : int

        Returns
        -------
        my_comic : xkcd comic
        """
        api = XkcdAPI()
        api_url = api.get_url(comic_id)
        api_response = api.get_response(api_url)

        my_comic = Comic(api_response, api_url)
        comic_image = api.get_image(my_comic.image_url)
        my_comic.set_image(comic_image)
        return my_comic

    def get_comic_without_image(self, comic_id):
        """
         get the comic without image with the help of XkcdAPI class method
         Parameters
         ----------
         comic_id : int

         Returns
         -------
         my_comic : xkcd comic
         """
        api = XkcdAPI()
        api_url = api.get_url(comic_id)
        api_response = api.get_response(api_url)
        my_comic = Comic(api_response, api_url)
        return my_comic
