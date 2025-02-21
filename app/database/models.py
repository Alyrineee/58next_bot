from sqlalchemy import Column, String, BigInteger, DateTime, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config import DB_URL


engine = create_async_engine(url=DB_URL)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


event_members = Table(
    "event_members",
    Base.metadata,
    Column("user_id", BigInteger, ForeignKey("User.telegram_id"), primary_key=True),
    Column("event_id", BigInteger, ForeignKey("Event.id"), primary_key=True)
)


class User(Base):
    __tablename__ = 'User'
    telegram_id = Column(BigInteger, primary_key=True, unique=True)
    user_class = Column("class", String(10))

    events: Mapped[list["Event"]] = relationship(
        "Event",
        secondary=event_members,
        back_populates="members"
    )


class Event(Base):
    __tablename__ = "Event"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50))
    description = Column(String(250))
    date_of_start = Column(DateTime)
    date_of_end = Column(DateTime)

    members: Mapped[list["User"]] = relationship(
        "User",
        secondary=event_members,
        back_populates="events",
        lazy="selectin"
    )


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)