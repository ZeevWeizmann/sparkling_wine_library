# Sparkling wine recommendation Library project

## "A bottle of wine contains more philosophy than all the books in the world." 😊🍷 — Louis Pasteur

## Author:

**Zeev Weizmann**  
Student, MSc Data Science and Artificial Intelligence
Université Côte d'Azur, France

## Data Source

Carrefour France (carrefour.fr)

## Overview

The Sparkling Wine Recommendation Project is an interactive Python application designed to help users find their perfect sparkling wine based on type, budget, and preferences. This project includes multiple Python modules and a suite of unit tests to ensure robust functionality.

## Modules

### 1. [sparkling_wine_classes.py](https://github.com/ZeevWeizmann/sparkling_wine_library/blob/main/sparkling_wine_classes.py)

This module defines the wine classes used in the project. Each wine type is represented as a class with attributes such as name, price, rating, and availability.

#### Features

- **Wine Classes**: Classes for various types of sparkling wines, such as Champagne, Prosecco, Cremant, and Mousseux.
- **Attributes**:
  - `name`: Name of the wine.
  - `price`: Price in euros.
  - `rating`: A numerical rating from 0 to 5.
  - `available`: Boolean indicating availability.

### 2. [sparkling_wine_list.py](https://github.com/ZeevWeizmann/sparkling_wine_library/blob/main/sparkling_wine_list.py)

This module contains a predefined list of sparkling wines as objects of the wine classes defined in `sparkling_wine_classes.py`.

#### Features

- A comprehensive list of wines, each initialized with its respective attributes (`name`, `price`, `rating`, and `available`).

### 3. [sparkling_wine_library.py](https://github.com/ZeevWeizmann/sparkling_wine_library/blob/main/sparkling_wine_librarary.py)

This is the core module of the project, containing functions for recommending wines based on user input.

#### Functions

- **recommend_wine_by_type_and_budget**:
  - Filters wines based on type, budget, and previously recommended wines.
  - Handles invalid inputs like non-numeric or negative budget values gracefully.
  - Outputs a recommendation or a message if no matching wine is found.
- **offer_another_suggestion**:
  - Allows users to request another recommendation without repeating previously suggested wines.

### 4. [test.py](https://github.com/ZeevWeizmann/sparkling_wine_library/blob/main/test.py)

This module contains unit tests to validate the functionality of the project.

#### Unit Tests

Run the unit tests to validate the functionality:  
`python -m unittest test.py`

#### Test Descriptions

- **test_recommend_wine_with_valid_data**: Ensures that a wine is recommended when valid inputs are provided. Tests filtering by wine type and budget.
- **test_recommend_wine_with_no_matching_type**: Verifies that the system correctly handles cases where no wine matches the specified type.
- **test_recommend_wine_with_no_matching_budget**: Tests the system's behavior when no wine falls within the specified budget range.
- **test_recommend_wine_prevents_repeating**: Ensures that previously recommended wines are not suggested again in the same session.
- **test_recommend_wine_with_negative_budget**: Confirms that the function handles negative budget values gracefully and does not return a recommendation.
- **test_recommend_wine_with_invalid_budget_type**: Verifies that the function handles non-numeric budget values correctly and does not attempt to process invalid inputs.

## How It Works

1. The user selects a wine type (e.g., Champagne, Prosecco, etc.).
2. The user enters a minimum and maximum budget.
3. The application recommends a wine based on the user's preferences.
4. The user can request another recommendation or exit the application.

### Example Usage

Run the application by executing the main script:  
`python sparkling_wine_library.py`

Interact with the program by following the prompts to select a wine type and budget. The system will provide tailored recommendations.

## Project Page

Explore the project online:  
[https://zeevweizmann.github.io/sparkling_wine_library/](https://zeevweizmann.github.io/sparkling_wine_library/)
