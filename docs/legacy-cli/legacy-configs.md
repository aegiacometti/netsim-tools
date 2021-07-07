# initial-config.ansible

**initial-config.ansible** is an Ansible playbook that can be used to deploy initial device configurations created from included configuration templates and expanded inventory data created with **create-topology** script.

```{warning}
Direct access to Ansible playbook has been replaced with **‌netlab initial** command in release 0.8. The playbook is still available within `netlab/ansible` directory. To use it directly, download the source code from GitHub and use `source setup.sh` to set up PATH variable.
```

The playbook deploys device configurations in two steps:

* Initial device configurations (**initial** tag)
* Module-specific device configurations (**module** tag)

When run without the **--tags** parameter, the playbook deploys all relevant configurations.

When run with **-v** parameter, the playbook displays device configurations before deploying them. You could use **-v --tags test** parameters to display device configurations without deploying them.

## Initial Device Configurations

Initial device configurations are created from inventory data and templates in **templates/initial** directory. Device-specific configuration template is selected using **ansible_network_os** value (making IOSv and CSR 1000v templates identical).

As of [release 0.4](../release/0.4.md), the following parameters are supported:

* hostname
* interface IPv4 and IPv6 addresses
* unnumbered interfaces
* interface descriptions
* interface MAC addresses
* interface bandwidth (when supported by the device)

The initial configuration also includes LLDP running on all interfaces apart from the management interface (not configurable).

Default passwords and other default configuration parameters are supposed to be provided by the Vagrant boxes.

## Module Configurations

Module-specific device configurations are created from templates in **templates/_module_** directory. Device-specific configuration template is selected using **ansible_network_os** value. See the [module descriptions](../module-reference.md) for list of supported parameters.

This part of the configuration deployment could be limited with **modlist** external variable -- a subset of configuration modules to be deployed. For example, to configure just OSPF (in a network running OSPF and BGP) on R1, use:

```
$ initial-config.ansible -l r1 -e modlist=[ospf]
```
