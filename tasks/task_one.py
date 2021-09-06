import json
from xkcd import comicrequest as cr


def run():
    """
    Write a script called task_one.py that when called will output something like this to the console. (reference below)
    """
    comics = []
    for seq in range(3):
        comic_request = cr.ComicRequest()
        my_comic = comic_request.get_comic_without_image(seq + 1)
        # print(json.dumps(my_comic.__dict__, indent=4 ))

        comic_dict = {'comic': my_comic.title,
                      'meta_comic': {'alt-text': my_comic.alt,
                                     'number': my_comic.num,
                                     'link': my_comic.comic_url.replace('/info.0.json', ''),
                                     'imgae': my_comic.image_url.split('/')[-1],
                                     'image_link': my_comic.image_url}}

        comics.append(comic_dict)

    print(json.dumps(comics, indent=4))


if __name__ == '__main__':
    run()
