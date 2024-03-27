# PyWebIO imports
import pywebio
from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.session import *
from functools import partial


app_name = "Test"
port = 80
debug = True


def do_nothing():
  pass


def menu():
  clear()
  put_markdown("# Hello, world!")


if __name__ == '__main__':
  pywebio.config(title=app_name)
  start_server(menu, port=port, debug=debug)
