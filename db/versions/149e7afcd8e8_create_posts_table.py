"""create posts table

Revision ID: 149e7afcd8e8
Revises: 
Create Date: 2024-02-04 13:57:29.674092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '149e7afcd8e8'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
