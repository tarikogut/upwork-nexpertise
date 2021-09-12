import unittest

from lib import validate_zone


class DNSSecTest(unittest.TestCase):
    def valid_domain_test(self):
        validate_zone("nextpertise.nl")

    def unvalid_domain_test(self):
        validate_zone("aot.nl")

    def signed_but_dskeynotmatch(self):
        validate_zone("aot.nl")


if __name__ == '__main__':
    unittest.main()
