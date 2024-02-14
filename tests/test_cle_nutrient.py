import unittest

from nutrient import CleNutrient


class CleNutrientTestCase(unittest.TestCase):
    def setUp(self):
        self.name = "A"
        self.total_gram = 150
        self.carbohydrate_g = 31.0
        self.carbohydrate_p = 21.0
        self.sugars_g = 2.0
        self.sugars_p = 5.0
        self.fat_g = 0.6
        self.fat_p = 2.0
        self.trans_fat_g = 0.0
        self.saturated_fat_g = 0.0
        self.cholesterol_g = 0.0
        self.protein_g = 8.0
        self.protein_p = 22.0
        self.cle = CleNutrient.create(
            self.name,
            self.total_gram,
            self.carbohydrate_g,
            self.carbohydrate_p,
            self.sugars_g,
            self.sugars_p,
            self.fat_g,
            self.fat_p,
            self.trans_fat_g,
            self.saturated_fat_g,
            self.cholesterol_g,
            self.protein_g,
            self.protein_p,
        )

    def test_calculate(self):
        per = 0.5
        calc = self.cle.calculate(self.cle.total_gram * per)
        self.assertEqual(
            calc.name,
            self.cle.name,
            f"이름 is not correct.",
        )
        self.assertEqual(
            calc.total_gram,
            self.cle.total_gram * per,
            f"무게 is not correct.",
        )
        self.assertEqual(
            calc.carbohydrate,
            (
                round(self.cle.carbohydrate[0] * per, self.cle._ndigits),
                round(self.cle.carbohydrate[1] * per, self.cle._ndigits),
            ),
            f"{calc._labels['carbohydrate']} is not correct.",
        )
        self.assertEqual(
            calc.sugars,
            (
                round(self.cle.sugars[0] * per, self.cle._ndigits),
                round(self.cle.sugars[1] * per, self.cle._ndigits),
            ),
            f"{calc._labels['sugars']} is not correct.",
        )
        self.assertEqual(
            calc.fat,
            (
                round(self.cle.fat[0] * per, self.cle._ndigits),
                round(self.cle.fat[1] * per, self.cle._ndigits),
            ),
            f"{calc._labels['fat']} is not correct.",
        )
        self.assertEqual(
            calc.trans_fat,
            (
                round(self.cle.trans_fat[0] * per, self.cle._ndigits),
                round(self.cle.trans_fat[1] * per, self.cle._ndigits),
            ),
            f"{calc._labels['trans_fat']} is not correct.",
        )
        self.assertEqual(
            calc.saturated_fat,
            (
                round(self.cle.saturated_fat[0] * per, self.cle._ndigits),
                round(self.cle.saturated_fat[1] * per, self.cle._ndigits),
            ),
            f"{calc._labels['saturated_fat']} is not correct.",
        )
        self.assertEqual(
            calc.cholesterol,
            (
                round(self.cle.cholesterol[0] * per, self.cle._ndigits),
                round(self.cle.cholesterol[1] * per, self.cle._ndigits),
            ),
            f"{calc._labels['cholesterol']} is not correct.",
        )
        self.assertEqual(
            calc.protein,
            (
                round(self.cle.protein[0] * per, self.cle._ndigits),
                round(self.cle.protein[1] * per, self.cle._ndigits),
            ),
            f"{calc._labels['protein']} is not correct.",
        )

    def test_create(self):
        self.assertEqual(
            self.cle.name,
            self.name,
            f"이름 is not correct.",
        )
        self.assertEqual(
            self.cle.total_gram,
            self.total_gram,
            f"무게 is not correct.",
        )
        self.assertEqual(
            self.cle.carbohydrate,
            (self.carbohydrate_g, self.carbohydrate_p),
            f"{self.cle._labels['carbohydrate']} is not correct.",
        )
        self.assertEqual(
            self.cle.sugars,
            (self.sugars_g, self.sugars_p),
            f"{self.cle._labels['sugars']} is not correct.",
        )
        self.assertEqual(
            self.cle.fat,
            (self.fat_g, self.fat_p),
            f"{self.cle._labels['fat']} is not correct.",
        )
        self.assertEqual(
            self.cle.trans_fat,
            (self.trans_fat_g, 0.0),
            f"{self.cle._labels['trans_fat']} is not correct.",
        )
        self.assertEqual(
            self.cle.saturated_fat,
            (self.saturated_fat_g, 0.0),
            f"{self.cle._labels['saturated_fat']} is not correct.",
        )
        self.assertEqual(
            self.cle.cholesterol,
            (self.cholesterol_g, 0.0),
            f"{self.cle._labels['cholesterol']} is not correct.",
        )
        self.assertEqual(
            self.cle.protein,
            (self.protein_g, self.protein_p),
            f"{self.cle._labels['protein']} is not correct.",
        )
