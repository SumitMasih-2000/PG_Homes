import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "staynest.db")


def init_database():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            type TEXT,
            city TEXT,
            price INTEGER,
            rating REAL,
            is_verified BOOLEAN,
            uni_partner BOOLEAN,
            image_url TEXT,
            amenities TEXT
        )
    ''')

    c.execute("SELECT COUNT(*) FROM properties")
    if c.fetchone()[0] == 0:
        sample_data = [
            ('Campus View PG', 'PG', 'Delhi', 12000, 4.8, True, True,
             'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=500',
             'WiFi, Food, AC'),
            ('Cozy Studio Flat', 'Flat', 'Delhi', 18000, 4.5, True, False,
             'https://images.unsplash.com/photo-1502672260266-1c1e522d4d2c?w=500',
             'AC, Kitchen, Security'),
            ('Elite Student Housing', 'PG', 'Mumbai', 15000, 4.9, True, True,
             'https://images.unsplash.com/photo-1554995207-c18c203602cb?w=500',
             'WiFi, Food, AC, Laundry'),
            ('Green Valley PG', 'PG', 'Bangalore', 9500, 4.3, True, False,
             'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=500',
             'WiFi, Food, Power Backup'),
            ('Skyline Residency', 'Flat', 'Mumbai', 22000, 4.6, True, False,
             'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=500',
             'AC, Gym, Security, Parking'),
            ('Scholars Nest PG', 'PG', 'Pune', 8500, 4.4, True, True,
             'https://images.unsplash.com/photo-1560185893-a55cbc8c57e8?w=500',
             'WiFi, Food, Laundry'),
            ('Urban Roots Flat', 'Flat', 'Bangalore', 16500, 4.2, False, False,
             'https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?w=500',
             'AC, Kitchen, Wifi'),
            ('The Study Hub PG', 'PG', 'Pune', 10200, 4.7, True, True,
             'https://images.unsplash.com/photo-1567016432779-094069958ea5?w=500',
             'WiFi, Food, AC, Gym'),
            ('Riverside Apartments', 'Flat', 'Hyderabad', 19500, 4.5, True, False,
             'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=500',
             'AC, Security, Power Backup'),
            ('Comfort Zone PG', 'PG', 'Hyderabad', 9000, 4.1, False, False,
             'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=500',
             'WiFi, Food'),
            ('Metro Living Flat', 'Flat', 'Delhi', 21000, 4.6, True, False,
             'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=500',
             'AC, Gym, Parking, Security'),
            ('Sunrise PG for Girls', 'PG', 'Mumbai', 13500, 4.8, True, True,
             'https://images.unsplash.com/photo-1484154218962-a197022b5858?w=500',
             'WiFi, Food, AC, Laundry, Security'),
        ]
        c.executemany('''
            INSERT INTO properties
            (title, type, city, price, rating, is_verified, uni_partner, image_url, amenities)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', sample_data)

    conn.commit()
    conn.close()


def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def get_all_properties():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM properties")
    rows = c.fetchall()
    cols = [d[0] for d in c.description]
    conn.close()
    return [dict(zip(cols, row)) for row in rows]


def get_cities():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT DISTINCT city FROM properties ORDER BY city")
    cities = [r[0] for r in c.fetchall()]
    conn.close()
    return cities


def search_properties(city=None, prop_type=None, max_price=None):
    conn = get_connection()
    c = conn.cursor()
    query = "SELECT * FROM properties WHERE 1=1"
    params = []
    if city and city != "All":
        query += " AND city = ?"
        params.append(city)
    if prop_type and prop_type != "All":
        query += " AND type = ?"
        params.append(prop_type)
    if max_price:
        query += " AND price <= ?"
        params.append(max_price)
    c.execute(query, params)
    rows = c.fetchall()
    cols = [d[0] for d in c.description]
    conn.close()
    return [dict(zip(cols, row)) for row in rows]


if __name__ == "__main__":
    init_database()
    print("Database initialized successfully.")
