"""add conntent column to post table

Revision ID: d90aa218a652
Revises: 149e7afcd8e8
Create Date: 2024-02-04 17:29:16.462252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd90aa218a652'
down_revision = '149e7afcd8e8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
