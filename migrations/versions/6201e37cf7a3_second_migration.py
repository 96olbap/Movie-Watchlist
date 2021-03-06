"""Second migration

Revision ID: 6201e37cf7a3
Revises: 2def1c5b79c5
Create Date: 2022-05-07 16:50:22.792013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6201e37cf7a3'
down_revision = '2def1c5b79c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
