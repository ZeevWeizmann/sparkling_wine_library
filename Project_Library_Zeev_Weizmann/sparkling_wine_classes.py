class SparklingWine:
    def __init__(self, name, price, rating, available_in_antibes, region):
        self.name = name
        self.price = price
        self.rating = rating
        self.available_in_antibes = available_in_antibes
        self.region = region

    def __str__(self):
        rating_str = f"rating: {self.rating}" if self.rating is not None else "rating unavailable"
        availability_str = "Available" if self.available_in_antibes else "Not available"
        return f"{self.name} (€{self.price}, {rating_str}, region: {self.region}, {availability_str})"

    def is_high_quality(self):
        return self.rating is not None and self.rating >= 4.5

class Champagne(SparklingWine):
    def __init__(self, name, price, rating, available_in_antibes):
        super().__init__(name, price, rating, available_in_antibes, region="Champagne")


class Cremant(SparklingWine):
    def __init__(self, name, price, rating, available_in_antibes, region="France"):
        super().__init__(name, price, rating, available_in_antibes, region=region)

class Prosecco(SparklingWine):
    def __init__(self, name, price, rating, available_in_antibes, region="Italy"):
        super().__init__(name, price, rating, available_in_antibes, region)

class Mousseux(SparklingWine):
    def __init__(self, name, price, rating, available_in_antibes, region="Various"):
        super().__init__(name, price, rating, available_in_antibes, region)



