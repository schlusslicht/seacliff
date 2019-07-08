from abc import ABC, abstractmethod
from typing import List

from seacliff.utilities import logger


class _param(ABC):

  def __init__(self, params: List[str]) -> None:
    args = []
    logger().debug('Parsing cli param %s', params.pop(0)[2:])
    while params and not params[0].startswith('--'): args += [params.pop(0)]
    logger().debug('Passing cli args %s', str(args))
    self._parse(args)

  @abstractmethod
  def _parse(self, params: List[str]) -> None:
    raise(NotImplementedError('Too abstract'))
