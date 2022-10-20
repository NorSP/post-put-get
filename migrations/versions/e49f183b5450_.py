"""empty message

Revision ID: e49f183b5450
Revises: dd49f2f7b318
Create Date: 2022-10-19 17:02:26.691835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e49f183b5450'
down_revision = 'dd49f2f7b318'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorite', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'favorite', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'favorite', type_='foreignkey')
    op.drop_column('favorite', 'user_id')
    # ### end Alembic commands ###
