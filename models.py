from typing import Optional, Union
from pydantic import BaseModel

class Food(BaseModel):
    ingredients: str
    nutrition: Optional[str] = None


class FoodResponse(BaseModel):
    has_nuts: Optional[bool] = False
    has_onion: Optional[bool] = False
    has_garlic: Optional[bool] = False
    has_lactose: Optional[bool] = False
    has_allergen: Optional[bool] = False
    has_peanut: Optional[bool] = False
    has_sodium: Optional[bool] = False
    sodium_quantity: Optional[float] = 0
    sodiumu_percentage: Optional[float] = 0
    has_sugar: Optional[bool] = False
    sugar_quantity: Optional[float] = 0
    sugar_percentage: Optional[float] = 0
    has_carbs: Optional[bool] = False
    carbs_quantity: Optional[float] = 0
    carbs_percentage: Optional[float] = 0
    good_ingrediants: list = []
    bad_ingrediants: list = []
