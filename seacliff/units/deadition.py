from typing import Any, Dict

from seacliff.utilities import dotdict


class metadata(dotdict):
  available: bool
  description: str
  editors: str
  lastseen: Dict[str, Any]
  published: Dict[str, Any]
  ranking: int

  def __init__(self) -> None:
    self.lastseen = dotdict()
    self.published = dotdict()
    self.ranking = 0


class deadition(dotdict):
  href: str
  name: str
  meta: metadata

  def __init__(self, href: str, name: str) -> None:
    self.href = href
    self.name = name
    self.meta = metadata()
