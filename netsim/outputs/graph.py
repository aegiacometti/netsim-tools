#
# Create Ansible inventory
#
import typing

import yaml
import os
from box import Box

from .. import common
from . import _TopologyOutput

def node_with_label(f : typing.TextIO, n: Box) -> None:
  f.write("  %s [" % n.name)
  f.write(' label=<%s [%s]<br /><sub>%s</sub>>' % (n.name,n.device,n.loopback.ipv4 or n.loopback.ipv6 or ""))
  f.write(" ]\n")

def network_with_label(f : typing.TextIO, n: Box) -> None:
  f.write("  %s [" % n.bridge)
  f.write(" style=filled fillcolor=lightgrey fontsize=11")
  f.write(' label="%s"' % (n.prefix.ipv4 or n.prefix.ipv6 or n.bridge))
  f.write(" ]\n")

def edge_label(f : typing.TextIO, direction: str, data: Box) -> None:
  addr = data.ipv4 or data.ipv6
  if addr:
    f.write(' %slabel="%s"' % (direction,addr))

def edge_p2p(f : typing.TextIO, l: Box) -> None:
  f.write(' %s -- %s' % (l.left.node, l.right.node))
  f.write(' [')
  edge_label(f,'tail',l[l.left.node])
  edge_label(f,'head',l[l.right.node])
  f.write(' ]\n')

def edge_node_net(f : typing.TextIO, l: Box, k: str) -> None:
  f.write(" %s -- %s" % (k,l.bridge))
  f.write(' [')
  edge_label(f,'tail',l[k])
  f.write(' ]\n')

def graph_start(f : typing.TextIO) -> None:
  f.write("graph {\n")
  f.write("  node [shape=box, style=rounded fontname=Verdana]\n")
  f.write("  edge [fontname=Verdana labelfontsize=10 labeldistance=1.5]\n")

def graph_topology(topology: Box, fname: str) -> None:
  f = common.open_output_file(fname)
  graph_start(f)

  node_map = {}
  for n in topology.nodes:
    node_map[n.name] = n
    node_with_label(f,n)

  for l in topology.links:
    if l.type == "p2p":
      edge_p2p(f,l)
    else:
      if not l.bridge:
        common.error('Found a lan/stub link without a bridge name, skipping',common.IncorrectValue,'graph')
        next
      network_with_label(f,l)
      for k in l.keys():
        if k in node_map:
          edge_node_net(f,l,k)

  f.write("}\n")
  f.close()

class Graph(_TopologyOutput):

  def write(self, topology: Box) -> None:
    graphfile = self.settings.filename or 'graph.dot'
    output_format = 'topology'

    if hasattr(self,'filenames'):
      graphfile = self.filenames[0]
      if len(self.filenames) > 1:
        common.error('Extra output filename(s) ignored: %s' % str(self.filenames[1:]),common.IncorrectValue,'graph')

    if hasattr(self,'format'):
      output_format = self.format

    graph_topology(topology,graphfile)
    print("Created graph file %s in %s format" % (graphfile, output_format))