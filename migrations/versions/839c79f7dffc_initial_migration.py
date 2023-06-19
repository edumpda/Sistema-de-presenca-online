"""initial migration

Revision ID: 839c79f7dffc
Revises: 
Create Date: 2023-05-20 09:59:33.538547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '839c79f7dffc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attendance')
    with op.batch_alter_table('class', schema=None) as batch_op:
        batch_op.alter_column('code',
               existing_type=sa.VARCHAR(length=4),
               nullable=True)
        batch_op.create_unique_constraint(None, ['code'])
        batch_op.drop_column('name')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('registration', sa.String(length=9), nullable=True))
        batch_op.add_column(sa.Column('password_hash', sa.String(length=64), nullable=True))
        batch_op.alter_column('role',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
        batch_op.create_unique_constraint(None, ['registration'])
        batch_op.drop_column('enrollment')
        batch_op.drop_column('username')
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=64), nullable=False))
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=20), nullable=False))
        batch_op.add_column(sa.Column('enrollment', sa.VARCHAR(length=9), nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('role',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
        batch_op.drop_column('password_hash')
        batch_op.drop_column('registration')

    with op.batch_alter_table('class', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=100), nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('code',
               existing_type=sa.VARCHAR(length=4),
               nullable=False)

    op.create_table('attendance',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('class_code', sa.VARCHAR(length=4), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###