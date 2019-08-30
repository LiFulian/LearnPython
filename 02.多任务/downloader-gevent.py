import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "2.jpg", "http://dingyue.nosdn.127.net/Z=f5GOKxHVtFldZauMGEuN0oe5RxPEFgBWTvzPLrsjkMv1518483490799.jpg"),
        gevent.spawn(downloader, "3.jpg", "https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2570578367,1831232679&fm=26&gp=0.jpg")
    ])


if __name__ == '__main__':
    main()