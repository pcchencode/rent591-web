"""create guitar-song table

Revision ID: a48d7e2b701d
Revises: 
Create Date: 2022-07-11 15:21:11.695667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a48d7e2b701d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'guitar_song',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Unicode(10), comment='歌曲名稱'),
        sa.Column('author', sa.Unicode(15), comment='作者'),
        sa.Column('desc', sa.Unicode(100), comment='詳細描述'),
        sa.Column('url', sa.Unicode(500), comment='參考連結'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
        comment='吉他曲目分享表',
    )

def downgrade():
    op.drop_table('guitar_song')
