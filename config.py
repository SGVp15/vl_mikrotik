import os.path

SYSTEMLOG = os.path.join(os.getcwd(), 'data', 'systemlog.txt')

ON_VPN_COMMAND = ('/ip ipsec/ policy/ disable  numbers=2',
                  '/ip ipsec/ policy/ disable  numbers=3',
                  '/ip ipsec/ policy/ disable  numbers=4',
                  '/ip ipsec/ policy/ disable  numbers=5',
                  'interface l2tp-server server set enabled=no',
                  '/interface/wireguard/disable 0')

OFF_VPN_COMMAND = ('/ip ipsec/ policy/ enable  numbers=2',
                   '/ip ipsec/ policy/ enable  numbers=3',
                   '/ip ipsec/ policy/ enable  numbers=4',
                   '/ip ipsec/ policy/ enable  numbers=5',
                   'interface l2tp-server server set enabled=yes',
                   '/interface/wireguard/enable 0')
