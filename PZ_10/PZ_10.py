# Список товаров в каждом магазине
magaziny = {
    'Магнит': ['молоко', 'соль', 'сахар'],
    'Пятерочка': ['мясо', 'молоко', 'сыр'],
    'Перекресток': ['молоко', 'творог', 'сыр', 'сахар']
}

# 1. Магазины, где нельзя купить сыр
cheese_unavailable = []
for magazin, tovary in magaziny.items():
    if "сыр" not in tovary:
        cheese_unavailable.append(magazin)

print(f"Сыр нельзя купить в: {cheese_unavailable}")

# 2. Магазины, где можно купить молоко и сахар
milk_and_sugar = []
for magazin, tovary in magaziny.items():
    if "молоко" in tovary and "сахар" in tovary:
        milk_and_sugar.append(magazin)

print(f"Молоко и сахар можно купить в: {milk_and_sugar}")

# 3. Магазины, где можно купить соль
salt_available = []
for magazin, tovary in magaziny.items():
    if "соль" in tovary:
        salt_available.append(magazin)

print(f"Соль можно купить в: {salt_available}")
