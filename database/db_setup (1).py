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
            amenities TEXT,
            owner_name TEXT,
            owner_contact TEXT
        )
    ''')

    c.execute("SELECT COUNT(*) FROM properties")
    if c.fetchone()[0] == 0:
        sample_data = [
            ('Campus View PG', 'PG', 'Delhi', 12000, 4.8, True, True,
             'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=500',
             'WiFi, Food, AC', 'Rajesh Kumar', '+91-98XXXXXX10'),
            ('Cozy Studio Flat', 'Flat', 'Delhi', 18000, 4.5, True, False,
             'https://images.unsplash.com/photo-1502672260266-1c1e522d4d2c?w=500',
             'AC, Kitchen, Security', 'Meera Sharma', '+91-98XXXXXX21'),
            ('Elite Student Housing', 'PG', 'Mumbai', 15000, 4.9, True, True,
             'https://images.unsplash.com/photo-1554995207-c18c203602cb?w=500',
             'WiFi, Food, AC, Laundry', 'Amit Deshmukh', '+91-98XXXXXX32'),
            ('Green Valley PG', 'PG', 'Bangalore', 9500, 4.3, True, False,
             'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=500',
             'WiFi, Food, Power Backup', 'Suresh Rao', '+91-98XXXXXX43'),
            ('Skyline Residency', 'Flat', 'Mumbai', 22000, 4.6, True, False,
             'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=500',
             'AC, Gym, Security, Parking', 'Priya Nair', '+91-98XXXXXX54'),
            ('Scholars Nest PG', 'PG', 'Pune', 8500, 4.4, True, True,
             'https://images.unsplash.com/photo-1560185893-a55cbc8c57e8?w=500',
             'WiFi, Food, Laundry', 'Vikram Joshi', '+91-98XXXXXX65'),
            ('Urban Roots Flat', 'Flat', 'Bangalore', 16500, 4.2, False, False,
             'https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?w=500',
             'AC, Kitchen, Wifi', 'Ananya Gupta', '+91-98XXXXXX76'),
            ('The Study Hub PG', 'PG', 'Pune', 10200, 4.7, True, True,
             'https://images.unsplash.com/photo-1567016432779-094069958ea5?w=500',
             'WiFi, Food, AC, Gym', 'Karan Malhotra', '+91-98XXXXXX87'),
            ('Riverside Apartments', 'Flat', 'Hyderabad', 19500, 4.5, True, False,
             'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=500',
             'AC, Security, Power Backup', 'Lakshmi Reddy', '+91-98XXXXXX98'),
            ('Comfort Zone PG', 'PG', 'Hyderabad', 9000, 4.1, False, False,
             'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=500',
             'WiFi, Food', 'Ravi Chandra', '+91-98XXXXXX09'),
            ('Metro Living Flat', 'Flat', 'Delhi', 21000, 4.6, True, False,
             'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=500',
             'AC, Gym, Parking, Security', 'Neha Kapoor', '+91-98XXXXXX18'),
            ('Sunrise PG for Girls', 'PG', 'Mumbai', 13500, 4.8, True, True,
             'https://images.unsplash.com/photo-1484154218962-a197022b5858?w=500',
             'WiFi, Food, AC, Laundry, Security', 'Sunita Iyer', '+91-98XXXXXX27'),
            ('Blue Nest PG', 'PG', 'Chennai', 8800, 4.2, True, False,
             'https://images.unsplash.com/photo-1502672023488-70e25813eb80?w=500',
             'WiFi, Food, Power Backup', 'Karthik Subramaniam', '+91-98XXXXXX36'),
            ('Marina View Flat', 'Flat', 'Chennai', 20500, 4.5, True, False,
             'https://images.unsplash.com/photo-1502672023488-70e25813eb80?w=500',
             'AC, Parking, Security', 'Divya Krishnan', '+91-98XXXXXX45'),
            ('Tech Park PG', 'PG', 'Bangalore', 11500, 4.6, True, True,
             'https://images.unsplash.com/photo-1560185008-a33f5c1a3b4b?w=500',
             'WiFi, Food, AC, Gym', 'Naveen Kumar', '+91-98XXXXXX54'),
            ('Lake View Residency', 'Flat', 'Pune', 17500, 4.4, True, False,
             'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=500',
             'AC, Kitchen, Parking', 'Snehal Patil', '+91-98XXXXXX63'),
            ('Heritage PG for Boys', 'PG', 'Jaipur', 7800, 4.0, False, False,
             'https://images.unsplash.com/photo-1541971875076-8f970d573be6?w=500',
             'WiFi, Food', 'Mahesh Singh', '+91-98XXXXXX72'),
            ('Pink City Flats', 'Flat', 'Jaipur', 14500, 4.3, True, False,
             'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=500',
             'AC, Security, Parking', 'Rekha Chauhan', '+91-98XXXXXX81'),
            ('Silicon Valley PG', 'PG', 'Bangalore', 13200, 4.7, True, True,
             'https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=500',
             'WiFi, Food, AC, Laundry, Gym', 'Deepak Hegde', '+91-98XXXXXX90'),
            ('Old Town PG', 'PG', 'Hyderabad', 8200, 3.9, False, False,
             'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=500',
             'WiFi, Food', 'Farhan Ali', '+91-98XXXXXX19'),
            ('Business Bay Flat', 'Flat', 'Mumbai', 25000, 4.7, True, False,
             'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=500',
             'AC, Gym, Security, Parking, Wifi', 'Arjun Mehta', '+91-98XXXXXX28'),
            ('Ganga Nivas PG', 'PG', 'Delhi', 9800, 4.3, True, True,
             'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=500',
             'WiFi, Food, AC', 'Manoj Tiwari', '+91-98XXXXXX37'),
            ('Whitefield Residency', 'Flat', 'Bangalore', 19800, 4.5, True, False,
             'https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?w=500',
             'AC, Kitchen, Security, Parking', 'Pooja Shetty', '+91-98XXXXXX46'),
            ('Fresh Start PG', 'PG', 'Pune', 8900, 4.1, False, True,
             'https://images.unsplash.com/photo-1560185893-a55cbc8c57e8?w=500',
             'WiFi, Food, Laundry', 'Sanjay Bhosale', '+91-98XXXXXX55'),
            ('Emerald Heights Flat', 'Flat', 'Hyderabad', 23000, 4.8, True, False,
             'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=500',
             'AC, Gym, Security, Parking', 'Swati Rao', '+91-98XXXXXX64'),
        ]
        c.executemany('''
            INSERT INTO properties
            (title, type, city, price, rating, is_verified, uni_partner, image_url, amenities, owner_name, owner_contact)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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


def add_property(title, prop_type, city, price, amenities, owner_name, owner_contact, image_url=None):
    conn = get_connection()
    c = conn.cursor()
    default_img = 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=500'
    c.execute('''
        INSERT INTO properties
        (title, type, city, price, rating, is_verified, uni_partner, image_url, amenities, owner_name, owner_contact)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (title, prop_type, city, price, 0.0, False, False, image_url or default_img, amenities, owner_name, owner_contact))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_database()
    print("Database initialized successfully.")
