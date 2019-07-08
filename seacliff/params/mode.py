from importlib import import_module as mod
from sys import exit
from typing import List

from seacliff.params._param import _param
from seacliff.utilities import concretemethod, instance, logger


class mode(_param):

  @concretemethod
  def _parse(self, params: List[str]) -> None:
    try: mode = mod('seacliff.modes.{}'.format(params[0])).__dict__[params[0]]
    except: exit('Invalid mode {}'.format(params[0]))

    instance.mode = mode
    logger().info('Set mode to %s', params[0])
