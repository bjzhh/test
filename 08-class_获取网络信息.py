#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Zhanghui  time:2020/9/12

class NetInfo:
    def __init__(self):
        import os
        import sys

        try:
            import netifaces
        except ImportError:
            try:
                command_to_execute = "pip install netifaces || easy_install netifaces"
                os.system(command_to_execute)
            except OSError:
                print("Can NOT install netifaces, Aborted!")
                sys.exit(1)
            import netifaces

        self.routingGateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
        self.routingNicName = netifaces.gateways()['default'][netifaces.AF_INET][1]

        for interface in netifaces.interfaces():
            if interface == self.routingNicName:
                # print netifaces.ifaddresses(interface)
                self.routingNicMacAddr = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
                try:
                    self.routingIPAddr = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
                    # TODO(Guodong Ding) Note: On Windows, netmask maybe give a wrong result in 'netifaces' module.
                    self.routingIPNetmask = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']
                except KeyError:
                    pass

        # display_format = '%-30s %-20s'
        # print(display_format % ("Routing Gateway:", routingGateway))
        # print(display_format % ("Routing NIC Name:", routingNicName))
        # print(display_format % ("Routing NIC MAC Address:", routingNicMacAddr))
        # print(display_format % ("Routing IP Address:", routingIPAddr))
        # print(display_format % ("Routing IP Netmask:", routingIPNetmask))

    def GetMAC(self):
        return  self.routingNicMacAddr

    def GetIP(self):
        return  self.routingIPAddr

    def GetNicName(self):
        return  self.routingNicName

    def GetGateway(self):
        return  self.routingGateway

    def GetIPNetmask(self):
        return  self.routingIPNetmask



aa = NetInfo()
print(aa.GetMAC())
print(aa.GetIP())
print(aa.GetIPNetmask())
print(aa.GetGateway())
print(aa.GetNicName())