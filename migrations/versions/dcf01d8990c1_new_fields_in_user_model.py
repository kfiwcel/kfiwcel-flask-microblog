"""new fields in user model

Revision ID: dcf01d8990c1
Revises: 51f5ccfba190
Create Date: 2020-06-08 19:10:20.309537

"""

# revision identifiers, used by Alembic.
revision = 'dcf01d8990c1'
down_revision = '51f5ccfba190'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar1', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar1')
    # ### end Alembic commands ###
