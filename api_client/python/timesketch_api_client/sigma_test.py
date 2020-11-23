# Copyright 2020 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for the Timesketch API client"""
from __future__ import unicode_literals

import unittest
import mock

# TODO remove config
from . import test_lib
from . import client



class TimesketchSigmaTest(unittest.TestCase):
    """Test Sigma."""

    @mock.patch('requests.Session', test_lib.mock_session)
    def setUp(self):
        """Setup test case."""
        self.api_client = client.TimesketchApi(
            'http://127.0.0.1', 'test', 'test')
        self.rule = self.api_client.get_sigma_rule(
            "5266a592-b793-11ea-b3de-0242ac130004")
        self.rules = self.api_client.list_sigma_rules()

    def test_sigma_rule(self):
        """Test single Sigma rule."""

        self.assertIsNotNone(self.rule)

        self.assertEqual(
            self.rule.title, 'Suspicious Installation of Zenmap',
            "Title of the rule does not match")
        self.assertEqual(
            self.rule.id, '5266a592-b793-11ea-b3de-0242ac130004',
            "Id of the rule does not match")

    def test_sigma_rules(self):
        '''Testing the Sigma rules list'''

        self.assertIsNotNone(self.rules)
        self.assertEqual(self.rules['meta']['rules_count'], 2)
