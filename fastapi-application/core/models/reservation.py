from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime
from .table import Table


class Reservation(Base):
    customer_name: Mapped[str] = mapped_column(String(60))
    table_id: Mapped[int] = mapped_column(ForeignKey("table.id"))
    reservation_time: Mapped[DateTime] = mapped_column(DateTime)
    duration_minutes: Mapped[int] = mapped_column()

    table: Mapped["Table"] = relationship('Table',
                                          back_populates="reservations")

    def __repr__(self) -> str:
        return f"Reservation(id={self.id!r}, "\
               f"customer_name={self.customer_name!r}, " \
               f"table_id={self.table_id!r}, " \
               f"reservation_time={self.reservation_time!r}, " \
               f"duration_minutes={self.duration_minutes!r})"