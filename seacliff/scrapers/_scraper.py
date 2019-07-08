from abc import ABC, abstractmethod
from typing import Any, Dict, List

from seacliff.utilities import concretemethod, dotdict, instance, logger


class _scraper(ABC):

  def __init__(self, configuration: Dict[str, str]) -> None:
    this = self.__class__.__name__
    self.config = dotdict(configuration)
    logger().debug('Initialized scraper %s', this)

  @abstractmethod
  def scrape(self) -> List[Any]:
    raise(NotImplementedError('Too abstract'))
