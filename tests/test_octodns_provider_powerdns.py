#
#
#

from unittest import TestCase


class TestPowerDnsShim(TestCase):
    def test_missing(self):
        with self.assertRaises(ModuleNotFoundError):
            from octodns.provider.powerdns import PowerDnsProvider

            PowerDnsProvider
