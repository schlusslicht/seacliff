from seacliff.modes._mode import _mode
from seacliff.utilities import concretemethod


class dummy(_mode):

  @concretemethod
  def execute(self) -> None:
    pass
