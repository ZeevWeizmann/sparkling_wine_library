import unittest
from sparkling_wine_librarary import recommend_wine_by_type_and_budget, sparkling_wine

class TestSparklingWineLibrary(unittest.TestCase):
    def setUp(self):
        self.sample_wine = sparkling_wine  # Use the imported wine list for testing
        self.recommended_wines = []

    def test_recommend_wine_with_valid_data(self):
        wine_type = "Champagne"
        min_budget = 5.0
        max_budget = 20.0
        wine = recommend_wine_by_type_and_budget(wine_type, min_budget, max_budget, self.recommended_wines, verbose=False)
        self.assertIsNotNone(wine, "The function should return a wine within the budget range.")
        self.assertEqual(wine.__class__.__name__, wine_type, "The wine type should match the input type.")
        self.assertTrue(min_budget <= wine.price <= max_budget, "The wine price should fall within the budget range.")

    def test_recommend_wine_with_no_matching_type(self):
        wine_type = "NonExistentType"
        min_budget = 5.0
        max_budget = 20.0
        wine = recommend_wine_by_type_and_budget(wine_type, min_budget, max_budget, self.recommended_wines, verbose=False)
        self.assertIsNone(wine, "The function should return None when no wines of the specified type are found.")

    def test_recommend_wine_with_no_matching_budget(self):
        wine_type = "Champagne"
        min_budget = 2.0
        max_budget = 3.0
        wine = recommend_wine_by_type_and_budget(wine_type, min_budget, max_budget, self.recommended_wines, verbose=False)
        self.assertIsNone(wine, "The function should return None when no wines match the budget range.")

    def test_recommend_wine_prevents_repeating(self):
        """Test that previously recommended wines are not repeated."""
        wine_type = "Champagne"
        min_budget = 5.0
        max_budget = 20.0

        first_wine = recommend_wine_by_type_and_budget(wine_type, min_budget, max_budget, self.recommended_wines, verbose=False)
        self.recommended_wines.append(first_wine)

        second_wine = recommend_wine_by_type_and_budget(wine_type, min_budget, max_budget, self.recommended_wines, verbose=False)
        self.assertNotEqual(first_wine, second_wine, "The function should not recommend the same wine twice.")
    def test_recommend_wine_with_negative_budget(self):
        """Test that the function handles negative budget values gracefully."""
        wine_type = "Champagne"
    
        min_budget = -5.0
        max_budget = 20.0
        recommended_wines = []
        wine = recommend_wine_by_type_and_budget(wine_type, min_budget, max_budget, recommended_wines, verbose=False)
        self.assertIsNone(wine, "The function should not return a wine when the budget is invalid.")

        min_budget = 5.0
        max_budget = -20.0
        wine = recommend_wine_by_type_and_budget(wine_type, min_budget, max_budget, recommended_wines, verbose=False)
        self.assertIsNone(wine, "The function should not return a wine when the budget is invalid.")

        min_budget = -5.0
        max_budget = -20.0
        wine = recommend_wine_by_type_and_budget(wine_type, min_budget, max_budget, recommended_wines, verbose=False)
        self.assertIsNone(wine, "The function should not return a wine when the budget is invalid.")
    def test_recommend_wine_with_invalid_budget_type(self):
        """Test that the function handles non-numeric budget values gracefully."""
        wine_type = "Champagne"

        min_budget = "five"
        max_budget = 20.0
        wine = recommend_wine_by_type_and_budget(wine_type, min_budget, max_budget, self.recommended_wines, verbose=False)
        self.assertIsNone(wine, "The function should return None when the minimum budget is not a number.")

        min_budget = 5.0
        max_budget = "twenty"
        wine = recommend_wine_by_type_and_budget(wine_type, min_budget, max_budget, self.recommended_wines, verbose=False)
        self.assertIsNone(wine, "The function should return None when the maximum budget is not a number.")

        min_budget = "five"
        max_budget = "twenty"
        wine = recommend_wine_by_type_and_budget(wine_type, min_budget, max_budget, self.recommended_wines, verbose=False)
        self.assertIsNone(wine, "The function should return None when both budget values are not numbers.")

if __name__ == "__main__":
    unittest.main()
