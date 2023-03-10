"""initial revision.

Revision ID: 622211feaeb0
Revises:
Create Date: 2022-10-09 09:14:35.591171
"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "622211feaeb0"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "author",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("dob", sa.Date(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("updated", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_author")),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("author")
    # ### end Alembic commands ###
