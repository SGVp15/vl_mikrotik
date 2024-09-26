from unittest import TestCase

from SSH_MIKROTIK.mikrotik_ssh import run_command_ssh


class Test(TestCase):
    def test_run_command_ssh(self):
        run_command_ssh(('/interface/wireguard',))
        self.fail()
