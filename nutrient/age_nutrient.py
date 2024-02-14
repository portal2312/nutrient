from .base import Nutrient, NutrientStatusEnum


class AgeNutrient(Nutrient):
    """나이 영양소

    Examples:
        from nutrient import AgeNutrient, CleNutrient
        foods = sum([
            CleNutrient.create("A", 150, 31.0, 21, 2.0, 5, 0.6, 2, 0, 0, 0, 8.0, 22),
            CleNutrient.create("B", 150, 9, 6, 5, 9, 7.5, 25, 0, 2, 29, 12, 35).calculate(30),
        ])
        AgeNutrient("Baby", 1).eat(foods)
    """

    _kcal_by_age = {
        1: 900,
    }
    _carbohydrate_by_age = {
        1: (130.0, 60.0),
    }
    _fat_by_age = {
        1: (15.0, 27.5),
    }
    _protein_by_age = {
        1: (20.0, 13.5),
    }
    _alias_age = {
        2: 1,
    }
    _ndigits = 1

    for alias, age in _alias_age.items():
        _kcal_by_age[alias] = _kcal_by_age[age]
        _carbohydrate_by_age[alias] = _carbohydrate_by_age[age]
        _fat_by_age[alias] = _fat_by_age[age]
        _protein_by_age[alias] = _protein_by_age[age]

    def __init__(self, name: str, age: int):
        super().__init__(("carbohydrate", "fat", "protein"))
        self.name = name
        self.age = age
        self.ra_carbohydrate = self._carbohydrate_by_age[age]
        self.ra_fat = self._fat_by_age[age]
        self.ra_protein = self._protein_by_age[age]
        self.carbohydrate = (0.0, 0.0)
        self.fat = (0.0, 0.0)
        self.protein = (0.0, 0.0)
        self.carbohydrate_status = NutrientStatusEnum.UNKNOWN
        self.fat_status = NutrientStatusEnum.UNKNOWN
        self.protein_status = NutrientStatusEnum.UNKNOWN

    def __repr__(self):
        info = []
        for attname in self._nutrient:
            label = self._labels[attname]
            ra_g, ra_p = getattr(self, f"ra_{attname}")
            g = getattr(self, attname)[0]
            p = round(ra_p * g / ra_g, self._ndigits)
            status = getattr(self, f"{attname}_status")
            info.append(f"{label}: {g}/{ra_g}g ({p}/{ra_p}%, {status.value})")
        return (
            f"{self.__class__.__name__}({self.name}, {self.age}세, {', '.join(info)})"
        )

    @classmethod
    def calculate_status(cls, ra, g):
        if ra < g:
            status = NutrientStatusEnum.OVER
        elif ra == g:
            status = NutrientStatusEnum.GOOD
        elif ra > g:
            status = NutrientStatusEnum.BAD
        else:
            status = NutrientStatusEnum.UNKNOWN
        return status

    def eat(self, obj):
        for attname in self._nutrient:
            ra_g, _ = getattr(self, f"ra_{attname}")
            g, p = getattr(obj, attname)
            setattr(self, attname, (g, p))
            setattr(self, f"{attname}_status", self.calculate_status(ra_g, g))
        return self
