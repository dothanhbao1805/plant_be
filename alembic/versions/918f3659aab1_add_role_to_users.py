"""add role to users

Revision ID: 918f3659aab1
Revises: a72c1ce0486d
Create Date: 2026-04-02 15:01:35.304395

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "918f3659aab1"
down_revision: Union[str, Sequence[str], None] = "a72c1ce0486d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Tạo enum type bằng SQL thuần — chắc chắn nhất
    op.execute("CREATE TYPE userrole AS ENUM ('admin', 'user', 'moderator')")

    op.add_column(
        "users",
        sa.Column(
            "role",
            sa.Enum("admin", "user", "moderator", name="userrole"),
            nullable=False,
            server_default="user",
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_column("users", "role")
    op.execute("DROP TYPE userrole")
