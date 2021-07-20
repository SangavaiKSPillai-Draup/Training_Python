"""
A dataclass is now created here to store information regarding mobiles
"""

from dataclasses import dataclass


@dataclass
class Mobile:
    id: str
    name: str
    series: str
    camera_mp: int
    battery_ah: int
    cost: float
