"""add few last columns to posts table

Revision ID: 76737cf5d053
Revises: 8e33d9275921
Create Date: 2024-02-05 23:24:04.365069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76737cf5d053'
down_revision = '8e33d9275921'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='True'))
    op.add_column('posts',sa.Column('created_AT',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
