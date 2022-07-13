"""add_constraint_username

Revision ID: 331967bc320f
Revises: 46e5099874c4
Create Date: 2022-07-13 16:03:41.333112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '331967bc320f'
down_revision = '46e5099874c4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint('uq_user_name', 'user_account', ['username'])


def downgrade() -> None:
    op.drop_constraint(constraint_name='uq_user_name', table_name='user_account', type_='unique')
