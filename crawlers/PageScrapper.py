# -*- coding: utf-8 -*-
import requests
from models.Page import Page
import urllib3


urllib3.disable_warnings()

class PageScrapper:

    def __init__(self, website, pages=[]):
        self._website = website
        self._pages = pages


    def _get_content(self, page):
        return str(page.content).replace("'", "")


    def _get_headers(self, page):
        return page.headers


    def get_results(self):
        results = []
        for url in self._pages:
            url = url.replace('\n','')
            page_infos = requests.get(url, verify=False, timeout=60)
            page = Page(website=self._website, link=url, headers=self._get_headers(page_infos), content=self._get_content(page_infos))
            results.append(page)
        return results
