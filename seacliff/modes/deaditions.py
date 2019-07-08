from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

from seacliff.modes._mode import _mode
from seacliff.processors.deaditions import deaditions as processor
from seacliff.scrapers.deaditions import deaditions as scraper
from seacliff.utilities import concretemethod


class deaditions(_mode):

  @concretemethod
  def execute(self) -> None:
    disable_warnings(category = InsecureRequestWarning)
    processor(self.config).process(scraper(self.config).scrape())
