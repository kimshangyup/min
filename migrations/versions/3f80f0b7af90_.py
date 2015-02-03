"""empty message

Revision ID: 3f80f0b7af90
Revises: None
Create Date: 2015-02-03 05:53:46.460718

"""

# revision identifiers, used by Alembic.
revision = '3f80f0b7af90'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shangyup')
    op.drop_table('user2')
    op.drop_table('ments')
    op.drop_table('posting')
    op.drop_table('posts')
    op.drop_table('user1')
    op.drop_table('yup')
    op.drop_table('post2')
    op.drop_table('post1')
    op.drop_table('users2')
    op.drop_table('users')
    op.drop_table('user5')
    op.drop_table('questions')
    op.drop_table('tabletest')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tabletest',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'tabletest_pkey')
    )
    op.create_table('questions',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'questions_pkey')
    )
    op.create_table('user5',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'user5_pkey')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'users_pkey')
    )
    op.create_table('users2',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'users2_pkey')
    )
    op.create_table('post1',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('body', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'user1.id'], name=u'post1_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'post1_pkey')
    )
    op.create_table('post2',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('body', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'user2.id'], name=u'post2_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'post2_pkey')
    )
    op.create_table('yup',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.Column('grade', sa.INTEGER(), autoincrement=False, nullable=True)
    )
    op.create_table('user1',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nickname', sa.VARCHAR(length=158), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'user1_pkey')
    )
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'posts_pkey')
    )
    op.create_table('posting',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('post_title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('post_text', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'posting_pkey')
    )
    op.create_table('ments',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('ment', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'ments_pkey')
    )
    op.create_table('user2',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'user2_pkey')
    )
    op.create_table('shangyup',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('nickname', sa.VARCHAR(), autoincrement=False, nullable=True)
    )
    ### end Alembic commands ###
