import sqlite3

conn = sqlite3.connect('mushrooms.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Mushrooms (
        mushroom_id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        season TEXT,
        edible BOOLEAN,
        category_id INTEGER,
        primary_region_id INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Categories (
        category_id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Regions (
        region_id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        size DECIMAL
    )
''')

cursor.execute("INSERT INTO Categories (name, description) VALUES ('Трубчатые', 'Трубчатые грибы')")
cursor.execute("INSERT INTO Categories (name, description) VALUES ('Пластинчатые', 'Пластинчатые грибы')")
cursor.execute("INSERT INTO Regions (name, description, size) VALUES ('Лесной массив', 'Большой лес', 5000)")
cursor.execute("INSERT INTO Mushrooms (name, description, season, edible, category_id, primary_region_id) VALUES ('Белый гриб', 'Очень вкусный гриб', 'лето', TRUE, 1, 1)")

conn.commit()

def get_unique_regions():
    cursor.execute("""
        SELECT DISTINCT r.name
        FROM Regions r
        JOIN Mushrooms m ON r.region_id = m.primary_region_id;
    """)
    regions = cursor.fetchall()
    print("Уникальные регионы сбора грибов:")
    for region in regions:
        print(region[0])
    print()

def get_tubular_mushrooms():
    cursor.execute("""
        SELECT m.name, m.season, m.edible
        FROM Mushrooms m
        JOIN Categories c ON m.category_id = c.category_id
        WHERE c.name = 'Трубчатые';
    """)
    mushrooms = cursor.fetchall()
    print("Грибы из категории 'Трубчатые':")
    for mushroom in mushrooms:
        print(f"Название: {mushroom[0]}, Сезон: {mushroom[1]}, Съедобный: {'Да' if mushroom[2] else 'Нет'}")
    print()

def count_mushrooms_by_category():
    cursor.execute("""
        SELECT c.name AS category_name, COUNT(m.mushroom_id) AS mushroom_count
        FROM Categories c
        JOIN Mushrooms m ON c.category_id = m.category_id
        GROUP BY c.name
        ORDER BY mushroom_count DESC;
    """)
    categories = cursor.fetchall()
    print("Количество грибов в каждой категории:")
    for category in categories:
        print(f"Категория: {category[0]}, Количество: {category[1]}")
    print()

def get_edible_mushrooms_in_largest_regions():
    cursor.execute("""
        SELECT m.name, m.description
        FROM Mushrooms m
        JOIN Regions r ON m.primary_region_id = r.region_id
        WHERE m.edible = TRUE
        ORDER BY r.size DESC
        LIMIT 5;
    """)
    mushrooms = cursor.fetchall()
    print("Съедобные грибы в пяти самых больших регионах:")
    for mushroom in mushrooms:
        print(f"Название: {mushroom[0]}, Описание: {mushroom[1]}")
    print()

def get_spring_plated_mushrooms_in_small_regions():
    cursor.execute("""
        SELECT m.name
        FROM Mushrooms m
        JOIN Categories c ON m.category_id = c.category_id
        JOIN Regions r ON m.primary_region_id = r.region_id
        WHERE m.season = 'весна'
          AND c.name = 'Пластинчатые'
          AND r.size <= 6000;
    """)
    mushrooms = cursor.fetchall()
    print("Весенние 'Пластинчатые' грибы в небольших регионах (до 6000 условных единиц):")
    for mushroom in mushrooms:
        print(mushroom[0])
    print()

if __name__ == "__main__":
    get_unique_regions()
    get_tubular_mushrooms()
    count_mushrooms_by_category()
    get_edible_mushrooms_in_largest_regions()
    get_spring_plated_mushrooms_in_small_regions()