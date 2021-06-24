#
# Common Ansible interface commands
#

import subprocess
import sys
import os
import typing
from pathlib import Path

from .. import common

try:
  from importlib import resources
except ImportError:
  import importlib_resources as resources # type: ignore

def find_playbook(name: str) -> str:
  cwd = Path(os.getcwd()).resolve()
  scriptdir = Path(sys.argv[0]).resolve().parent
  moddir = Path(__file__).resolve().parent.parent

  for dir in [cwd,cwd / 'ansible',scriptdir / 'ansible',moddir / 'ansible']:
    if os.path.isfile(dir / name):
      return str(dir / name)

def playbook(name: str, args: typing.List[str]) -> None:
  pbname = find_playbook(name)
  if not pbname:
    common.fatal("Cannot find Ansible playbook %s, aborting" % name)
  if common.VERBOSE:
    print("Running Ansible playbook %s" % pbname)

  cmd = ['ansible-playbook',pbname]
  cmd.extend(args)

  try:
    subprocess.check_call(cmd)
  except:
    common.fatal("Ansible playbook failed")
