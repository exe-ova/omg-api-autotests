from pydantic import BaseModel
from typing import List, Literal
from datetime import date


class KPIsResponse(BaseModel):
    total_revenue: float
    total_orders: int
    avg_order_value: float

class OrderItem(BaseModel):
    id: int
    order_date: date
    customer_name: str
    product: str
    quantity: int
    revenue: float
    status: Literal["completed", "pending", "cancelled", "refunded"]

class OrdersResponse(BaseModel):
    orders: List[OrderItem]
    total: int
    page: int
    per_page: int

class RevenueChartItem(BaseModel):
    month: date
    revenue: float

RevenueChartResponse = List[RevenueChartItem]
