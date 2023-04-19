"""empty message

Revision ID: 4161c0693b19
Revises: 50e839206aae
Create Date: 2023-04-18 21:39:15.645570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4161c0693b19'
down_revision = '50e839206aae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
