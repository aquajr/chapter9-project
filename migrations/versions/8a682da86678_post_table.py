"""post table

Revision ID: 8a682da86678
Revises: b3bc1fa67008
Create Date: 2023-11-03 16:46:37.085464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a682da86678'
down_revision = 'b3bc1fa67008'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('income',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('income', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_income_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_income_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('income', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_income_timestamp'))
        batch_op.drop_index(batch_op.f('ix_income_name'))

    op.drop_table('income')
    # ### end Alembic commands ###
