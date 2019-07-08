from sys import exit
from typing import List

from seacliff.params._param import _param
from seacliff.utilities import concretemethod, instance, logger


class config_text(_param):

  @concretemethod
  def _parse(self, params: List[str]) -> None:
    try: instance.config.read_string(params[0])
    except: exit('Invalid config string {}'.format(params[0]))

    logger().info('Read config string %s', params[0])
