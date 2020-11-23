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
"""Timesketch API sigma library."""
from __future__ import unicode_literals

import json
import logging
import pandas

from . import error
from . import index
from . import resource

logger = logging.getLogger('timesketch_api.sigma')


class Sigma(resource.BaseResource):
    """Timesketch sigma object.

    A sigma object in Timesketch is a collection of one or more rules.

    Attributes:
        rule_uuid: The ID of the rule.
    """


    def __init__(self, rule_uuid, api ):
        """Initializes the Sigma object.

        Args:
            searchindex_id: Primary key ID of the searchindex.
            searchindex_name: Name of the searchindex (optional).
        """
        self.rule_uuid = rule_uuid
        self._resource_uri = 'sigma/{0:s}'.format(self.rule_uuid)
        super(Sigma, self).__init__(
            api=api, resource_uri=self._resource_uri)

    @property
    def es_query(self):
        """Returns the elastic search query."""
        sigma_data = self.data

        if not sigma_data:
            return []
        
        return_value = sigma_data.get('es_query')

        if not return_value:
            return []

        return return_value

    @property
    def title(self):
        """Returns the sigma rule title."""
        sigma_data = self.data

        if not sigma_data:
            return []

        title = sigma_data.get('title')

        if not title:
            return []

        return title
    
    @property
    def id(self):
        """Returns the sigma rule id."""
        sigma_data = self.data
        
        if not sigma_data:
            return []
            
        rule_uuid = sigma_data.get('id')

        if not rule_uuid:
            return []

        return rule_uuid

    def to_pandas(self):
        """Returns a pandas DataFrame."""
        panda_list = []
        sigma_data = self.data

        if not sigma_data:
            return []

        return pandas.DataFrame(sigma_data)
