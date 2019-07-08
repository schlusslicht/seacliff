from inspect import getmodule, stack
from logging import Logger, getLevelName, getLogger
from typing import Any, Callable, Dict, get_type_hints


def concretemethod(call: Callable) -> Callable:
  from inspect import stack
  from re import search

  name = search(r'class[^(]+\((\w+)\)\:', stack()[2][4][0]).group(1)
  base = getattr(stack()[2][0].f_locals[name], call.__name__)

  if get_type_hints(call) != get_type_hints(base):
    raise(TypeError('Invalid concretisation'))

  return(call)


class dotdict(dict):
  __getattr__ = dict.get
  __setattr__ = dict.__setitem__
  __delattr__ = dict.__delitem__

  def __init__(self, *args, **kwargs):
    for key, value in dict(*args, **kwargs).items():
      if hasattr(value, 'keys'): value = dotdict(value)
      self[key] = value


def defaultconfig() -> Dict[str, Dict[str, str]]:
  return dotdict({
    'DEFAULT': {
      'name': 'seacliff'
    },
    'dummy': { },
    'logging': {
      'level': 'INFO'
    }
  })


class instance():
  __data = dotdict()

  @classmethod
  def __delattr__(cls, attr: str) -> None:
    del cls.__data[attr]

  @classmethod
  def __getattr__(cls, attr: str) -> Any:
    return cls.__data[attr]

  @classmethod
  def __setattr__(cls, attr: str, value: Any) -> None:
    cls.__data[attr] = value


def logger() -> Logger:
  conf = dotdict(instance.config['logging'])
  unit = getLogger(getmodule(stack()[1].frame).__name__)
  unit.setLevel(getLevelName(conf.level))
  return unit
