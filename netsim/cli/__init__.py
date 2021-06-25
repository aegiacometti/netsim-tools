#!/usr/bin/env python3
#
# Main CLI entry point
#

import sys
import importlib
import argparse

from . import usage

def common_parse_args() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser(description='Common argument parsing',add_help=False)
  parser.add_argument('--defaults', dest='defaults', action='store', default='topology-defaults.yml',
                  help='Local topology defaults file')
  parser.add_argument('--log', dest='logging', action='store_true',
                  help='Enable basic logging')
  parser.add_argument('-q','--quiet', dest='quiet', action='store_true',
                  help='Report only major errors')
  parser.add_argument('-v','--view', dest='verbose', action='store_true',
                  help='Verbose logging')
  return parser

def topology_parse_args() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser(description='Common topology arguments',add_help=False)
  parser.add_argument('-d','--device', dest='device', action='store', help='Default device type')
  parser.add_argument('-p','--provider', dest='provider', action='store',help='Override virtualization provider')
  return parser

def lab_commands() -> None:
  if len(sys.argv) < 2:
    usage.run([])
    sys.exit()

  cmd = sys.argv[1]
  try:
    mod = importlib.import_module("."+cmd,__name__)
  except:
    mod = None

  if mod and hasattr(mod,'run'):
    mod.run(sys.argv[2:])   # type: ignore
    return

  print("Invalid CLI command: %s\n\nUse 'netlab usage' to get the list of valid commands" % cmd)
  sys.exit(1)
