# Explanation: Iterate over a list with enumerate(), printing items with their index.

favorite_foods = ["Pizza", "Sushi", "Burgers", "Pasta", "Salad"]
for index, food in enumerate(favorite_foods):
    print(f"{index + 1}. {food}")
