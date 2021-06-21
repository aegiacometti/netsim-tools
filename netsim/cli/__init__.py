#!/usr/bin/env python3
#
# Main CLI entry point
#

from .. import main
from . import parser

def create_topology() -> None:
  args = parser.create_topology_parse()
  main(args)
