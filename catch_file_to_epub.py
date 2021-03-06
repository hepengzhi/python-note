#!/usr/bin/env python
# vim:fileencoding=utf-8
from __future__ import unicode_literals, division, absolute_import, print_function
from calibre.web.feeds.news import BasicNewsRecipe

class liaoxuefeng_python(BasicNewsRecipe):
    title          = '廖雪峰Python教程'
    description = 'python教程'
    max_articles_per_feed = 200
    url_prefix = 'http://www.liaoxuefeng.com'
    no_stylesheets = True
    keep_only_tags = [{ 'id': 'main' }]
    remove_tags=[{'class':'x-wiki-info'}]
    remove_tags_after=[{'class':'x-wiki-content x-content'}]

    def get_title(self, link):
        return link.contents[0].strip()

    def parse_index(self):
        soup = self.index_to_soup('http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000')

        div = soup.find('div', { 'class': 'x-wiki-tree' })

        articles = []
        for link in div.findAll('a'):
            til = self.get_title(link)
            url = self.url_prefix + link['href']
            a = { 'title': til, 'url': url }

            articles.append(a)

        tutorial = [('廖雪峰python教程', articles)]

        return tutorial