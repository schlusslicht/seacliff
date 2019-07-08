from logging import getLevelName
from sys import exit
from typing import List

from seacliff.params._param import _param
from seacliff.utilities import concretemethod, instance, logger


class log_level(_param):

  @concretemethod
  def _parse(self, params: List[str]) -> None:
    try: logger().setLevel(getLevelName(params[0]))
    except: exit('Invalid log level {}'.format(params[0]))

    instance.config.set('logging', 'level', params[0])
    logger().info('Set log level to %s', params[0])
