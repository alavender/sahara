# Copyright 2014 OpenStack Foundation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""add_job_exec_extra

Revision ID: 44f8293d129d
Revises: 001
Create Date: 2014-01-23 23:25:13.225628

"""

# revision identifiers, used by Alembic.
revision = '002'
down_revision = '001'

from alembic import op
import sqlalchemy as sa

from sahara.db.sqlalchemy import types as st


def upgrade():
    op.add_column('job_executions', sa.Column('extra', st.JsonEncoded(),
                                              nullable=True))


def downgrade():
    op.drop_column('job_executions', 'extra')