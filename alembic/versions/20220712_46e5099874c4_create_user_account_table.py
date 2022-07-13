"""create user account table

Revision ID: 46e5099874c4
Revises: a48d7e2b701d
Create Date: 2022-07-12 13:29:00.969006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46e5099874c4'
down_revision = 'a48d7e2b701d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.Unicode(10), comment='帳號'),
        sa.Column('email', sa.Unicode(15), comment='電子郵件信箱'),
        sa.Column('password', sa.Unicode(100)),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
        comment='使用者帳號表',
    )

    op.create_index(
        index_name='user_name_idx',
        table_name='user_account',
        columns=['username'],
    )

    op.create_index(
        index_name='email_idx',
        table_name='user_account',
        columns=['email'],
    )

def downgrade():
    op.drop_index('email_idx','user_account')
    op.drop_index('user_name_idx','user_account')
    op.drop_table('user_account')
