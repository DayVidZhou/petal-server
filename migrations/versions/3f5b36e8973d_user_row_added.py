"""user row added

Revision ID: 3f5b36e8973d
Revises: 9ea7400a848e
Create Date: 2019-03-06 22:04:25.195193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f5b36e8973d'
down_revision = '9ea7400a848e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('measurements', sa.Column('user', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('measurements', 'user')
    # ### end Alembic commands ###
