"""empty message

Revision ID: 8499c3b35035
Revises: 2e41861425c8
Create Date: 2023-04-20 04:55:58.512579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8499c3b35035'
down_revision = '2e41861425c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###