from sys import exit
from typing import List

from seacliff.params._param import _param
from seacliff.utilities import concretemethod, instance, logger


class config_file(_param):

  @concretemethod
  def _parse(self, params: List[str]) -> None:
    try: instance.config.read_file(open(params[0]))
    except: exit('Invalid config file {}'.format(params[0]))

    logger().info('Read config file %s', params[0])
