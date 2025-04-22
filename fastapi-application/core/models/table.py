from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from .base import Base


class Table(Base):
    name: Mapped[str] = mapped_column(String(30))
    seats: Mapped[int] = mapped_column(Integer)
    location: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return (
            f"Table(id={self.id!r}, "
            f"name={self.name!r}, "
            f"seats={self.seats!r}, "
            f"location={self.location!r})"
        )
