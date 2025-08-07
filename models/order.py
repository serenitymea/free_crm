from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    project_name = Column(String)
    status = Column(String)
    _deadline = Column("deadline", DateTime)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    client = relationship("Client")

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        if isinstance(value, str):
            try:
                self._deadline = datetime.datetime.strptime(value, "%Y-%m-%d")
            except ValueError as exc:
                raise ValueError("Неверный формат даты. Используйте ГГГГ-ММ-ДД") from exc

        else:
            self._deadline = value
