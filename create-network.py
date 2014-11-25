#!/usr/bin/env python
from mininet.node import RemoteController
from functools import partial
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI

__author__ = 'michael'
#sudo mn --custom ~/mininet/custom/topo-2sw-2host.py --topo mytopo --test pingall

from mininet.topo import Topo


class MyTopo(Topo):
    """Simple topology example."""

    def __init__(self):
        """Create custom topo."""

        # Initialize topology
        Topo.__init__(self)



        #DMZ
        dmz_sw = self.addSwitch('s1')
        dmz_srv = self.addHost('h1')
        dmz_fw = self.addHost('h2')

        self.addLink(dmz_sw, dmz_srv)
        self.addLink(dmz_sw, dmz_fw)



        #Apps
        apps_sw = self.addSwitch('s2')
        apps_srv = self.addHost('h3')
        apps_fw = self.addHost('h4')

        self.addLink(apps_sw, apps_srv)
        self.addLink(apps_sw, apps_fw)



        #Dept 1
        d1_sw1 = self.addSwitch('s3')
        d1_sw2 = self.addSwitch('s4')
        d1_sw3 = self.addSwitch('s5')
        d1_wifi = self.addSwitch('s6')
        d1_host1 = self.addHost('h5')
        d1_host2 = self.addHost('h6')
        d1_host3 = self.addHost('h8')
        d1_host4 = self.addHost('h9')
        d1_host5 = self.addHost('h10')
        d1_host6 = self.addHost('h11')

        self.addLink(d1_sw1, d1_sw2)
        self.addLink(d1_sw1, d1_sw3)
        self.addLink(d1_sw1, d1_wifi)
        self.addLink(d1_sw2, d1_host1)
        self.addLink(d1_sw2, d1_host2)
        self.addLink(d1_sw3, d1_host3)
        self.addLink(d1_sw3, d1_host4)
        self.addLink(d1_wifi, d1_host5)
        self.addLink(d1_wifi, d1_host6)


        #Dept 2
        d2_sw1 = self.addSwitch('s7')
        d2_sw2 = self.addSwitch('s8')
        d2_sw3 = self.addSwitch('s9')
        d2_wifi = self.addSwitch('s10')
        d2_host1 = self.addHost('h12')
        d2_host2 = self.addHost('h13')
        d2_host3 = self.addHost('h14')
        d2_host4 = self.addHost('h15')
        d2_host5 = self.addHost('h16')
        d2_host6 = self.addHost('h17')
        self.addLink(d2_sw1, d2_sw2)
        self.addLink(d2_sw1, d2_sw3)
        self.addLink(d2_sw1, d2_wifi)
        self.addLink(d2_sw2, d2_host1)
        self.addLink(d2_sw2, d2_host2)
        self.addLink(d2_sw3, d2_host3)
        self.addLink(d2_sw3, d2_host4)
        self.addLink(d2_wifi, d2_host5)
        self.addLink(d2_wifi, d2_host6)


        #Core
        core = self.addSwitch('s100')
        self.addLink(core, dmz_sw)
        self.addLink(core, apps_sw)
        self.addLink(core, d1_sw1)
        self.addLink(core, d2_sw1)


topos = { 'mytopo': ( lambda: MyTopo() ) }


def main():
    setLogLevel('info')
    network = Mininet(topo=MyTopo(), controller=partial( RemoteController, ip='127.0.0.1', port=6633 ))
    network.start()
    network.pingAll()
    CLI(network)

if __name__ == '__main__':
    main()

