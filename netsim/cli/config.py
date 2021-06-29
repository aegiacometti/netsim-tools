#
# netlab config command
#
# Deploy custom configuration template to network devices
#
import typing
import argparse

from . import common_parse_args
from . import ansible

#
# CLI parser for 'netlab config' command
#
def custom_config_parse(args: typing.List[str]) -> typing.Tuple[argparse.Namespace, typing.List[str]]:
  parser = argparse.ArgumentParser(
    parents=[ common_parse_args() ],
    prog="netlab config",
    description='Deploy custom configuration template',
    epilog='All other arguments are passed directly to ansible-playbook')

  parser.add_argument(
    dest='template', action='store',
    type=argparse.FileType('r'),
    help='Deploy just the initial configuration')

  return parser.parse_known_args(args)

def run(cli_args: typing.List[str]) -> None:
  (args,rest) = custom_config_parse(cli_args)

  if args.verbose:
    rest = ['-v'] + rest

  rest = ['-e','config='+args.template.name] + rest

  if args.logging or args.verbose:
    print("Ansible playbook args: %s" % rest)

  ansible.playbook('config.ansible',rest)
