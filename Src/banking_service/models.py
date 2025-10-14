from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer

class Base(DeclarativeBase):
    pass
class BankUserDB(Base):
    __tablename__ = "banking_users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    pin: Mapped[int] = mapped_column(Integer, nullable=False)
    card: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    balance: Mapped[int] = mapped_column(Integer, nullable=False)
