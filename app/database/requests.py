from aiogram.loggers import event
from sqlalchemy import select

from app.database.models import User, async_session, Event


async def request_user_object(
        telegram_id: int,
        user_class="",
):
    async with async_session() as session:
        query = select(User).where(User.telegram_id == telegram_id)
        result = await session.execute(query)
        user = result.scalars().all()
        if not user:
            new_object = User(
                telegram_id=telegram_id,
                user_class=user_class,
            )
            session.add(new_object)
            await session.commit()
        else:
            return user[0]


async def get_events():
    async with async_session() as session:
        result = await session.execute(select(Event))
        events = result.scalars().all()
        return [[event.id, event.name] for event in events]


async def get_event(event_id: int):
    async with async_session() as session:
        result = await session.execute(select(Event).where(Event.id == event_id))
        event = result.scalars().all()
        return event[0]


async def add_user_to_event(user_id: int, event_id: int):
    async with async_session() as session:
        user = await session.get(User, user_id)
        event = await session.get(Event, event_id)
        if user and event:
            event.members.append(user)
            await session.commit()