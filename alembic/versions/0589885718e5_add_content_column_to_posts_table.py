"""add content column to posts table

Revision ID: 0589885718e5
Revises: 4ba866b45586
Create Date: 2023-06-08 18:40:01.754194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0589885718e5'
down_revision = '4ba866b45586'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
