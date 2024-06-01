# Дан список игрушек. Некоторые игрушки из этого списка имеются в N детских садах.
# Определить, каких игрушек их этого списка нет ни в одном из детских садов и какие есть в
# каждом из них.

toys = {'машинка', 'мишка', 'кукла', 'вертолет'}

kindergarten_1 = {'машинка', 'кукла'}
kindergarten_2 = {'машинка', 'вертолет'}
kindergarten_3 = {'машинка', 'кукла', 'вертолет'}
kindergarten = kindergarten_1 | kindergarten_2 | kindergarten_3

for i in toys:
    if i not in kindergarten:
        noy = i


vse = kindergarten_1&kindergarten_2&kindergarten_3


print(f'игрушки которых нет в детских садах: {noy}\nигрушки которыен есть во всех детских садах: {vse}')

