import random
import xkcd.comicrequest as cr


def run():
    """
    1. GET 15 random comics and following details in using Python.
        a. Get the names of the comic
        b. Get the alt-text of the comic
        c. Get the number of the comic
        d. Get the link of the comic
        e. Get the image of the comics
        f. Get the image Link of the comics

    """
    comics = []
    for seq in range(15):
        random_id = random.randint(1, 87)
        comic_request = cr.ComicRequest()
        my_comic = comic_request.get_comic(random_id)

        print("Details of random comic :", str(seq + 1))
        print("\t the names of the comic :", my_comic.title)
        print("\t the alt-text of the comic :", my_comic.alt)
        print("\t the number of the comic :", my_comic.num)
        print("\t the link of the comic :", my_comic.comic_url)
        print("\t the image of the comics :", my_comic.image_url.split('/')[-1])
        print("\t the image Link of the comics :", my_comic.image_url)

        comics.append(my_comic)


if __name__ == '__main__':
    run()
