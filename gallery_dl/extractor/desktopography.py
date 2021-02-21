# -*- coding: utf-8 -*-

# Copyright 2014-2020 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://desktopography.net"""

from .common import Extractor, Message
from .. import text

BASE_PATTERN = r"(?:https?://)?desktopography\.net"

class DesktopologyExtractor(Extractor):
    """Base class for e621 extractors"""
    category = "desktopology"
    filename_fmt = "{category}_{id}_{file[md5]}.{extension}"
    root = "https://desktopography.net"

    def __init__(self, match):
        super().__init__(match)

    def metadata(self):
        """Return a dict with general metadata"""

    def posts(self):
        """Return an iterable containing all relevant 'posts' objects"""

    def items(self):
        data = self.metadata()
        for post in self.posts():
            file = post["file"]

            post["filename"] = file["md5"]
            post["extension"] = file["ext"]
            post.update(data)
            yield Message.Directory, post
            yield Message.Url, file["url"], post

class DesktopologyExhibitionExtractor(DesktopologyExtractor):
    """Return an iterable containing all relevant 'posts' objects"""

class DesktopologyEntryExtractor(DesktopologyExtractor):
    """Extractor for an artist's paintings on wikiart.org"""
    pattern = (BASE_PATTERN + r"/portfolios/([\w-]+)")
    log = False

    def __init__(self, match):
        """ aaa """

    def items(self):
        url = "{}/portfolios/{}".format(
            self.root, match[0])
        page = self.request(url).text
        print(page)
