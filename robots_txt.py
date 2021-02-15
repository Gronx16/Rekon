import urllib.request
import io
from general import *

def get_robots_txt(url):
    if url.endswith("/"):
        path = url
    else:
        path = url + "/"
    pp=path + "robots.txt"
    try:
        req = urllib.request.urlopen(pp, data =None)
        data = io.TextIOWrapper(req, encoding="utf-8")


    except Exception as ex:
        print("Robots.txt file doesn't exist")
        return 0
    else:
        return data.read()
