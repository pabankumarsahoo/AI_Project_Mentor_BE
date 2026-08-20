from datetime import datetime

from sqlalchemy import DateTime, Integer, Unicode, UnicodeText, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
	pass


class Project(Base):
	__tablename__ = "Projects"

	project_id: Mapped[int] = mapped_column(Integer, primary_key=True)
	project_name: Mapped[str] = mapped_column(Unicode(150), nullable=False)
	description: Mapped[str] = mapped_column(UnicodeText, nullable=False)
	technology_stack: Mapped[str] = mapped_column(Unicode(300), nullable=False)
	created_at: Mapped[datetime] = mapped_column(
		DateTime,
		nullable=False,
		server_default=text("sysdatetime()"),
	)
