"""create_phone_number_for_user_column

Revision ID: 50ec7b1b67a0
Revises: 
Create Date: 2024-03-03 21:17:03.470021

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50ec7b1b67a0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(table_name='users', column=sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column(table_name='users', column_name='phone_number')
