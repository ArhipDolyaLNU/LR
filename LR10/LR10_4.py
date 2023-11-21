def grams_to_kilograms(grams):
    return grams / 1000


def kilograms_to_grams(kilograms):
    return kilograms * 1000


def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462


def pounds_to_kilograms(pounds):
    return pounds / 2.20462


def compare_weights(kg1, lb1, kg2, lb2):
    # Порівняння ваг за вагою в кілограмах
    if kg1 > kg2:
        return "Перший об'єкт важчий."
    elif kg1 < kg2:
        return "Другий об'єкт важчий."
    else:
        # Якщо ваги в кілограмах рівні, порівнюємо ваги в фунтах
        if lb1 > lb2:
            return "Перший об'єкт важчий."
        elif lb1 < lb2:
            return "Другий об'єкт важчий."
        else:
            return "Ваги однакові."


grams = 1000
kilograms = grams_to_kilograms(grams)
print(f"{grams} грам = {kilograms} кілограм")

pounds = 2.20462
kilograms = pounds_to_kilograms(pounds)
print(f"{pounds} фунтів = {kilograms} кілограм")

# Приклад порівняння ваг
weight1_kg = 10
weight1_lb = 22.0462
weight2_kg = 8
weight2_lb = 17.637
comparison_result = compare_weights(weight1_kg, weight1_lb, weight2_kg, weight2_lb)
print(comparison_result)
