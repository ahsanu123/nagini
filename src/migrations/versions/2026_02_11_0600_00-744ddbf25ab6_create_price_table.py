"""create price table

Revision ID: 744ddbf25ab6
Revises:
Create Date: 2026-02-11 06:00:00.407593

"""

from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "744ddbf25ab6"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "price",
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
            autoincrement=True,
        ),
        sa.Column("date", sa.DateTime, nullable=False),
        sa.Column("xlabel", sa.Integer, nullable=False),
        sa.Column("value", sa.Integer, nullable=False),
        sa.Column("percentage", sa.Float, nullable=False),
        sa.Column("change", sa.Integer, nullable=False),
        sa.Column("code", sa.String, nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("price")
