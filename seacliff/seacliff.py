import sys
from configparser import ConfigParser
from importlib import import_module as mod
from logging import basicConfig
from os import getpid
from sys import argv, exit

from seacliff.modes.dummy import dummy
from seacliff.utilities import defaultconfig, instance, logger


def main() -> None: seacliff().main()
if __name__ == '__main__': main()

class seacliff():

  def __init__(self) -> None:
    argv.pop(0)
    basicConfig(
      datefmt = '%Y-%m-%d %H:%M:%S',
      format = '%(asctime)s [%(levelname)s] <%(name)s> %(message)s'
    )

  def main(self) -> None:
    instance.config = ConfigParser()
    instance.config.read_dict(defaultconfig())
    instance.mode = dummy

    try:
      logger().info('Started seacliff with pid %s', getpid())

      for i in [i for i in argv if i.startswith('--')]:
        try: mod('seacliff.params.{}'.format(i[2:])).__dict__[i[2:]](argv)
        except: exit('Invalid parameter or argument to {}'.format(i[2:]))

      mode = instance.mode()
      mode.execute()

    except KeyboardInterrupt: print('\N{bomb}')
    except Exception as exception: logger().exception(exception)
    except SystemExit as exception: logger().critical(str(exception))

    finally: logger().info('Stopped seacliff with pid %s', getpid())
