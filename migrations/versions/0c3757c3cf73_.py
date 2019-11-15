"""empty message

Revision ID: 0c3757c3cf73
Revises: 
Create Date: 2019-11-14 23:44:07.311798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c3757c3cf73'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id_todo', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id_todo')
    )
    op.create_table('users',
    sa.Column('id_user', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('rol', sa.String(length=50), nullable=False),
    sa.Column('reset_password_token', sa.String(length=50), nullable=True),
    sa.Column('reset_password_expire', sa.DateTime(timezone=50), nullable=True),
    sa.PrimaryKeyConstraint('id_user'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('todos')
    # ### end Alembic commands ###
