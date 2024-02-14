from .base import Nutrient


class CleNutrient(Nutrient):
    """Cle 영양소

    Examples:
        CleNutrient.create("A", 150, 31.0, 21, 2.0, 5, 0.6, 2, 0, 0, 0, 8.0, 22).calculate(120)
    """

    _ndigits = 1

    def __init__(
        self,
        name: str,
        total_gram=0,
        carbohydrate=(0.0, 0.0),
        sugars=(0.0, 0.0),
        fat=(0.0, 0.0),
        trans_fat=0.0,
        saturated_fat=0.0,
        cholesterol=0.0,
        protein=(0.0, 0.0),
    ):
        super().__init__(
            (
                "carbohydrate",
                "sugars",
                "fat",
                "trans_fat",
                "saturated_fat",
                "cholesterol",
                "protein",
            )
        )
        self.name = name
        self.total_gram = total_gram
        self.carbohydrate = carbohydrate
        self.sugars = sugars
        self.fat = fat
        self.trans_fat = (trans_fat, 0.0)
        self.saturated_fat = (saturated_fat, 0.0)
        self.cholesterol = (cholesterol, 0.0)
        self.protein = protein

    def __add__(self, other):
        cle = CleNutrient(
            f"{self.name}+{other.name}",
            self.total_gram + other.total_gram,
        )
        for attname in self._nutrient:
            g1, p1 = getattr(self, attname)
            g2, p2 = getattr(other, attname)
            setattr(
                cle,
                attname,
                (round(g1 + g2, cle._ndigits), round(p1 + p2, cle._ndigits)),
            )
        return cle

    def __radd__(self, *args, **kwargs):
        return self

    def __repr__(self):
        info = []
        for attname in ("carbohydrate", "fat", "protein"):
            g, p = getattr(self, attname)
            info.append(f"{self._labels[attname]}: {g}{self._units[attname]}, {p}%")
        return f"{self.__class__.__name__}({self.name}: {self.total_gram}g, {', '.join(info)})"

    def calculate(self, gram: int):
        cle_nutrient = CleNutrient(self.name, gram)
        per = gram / self.total_gram
        for attname in self._nutrient:
            g, p = getattr(self, attname)
            setattr(
                cle_nutrient,
                attname,
                (
                    round(g * per, cle_nutrient._ndigits),
                    round(p * per, cle_nutrient._ndigits),
                ),
            )
        return cle_nutrient

    @classmethod
    def create(
        cls,
        name: str,
        total_gram: int,
        carbohydrate_g: float,
        carbohydrate_p: float,
        sugars_g: float,
        sugars_p: float,
        fat_g: float,
        fat_p: float,
        trans_fat: float,
        saturated_fat: float,
        cholesterol: float,
        protein_g: float,
        protein_p: float,
    ):
        return cls(
            name,
            total_gram,
            (carbohydrate_g, carbohydrate_p),
            (sugars_g, sugars_p),
            (fat_g, fat_p),
            trans_fat,
            saturated_fat,
            cholesterol,
            (protein_g, protein_p),
        )
