# coding: utf-8

"""
    Workplace Console API

    API for managing email and workplace service subscriptions.

    The version of the OpenAPI document: v1
    Contact: support@truehost.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from workplace_client.models.dns_record import DnsRecord

class TestDnsRecord(unittest.TestCase):
    """DnsRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DnsRecord:
        """Test DnsRecord
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DnsRecord`
        """
        model = DnsRecord()
        if include_optional:
            return DnsRecord(
                host = '',
                type = '',
                value = '',
                priority = '',
                ttl = 56
            )
        else:
            return DnsRecord(
                host = '',
                type = '',
                value = '',
                priority = '',
                ttl = 56,
        )
        """

    def testDnsRecord(self):
        """Test DnsRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
