Release notes
=============

2021-05-24 (`release 0.6.3 <https://github.com/ipspace/netsim-tools/releases/tag/release_0.6.3>`_)
  * BGP configuration module
  * IS-IS configuration module
  * Segment Routing with MPLS
  * OSPF configuration improvements: external links and passive interfaces
  * FRR and Cumulus VX support
  * Installation playbook
  * Bug fixes

  :doc:`More details <release/0.6>`

2021-04-11 (`release 0.5 <https://github.com/ipspace/netsim-tools/releases/tag/release_0.5>`_)
  * containerlab support
  * Flexible virtualization provider framework

  :doc:`More details <release/0.5>`

2021-03-26 (`release 0.4 <https://github.com/ipspace/netsim-tools/releases/tag/release_0.4>`_)
  * Unnumbered interfaces
  * Configuration modules framework
  * Baseline OSPF module

  :doc:`More details <release/0.4>`

2021-01-24 (`release 0.3 <https://github.com/ipspace/netsim-tools/releases/tag/release_0.3>`_)
  * Support for multiple virtualization providers
  * Vagrant with VirtualBox
  * EOS and Nexus OS supported on Vagrant/VirtualBox
  * Device images (Vagrant boxes) are configurable in the defaults

  :doc:`More details <release/0.3>`

2021-01-12 (`release 0.2 <https://github.com/ipspace/netsim-tools/releases/tag/release_0.2>`_)
   Major refactoring of addressing configuration

   * Structured address pools (loopback, lan, p2p)
   * IPv4 and IPv6 support
   * Initial configuration modules updated to work in dual-stack or IPv6-only environments

2021-01-07 (`release 0.11 <https://github.com/ipspace/netsim-tools/releases/tag/release_0.11>`_)
   Arrcus ArcOS support contributed by Dave Thelen

   Refactored configuration gathering -- use explicit **device_facts** modules or platform-specific tasks
   for platforms that don't gather device configuration with fact-gathering module
2020-12-21
   Nexus 9300v support
2020-12-17
   Initial release (IOSv, CSR, EOS)

.. toctree::
   :caption: Individual release notes
   :maxdepth: 2

   release/0.6.md
   release/0.5.md
   release/0.4.md
   release/0.3.md

Future plans
------------
Release 0.7

  * Add Cumulus VX support
