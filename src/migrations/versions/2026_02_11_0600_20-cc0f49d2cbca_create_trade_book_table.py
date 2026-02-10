"""create trade book table

Revision ID: cc0f49d2cbca
Revises: 744ddbf25ab6
Create Date: 2026-02-11 06:00:20.848348

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc0f49d2cbca'
down_revision: Union[str, Sequence[str], None] = '744ddbf25ab6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
