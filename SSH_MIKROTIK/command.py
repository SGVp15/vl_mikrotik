class Command:

    @staticmethod
    def on_vpn():
        s = []
        for i in range(2, 20):
            s.append(f'/ip ipsec/ policy/ disable  numbers={i}')

        s.append('/interface l2tp-server server set enabled=no')
        s.append('/interface/wireguard/disable 0')
        return s

    @staticmethod
    def status_wg_vpn():
        s = ('/interface/wireguard/print',)
        return s

    @staticmethod
    def off_vpn():
        s = []
        for i in range(2, 20):
            s.append(f'/ip ipsec/ policy/ enable  numbers={i}')

        s.append('/interface l2tp-server server set enabled=yes')
        s.append('/interface/wireguard/enable 0')
        return s
