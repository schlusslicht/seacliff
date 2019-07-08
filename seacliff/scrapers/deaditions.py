from datetime import datetime
from re import search, sub
from typing import Any, List

from cdx_toolkit import CDXFetcher
from cdx_toolkit.timeutils import TIMESTAMP
from lxml import html
from requests import get, head
from urllib3.util import Url, parse_url

from seacliff.scrapers._scraper import _scraper
from seacliff.units.deadition import deadition
from seacliff.utilities import concretemethod, logger


class deaditions(_scraper):

  @concretemethod
  def scrape(self) -> List[Any]:
    items = []

    for iter in html.parse(self.config.source).xpath(self.config.xpath_root):
      try:
        title = iter.find(self.config.xpath_title)
        comments = iter.find(self.config.xpath_comments)
        if title is None or comments is None: continue

        name = self.__zeroblank(title.text)
        href = parse_url(title.get('href'))
        if not name or not href.host: continue

        info = comments.text_content()
        item = deadition(href.url, name)
        star = iter.find(self.config.xpath_starred)
        if star is not None: item.meta.ranking += 1

        self.__available(item)
        self.__parseinfo(item, info)
        self.__ranking(item, href)
        self.__touched(item, 'ia')

        items.append(item)
        logger().debug('Scraped deadition %s', name)
      except: logger().debug('Ignoring deadition %s', name)

    return items

  def __available(self, item: deadition) -> None:
    try: req = head(item.href, allow_redirects = True, verify = False)
    except: req = None

    item.meta.available = True if req and req.status_code == 200 else False

  def __parseinfo(self, item: deadition, info: str) -> None:
    editors = search(self.config.re_editors, info.strip())
    years = search(self.config.re_years, editors[0]) if editors else None

    if editors:
      item.meta.editors = sub(r',? ' + self.config.re_years, '', editors[0])
      item.meta.description = self.__zeroblank(info.replace(editors[0], ''))
    else: item.meta.description = self.__zeroblank(info)

    if years and years[1]: item.meta.published.man = int(years[1])
    if years and years[2]: item.meta.lastseen.man = int(years[2])

  def __ranking(self, item: deadition, href: Url) -> None:
    if self.config.rank_key:
      domain = { 'domains[]': href.host }
      auth = { 'API-OPR': self.config.rank_key }
      req = get(self.config.rank_url, headers = auth, params = domain)

      item.meta.ranking += req.json()['response'][0]['page_rank_decimal']
    else: item.meta.ranking += (255 - len(href.url)) / 255

  def __touched(self, item: deadition, src: str) -> None:
    archive = CDXFetcher(source = src)
    stamp = lambda s: datetime.strptime(s.data['timestamp'], TIMESTAMP)

    lastseen = archive.get(item.href, filter = 'status:200', limit = -1)
    if len(lastseen): item.meta.lastseen[src] = stamp(lastseen[0])

    published = archive.get(item.href, filter = 'status:200', limit = 1)
    if len(published): item.meta.published[src] = stamp(published[0])

  def __zeroblank(self, text: str) -> str:
    return sub(r'\s+', ' ', text).strip()
