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
            type=int,
            autoincrement=True,
        ),
        sa.Column("date", type=datetime, nullable=False),
        sa.Column("xlabel", type=int, nullable=False),
        sa.Column("value", type=int, nullable=False),
        sa.Column("percentage", type=float, nullable=False),
        sa.Column("change", type=int, nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("price")
