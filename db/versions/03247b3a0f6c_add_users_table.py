"""add users table

Revision ID: 03247b3a0f6c
Revises: d90aa218a652
Create Date: 2024-02-04 18:04:05.456582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03247b3a0f6c'
down_revision = 'd90aa218a652'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_AT',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
