from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.discountcard import DiscountCardSchema, DiscountCardCreateUpdateSchema
from project.infrastructure.postgres.models import DiscountCard
from project.core.exceptions import DiscountCardNotFound, DiscountCardAlreadyExists


class DiscountCardRepository:
    _collection: Type[DiscountCard] = DiscountCard

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_discount_cards(
        self,
        session: AsyncSession,
    ) -> list[DiscountCardSchema]:
        query = select(self._collection)

        discount_cards = await session.scalars(query)

        return [DiscountCardSchema.model_validate(obj=discount_card) for discount_card in discount_cards.all()]

    async def get_discount_card_by_id(
        self,
        session: AsyncSession,
        discount_card_id: int,
    ) -> DiscountCardSchema:
        query = (
            select(self._collection)
            .where(self._collection.id == discount_card_id)
        )

        discount_card = await session.scalar(query)

        if not discount_card:
            raise DiscountCardNotFound(_id=discount_card_id)

        return DiscountCardSchema.model_validate(obj=discount_card)

    async def create_discount_card(
        self,
        session: AsyncSession,
        discount_card: DiscountCardCreateUpdateSchema,
    ) -> DiscountCardSchema:
        query = (
            insert(self._collection)
            .values(discount_card.model_dump())
            .returning(self._collection)
        )

        try:
            created_discount_card = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise DiscountCardAlreadyExists(card_number=discount_card.card_number)

        return DiscountCardSchema.model_validate(obj=created_discount_card)

    async def update_discount_card(
        self,
        session: AsyncSession,
        discount_card_id: int,
        discount_card: DiscountCardCreateUpdateSchema,
    ) -> DiscountCardSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == discount_card_id)
            .values(discount_card.model_dump())
            .returning(self._collection)
        )

        updated_discount_card = await session.scalar(query)

        if not updated_discount_card:
            raise DiscountCardNotFound(_id=discount_card_id)

        return DiscountCardSchema.model_validate(obj=updated_discount_card)

    async def delete_discount_card(
        self,
        session: AsyncSession,
        discount_card_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == discount_card_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise DiscountCardNotFound(_id=discount_card_id)
