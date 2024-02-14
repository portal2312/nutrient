from enum import Enum


class Nutrient:
    """영양소"""

    def __init__(self, nutrient):
        self._nutrient = nutrient
        self._labels = {
            name: {
                "carbohydrate": "탄수화물",
                "sugars": "당류",
                "fat": "지방",
                "trans_fat": "트랜스 지방",
                "saturated_fat": "포화 지방",
                "cholesterol": "콜레스테롤",
                "protein": "단백질",
            }[name]
            for name in nutrient
        }
        self._units = {
            name: {
                "carbohydrate": "g",
                "sugars": "g",
                "fat": "g",
                "trans_fat": "g",
                "saturated_fat": "g",
                "cholesterol": "mg",
                "protein": "g",
            }[name]
            for name in nutrient
        }


class NutrientStatusEnum(Enum):
    BAD = "부족"
    GOOD = "좋음"
    OVER = "과다"
    UNKNOWN = "알 수 없음"
