import unittest
import os.path
from FoodDB.FoodDB import FoodDB
from Food.Food import Food

class FoodDBTests(unittest.TestCase):
    def test_isFoodPresent(self):
        self.assertEqual(True, self.fdb.isPresent("Testing"))
        self.assertEqual(True, self.fdb.isPresent("TeSTinG"))

    def test_foodDoesNotExist(self):
        self.assertFalse(self.fdb.isPresent("test"))

    def test_getNutricion(self):
        self.assertEqual(["Testing", 100, 1, 2, 3, 4, 5, 6, 7, 8, 9.10], self.fdb.getFood("testing").getFoodNutricion())

    def test_dontCrashOnLackingValues(self):
        self.assertEqual(1, self.fdb.getFood("lacking").kcal)

    def test_createNutricionFile(self):
        fdb = FoodDB("tempFoodCsv.csv")
        self.assertTrue(os.path.isfile("tempFoodCsv.csv"))
        os.remove("tempFoodCsv.csv")

    def test_addFood(self):
        fdb = FoodDB("tempFoodCsv2.csv")
        food = Food("addedFood")
        fdb.addFood(food)
        food = Food("addedFood2")
        fdb.addFood(food)
        self.assertTrue(fdb.isPresent("addedFood"))
        self.assertTrue(fdb.isPresent("addedFood2"))
        os.remove("tempFoodCsv2.csv")

    def setUp(self):
        self.fdb = FoodDB("TestData/testCsv.csv")