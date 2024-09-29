class Command:

    @staticmethod
    def on_vpn():
        s = ('/ip ipsec/ policy/ disable  numbers=2',
             '/ip ipsec/ policy/ disable  numbers=3',
             '/ip ipsec/ policy/ disable  numbers=4',
             '/ip ipsec/ policy/ disable  numbers=5',
             'interface l2tp-server server set enabled=no',
             '/interface/wireguard/disable 0')
        return s

    @staticmethod
    def status_wg_vpn():
        s = ('/interface/wireguard/print',)
        return s

    @staticmethod
    def off_vpn():
        s = ('/ip ipsec/ policy/ enable  numbers=2',
             '/ip ipsec/ policy/ enable  numbers=3',
             '/ip ipsec/ policy/ enable  numbers=4',
             '/ip ipsec/ policy/ enable  numbers=5',
             'interface l2tp-server server set enabled=yes',
             '/interface/wireguard/enable 0')
        return s
