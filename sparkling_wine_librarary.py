from sparkling_wine_list import sparkling_wine


def recommend_wine_by_type_and_budget(wine_type, min_budget, max_budget, recommended_wines, verbose=True):
    if not isinstance(min_budget, (int, float)) or not isinstance(max_budget, (int, float)):
        if verbose:
            print("Oh la-la! Money must be numeric.")
        return None

    if min_budget < 0 or max_budget < 0:
        if verbose:
            print("Oh la-la! Money cannot be negative.")
        return None

    if verbose:
        print(f"\n I am looking for the best {wine_type} within a budget of €{min_budget} to €{max_budget}...")

    # Filter wines
    filtered_wines = [
        wine for wine in sparkling_wine
        if type(wine).__name__ == wine_type
        and min_budget <= wine.price <= max_budget
        and wine not in recommended_wines
    ]

    if not filtered_wines:
        if verbose:
            print(f"Sorry, no wines of type '{wine_type}' are available within this budget range.")
        return None

    # Find the best wine
    best_wine = max(filtered_wines, key=lambda x: x.rating or 0, default=None)
    if best_wine:
        if verbose:
            print(f"I recommend: {best_wine}")
        return best_wine
    else:
        if verbose:
            print(f"Sorry, no wines of type '{wine_type}' within this budget range have a rating.")
        return None


def offer_another_suggestion(wine_type, min_budget, max_budget, recommended_wines, verbose=True):
    while True:
        repeat = input("\nContinue with more Sparkling wine magic and my recomendations? (yes/no): ").strip().lower()
        if repeat == 'yes':
            next_wine = recommend_wine_by_type_and_budget(wine_type, min_budget, max_budget, recommended_wines, verbose)
            if next_wine:
                recommended_wines.append(next_wine)
                print(f"Enjoy this new suggestion: {next_wine}")
            else:
                print("No more recommendations available within this budget range.")
                break
        elif repeat == 'no':
            print("Enjoy your sparkling wine! Have a wonderful evening! Ciao! 😊🍷")
            return True  
        else:
            print("Please respond with 'yes' or 'no'.")


def main(verbose=True):
    if verbose:
        print("Bonjour! My name is Zeev, a sommelier specializing in sparkling wines and a student of the Côte d'Azur MS program.")
        print("Today, I’ll help you find the perfect sparkling wine for your evening, tailored to your preferences and budget.\n")

    while True:
        wine_type = input("Which type of wine would you like? (Champagne/Cremant/Prosecco/Mousseux): ").strip()
        if wine_type in ['Champagne', 'Cremant', 'Prosecco', 'Mousseux']:
            while True:
                try:
                    min_budget = float(input("\nEnter your minimum budget (€): "))
                    max_budget = float(input("Enter your maximum budget (€): "))

                    if min_budget < 0 or max_budget < 0:
                        print("Budget values cannot be negative. Please try again.")
                        continue 

                    if min_budget > max_budget:
                        print("The minimum budget cannot be greater than the maximum budget. Please try again.")
                        continue  

                    break  
                except ValueError:
                    print("Invalid input. Please enter numerical values for the budget.")

            # Proceed with wine recommendation
            recommended_wines = []
            recommended_wine = recommend_wine_by_type_and_budget(wine_type, min_budget, max_budget, recommended_wines, verbose)
            if recommended_wine:
                recommended_wines.append(recommended_wine)
                should_exit = offer_another_suggestion(wine_type, min_budget, max_budget, recommended_wines, verbose)
                if should_exit:
                    break 
        else:
            print("Invalid wine type. Please choose from 'Champagne', 'Cremant', 'Prosecco' or 'Mousseux'.")

        repeat = input("\nContinue with more Sparkling wine magic? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Thank you! Ciao! 😊🍷")
            break


if __name__ == "__main__":
    main()
