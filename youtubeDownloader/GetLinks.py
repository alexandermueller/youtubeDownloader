#!/usr/bin/env python

import httplib2
from bs4 import BeautifulSoup, SoupStrainer

def getLinks(url):
    links            = []
    http             = httplib2.Http()
    status, response = http.request(url)
    requirements     = [{'class' : ['yt-uix-scroller-scroll-unit', 'vve-check']}, 'data-index', 'data-innertube-clicktracking', 'data-thumbnail-url', 'data-video-id', 'data-video-title', 'data-video-username']

    for li in BeautifulSoup(response, "html5lib").find_all('li'):
        passesChecks = True

        for requirement in requirements:
            if not passesChecks:
                break

            if str(type(requirement)) == "<type 'str'>":
                if not li.has_attr(requirement):
                    passesChecks = False
                    break
            elif str(type(requirement)) == "<type 'dict'>":
                for attr in requirement.keys():
                    if not li.has_attr(attr):
                        passesChecks = False
                        break
                    else:
                        for value in requirement[attr]:
                            if value not in li[attr]:
                                passesChecks = False
                                break

                    if not passesChecks:
                        break

        if passesChecks:
            if li.a.has_attr('href'):
                links += [li.a['href']]

    return links 
