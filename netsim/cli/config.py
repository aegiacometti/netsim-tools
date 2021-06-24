#
# netlab create command
#
# Creates virtualization provider configuration and automation inventory from
# the specified topology
#
import typing

from . import ansible

def run(cli_args: typing.List[str]) -> None:
  ansible.playbook('initial-config.ansible',cli_args)
