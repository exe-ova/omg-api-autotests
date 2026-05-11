from pydantic import BaseModel


class KPIsResponse(BaseModel):
    total_revenue: float
    total_orders: int
    avg_order_value: float