#!/usr/bin/env python3
#
# Main CLI entry point
#

import sys
import importlib

from .. import main
from . import parser
from . import usage

def create_topology() -> None:
  args = parser.create_topology_parse()
  main(args)

def lab_commands() -> None:
  if len(sys.argv) < 2:
    usage.run([])

  cmd = sys.argv[1]
  mod = importlib.import_module("."+cmd,__name__)
  if not mod:
    print("Invalid CLI command: %s. Use 'help' to get the list of valid commands")
    sys.exit(1)
  mod.run(sys.argv[2:])
