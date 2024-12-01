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

def downgrade():
    op.drop_table('Clients', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('Products', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('Suppliers', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('Deliveries', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('Delivery_items', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('users', schema=settings.POSTGRES_SCHEMA)
