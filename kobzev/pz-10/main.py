# Туристические агентства предлагают следующие туры. Вожж – Мексика, Канада, Израиль, Италия, США. 
# РейнаТур – Англия, Япония, Канада, ЮАР. Радуга – США, Испания, Швеция, Австралия, Италия, Канада. 
# Определить:
# 1. в каких турагентствах можно одновременно приобрести туры в Италию и Канаду.
# 2. в турагенство РейнаТур добавить тур в Индию.
# 3. полный список всех туров.

tours = {
    'Вожж': {'Мексика', 'Канада', 'Израиль', 'Италия', 'США'},
    'РейнаТур': {'Англия', 'Япония', 'Канада', 'ЮАР'},
    'Радуга': {'США', 'Испания', 'Швеция', 'Австралия', 'Италия', 'Канада'}
}

# 1. Агентства с Италией и Канадой
italy_canada = [name for name, countries in tours.items() 
               if 'Италия' in countries and 'Канада' in countries]
print("1. Агентства с Италией и Канадой:", italy_canada)

# 2. Добавляем Индию в РейнаТур
tours['РейнаТур'].add('Индия')
print("2. После добавления Индии:", tours['РейнаТур'])

# 3. Полный список всех туров
all_tours = set().union(*tours.values())
print("3. Полный список всех туров:", sorted(all_tours))