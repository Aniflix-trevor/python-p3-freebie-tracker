"""create freebies table

Revision ID: 47fe58bffc79
Revises:
Create Date: 2025-05-27 12:30:02.602176

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "47fe58bffc79"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "freebies",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("item_name", sa.String(), nullable=False),
        sa.Column("value", sa.Integer(), nullable=False),
        sa.Column("dev_id", sa.Integer(), sa.ForeignKey("devs.id"), nullable=False),
        sa.Column(
            "company_id", sa.Integer(), sa.ForeignKey("companies.id"), nullable=False
        ),
    )


def downgrade():
    op.drop_table("freebies")

    def Division(num1,num2):
  while num2 != 0:
    remainder = num1 % num2
    num1 = num2
    num2 = remainder
  # code goes here
  return num1

# keep this function call here 
print(Division(input()))
