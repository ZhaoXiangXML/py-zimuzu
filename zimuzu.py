# -*- coding: utf-8 -*-
import argparse
import requests
import xml.etree.ElementTree as ElementTree


def main():
    parser = argparse.ArgumentParser(
        description='Check changes on [ZiMuZu.tv](www.zimuzu.tv), add tasks to [aria2](https://aria2.github.io/) if any new magnet link was found.')
    parser.add_argument("--add", dest="urls", metavar='URL', nargs='+',
                        help='urls to be added')
    parser.add_argument("--skip-existings", action='store_true',
                        help='skip any existing links, only watch for updates in the future')
    args = parser.parse_args()
    for url in args.urls:
        resid = add_url(url, args.skip_existings)
        download_rss(resid)


def add_url(url, skip_existings):
    resid = int(str.split(url, '/')[-1])
    return resid


def download_rss(resid):
    r = requests.get('http://diaodiaode.me/rss/feed/' + str(resid))
    r.raise_for_status()
    root = ElementTree.fromstring(r.content)[0]
    link = root.find('./link').text
    title = root.find('./title').text
    items = root.findall('./item')
    print len(items)


if __name__ == "__main__":
    main()
