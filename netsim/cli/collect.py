#
# netlab collect command
#
# Collect device configurations
#
import typing
import os
import argparse

from . import common_parse_args, topology_parse_args
from . import ansible
from .. import set_logging_flags

#
# CLI parser for 'netlab collect' command
#
def initial_config_parse(args: typing.List[str]) -> argparse.Namespace:
  parser = argparse.ArgumentParser(
    parents=[ common_parse_args() ],
    prog="netlab collect",
    description='Collect device configurations',
    epilog='All other arguments are passed directly to ansible-playbook')

  parser.add_argument(
    '-o','--output',
    dest='output', action='store',nargs='?',default='config',
    help='Output directory')
  return parser.parse_known_args(args)

def run(cli_args: typing.List[str]) -> None:
  (args,rest) = initial_config_parse(cli_args)

  if args.verbose:
    rest = ['-v'] + rest

  rest = ['-e','target='+args.output ] + rest

  if args.logging:
    print("Ansible playbook args: %s" % rest)

  ansible.playbook('collect-configs.ansible',rest)
