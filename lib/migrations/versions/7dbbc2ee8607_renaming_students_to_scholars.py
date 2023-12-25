"""Renaming students to scholars

Revision ID: 7dbbc2ee8607
Revises: 791279dd0760
Create Date: 2023-12-25 08:59:03.314522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7dbbc2ee8607'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
