#
# Dynamic output framework
# 
# Individual output routines are defined in modules within this directory inheriting
# TopologyOutput class and replacing or augmenting its methods (most commonly, write)
#

import platform
import subprocess
import os
import typing

# Related modules
from box import Box

from .. import common
from ..callback import Callback

class _TopologyOutput(Callback):
  def __init__(self, output: str, data: Box) -> None:
    self.settings = data

    output_parts = output.split('=')

    output_list = output_parts[0].split(':')
    self.output = output_list[0]
    if len(output_list) > 1:
      self.format = output_list[1]

    if len(output_parts) > 1:
      self.filenames = output_parts[1].split(',')

  @classmethod
  def load(self, output: str, data: Box) -> typing.Optional['_TopologyOutput']:
    module_name = __name__+"."+output.split(':')[0]
    obj = self.find_class(module_name)
    if obj:
      return obj(output,data)
    else:
      return None

  def get_template_path(self) -> str:
    return 'templates/outputs/' + self.output + "/" + (self.format or "default") + ".j2"

  def get_output_name(self, fname: str, topology: Box) -> typing.Optional[str]:
    if fname:
      return fname

    if self.settings:
      return self.settings.filename

    return None

  def write(self, topology: Box) -> None:
    common.fatal('someone called the "write" method of TopologyOutput abstract class')
