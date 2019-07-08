from abc import ABC, abstractmethod

from seacliff.utilities import dotdict, instance, logger


class _mode(ABC):

  def __init__(self) -> None:
    this = self.__class__.__name__
    if not instance.config.has_section(this):
      raise(RuntimeError('Missing {} configuration section'.format(this)))

    self.config = dotdict(instance.config.items(this, True))
    logger().debug('Initialized mode %s', this)

  @abstractmethod
  def execute(self) -> None:
    raise(NotImplementedError('Too abstract'))
