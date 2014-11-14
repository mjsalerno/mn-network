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
        dmz_sw = self.addSwitch('dmz_sw')
        dmz_srv = self.addHost('dmz_srv')
        dmz_fw = self.addHost('dmz_fw')

        self.addLink(dmz_sw, dmz_srv)
        self.addLink(dmz_sw, dmz_fw)



        #Apps
        apps_sw = self.addSwitch('apps_sw')
        apps_srv = self.addHost('apps_srv')
        apps_fw = self.addHost('apps_fw')

        self.addLink(apps_sw, apps_srv)
        self.addLink(apps_sw, apps_fw)



        #Dept 1
        d1_sw1 = self.addSwitch('d1_sw1')
        d1_sw2 = self.addSwitch('d1_sw2')
        d1_sw3 = self.addSwitch('d1_sw3')
        d1_wifi = self.addSwitch('d1_wifi')
        d1_host1 = self.addHost('d1_host1')
        d1_host2 = self.addHost('d1_host2')
        d1_host3 = self.addHost('d1_host3')
        d1_host4 = self.addHost('d1_host4')
        d1_host5 = self.addHost('d1_host5')
        d1_host6 = self.addHost('d1_host6')

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
        d2_sw1 = self.addSwitch('d2_sw1')
        d2_sw2 = self.addSwitch('d2_sw2')
        d2_sw3 = self.addSwitch('d2_sw3')
        d2_wifi = self.addSwitch('d2_wifi')
        d2_host1 = self.addHost('d2_host1')
        d2_host2 = self.addHost('d2_host2')
        d2_host3 = self.addHost('d2_host3')
        d2_host4 = self.addHost('d2_host4')
        d2_host5 = self.addHost('d2_host5')
        d2_host6 = self.addHost('d2_host6')

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
        core = self.addSwitch('core')
        self.addLink(core, dmz_sw)
        self.addLink(core, apps_sw)
        self.addLink(core, d1_sw1)
        self.addLink(core, d2_sw1)


topos = { 'mytopo': ( lambda: MyTopo() ) }