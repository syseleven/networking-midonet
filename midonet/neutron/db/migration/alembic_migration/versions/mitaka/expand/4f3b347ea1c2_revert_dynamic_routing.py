# Copyright 2015 Midokura SARL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Revert dynamic routing

Revision ID: 4f3b347ea1c2
Revises: 29cbb88b092
Create Date: 2015-12-04 15:01:34.026502

"""

# revision identifiers, used by Alembic.
revision = '4f3b347ea1c2'
down_revision = '29cbb88b092'

from alembic import op


def upgrade():
    op.drop_table('midonet_advertise_route')
    op.drop_table('midonet_routing_peers')
    op.drop_table('midonet_routing_instances')
