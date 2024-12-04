"""initial

Revision ID: 9d09e1cb9b76
Revises: 
Create Date: 2024-10-14 09:33:50.162970

"""
from alembic import op
import sqlalchemy as sa

from project.core.config import settings

revision = '9d09e1cb9b76'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'Clients',
        sa.Column('client_id', sa.Integer(), nullable=False),
        sa.Column('full_name', sa.String().with_variant(sa.String(length=100), 'postgresql'), nullable=False),
        sa.Column('phone_number', sa.String().with_variant(sa.String(length=15), 'postgresql'), nullable=True),
        sa.Column('email', sa.String().with_variant(sa.String(length=100), 'postgresql'), nullable=True),
        sa.PrimaryKeyConstraint('client_id'),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'Products',
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('product_name', sa.String(100), nullable=False),
        sa.Column('expiry_date', sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint('product_id'),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'Suppliers',
        sa.Column('supplier_id', sa.Integer(), primary_key=True),
        sa.Column('supplier_name', sa.String(100), nullable=False),
        sa.Column('contact_info', sa.String(150), nullable=True),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'Deliveries',
        sa.Column('delivery_id', sa.Integer(), primary_key=True),
        sa.Column('supplier_id', sa.Integer(), sa.ForeignKey('suppliers.supplier_id', ondelete='CASCADE'),
                  nullable=False),
        sa.Column('delivery_date', sa.Date(), nullable=True),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'Delivery_items',
        sa.Column('item_id', sa.Integer(), nullable=False),
        sa.Column('delivery_id', sa.Integer(), sa.ForeignKey('deliveries.delivery_id', ondelete='CASCADE'),
                  nullable=False),
        sa.Column('product_id', sa.Integer(), sa.ForeignKey('products.product_id', ondelete='CASCADE'), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('unit_price', sa.Numeric(10, 2), nullable=False),
        sa.PrimaryKeyConstraint('item_id'),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'Recipes',
        sa.Column('recipe_id', sa.Integer(), sa.Identity(start=1), primary_key=True),
        sa.Column('dish_id', sa.Integer(), sa.ForeignKey('Dishes.dish_id', ondelete='CASCADE'), nullable=False),
        sa.Column('product_id', sa.Integer(), sa.ForeignKey('Products.product_id', ondelete='CASCADE'), nullable=False),
        sa.Column('quantity', sa.Numeric(10, 2), nullable=False),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('last_name', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('email', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('password', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('phone_number', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'Dishes',
        sa.Column('dish_id', sa.Integer(), sa.Identity(start=1), primary_key=True),
        sa.Column('dish_name', sa.String(100), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'Menu',
        sa.Column('menu_id', sa.Integer(), sa.Identity(start=1), primary_key=True),
        sa.Column('dish_id', sa.Integer(), sa.ForeignKey('dishes.dish_id', ondelete='CASCADE'), nullable=False),
        sa.Column('recipe_id', sa.Integer(), sa.ForeignKey('recipes.recipe_id', ondelete='CASCADE'), nullable=False),
        sa.Column('dish_name', sa.String(100), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'DishIngredients',
        sa.Column('record_id', sa.Integer(), sa.Identity(start=1), primary_key=True),
        sa.Column('recipe_id', sa.Integer(), sa.ForeignKey('recipes.recipe_id', ondelete='CASCADE'), nullable=False),
        sa.Column('product_id', sa.Integer(), sa.ForeignKey('products.product_id', ondelete='CASCADE'), nullable=False),
        sa.Column('quantity', sa.Numeric(10, 2), nullable=False),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'TableReservations',
        sa.Column('reservation_id', sa.Integer(), sa.Identity(start=1), primary_key=True),
        sa.Column('table_number', sa.Integer(), nullable=False),
        sa.Column('reservation_time', sa.TIMESTAMP(), nullable=False),
        sa.Column('client_id', sa.Integer(), sa.ForeignKey('clients.client_id', ondelete='CASCADE'), nullable=False),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'DiscountCards',
        sa.Column('discount_id', sa.Integer(), sa.Identity(start=1), primary_key=True),
        sa.Column('discount_percentage', sa.Numeric(5, 2), nullable=False),
        sa.Column('discount_conditions', sa.Text(), nullable=True),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'Orders',
        sa.Column('order_id', sa.Integer(), sa.Identity(start=1), primary_key=True),
        sa.Column('order_datetime', sa.TIMESTAMP(), nullable=False),
        sa.Column('client_id', sa.Integer(), sa.ForeignKey('clients.client_id', ondelete='CASCADE'), nullable=True),
        sa.Column('employee_id', sa.Integer(), sa.ForeignKey('employees.employee_id', ondelete='SET NULL'),
                  nullable=True),
        sa.Column('reservation_id', sa.Integer(),
                  sa.ForeignKey('table_reservations.reservation_id', ondelete='SET NULL'), nullable=True),
        sa.Column('discount_id', sa.Integer(), sa.ForeignKey('discount_cards.discount_id', ondelete='SET NULL'),
                  nullable=True),
        sa.Column('product_id', sa.Integer(), sa.ForeignKey('products.product_id', ondelete='SET NULL'), nullable=True),
        sa.Column('dish_id', sa.Integer(), sa.ForeignKey('dishes.dish_id', ondelete='SET NULL'), nullable=True),
        sa.Column('order_status', sa.String(50), nullable=True),
        sa.Column('total_price', sa.Numeric(10, 2), nullable=True),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'Employees',
        sa.Column('employee_id', sa.Integer(), sa.Identity(start=1), primary_key=True),
        sa.Column('full_name', sa.String(100), nullable=False),
        sa.Column('position', sa.String(100), nullable=True),
        sa.Column('hire_date', sa.Date(), nullable=True),
        schema=settings.POSTGRES_SCHEMA
    )

def downgrade():
    op.drop_table('Clients', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('Products', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('Suppliers', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('Deliveries', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('Delivery_items', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('Recipes', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('Dishes', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('Menu', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('DishIngredients', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('TableReservations', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('DiscountCards', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('Orders', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('Employees', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('users', schema=settings.POSTGRES_SCHEMA)
