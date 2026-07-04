import sqlite3
import os

def init_database():
    os.makedirs('database', exist_ok=True)
    conn = sqlite3.connect('database/staynest.db')
    c = conn.cursor()

    # Create Properties Table
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

    # Insert Mock Data
    c.execute("SELECT COUNT(*) FROM properties")
    if c.fetchone()[0] == 0:
        sample_data = [
            ('Campus View PG', 'PG', 'Delhi', 12000, 4.8, True, True, 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=500', 'WiFi, Food, AC'),
            ('Cozy Studio Flat', 'Flat', 'Delhi', 18000, 4.5, True, False, 'https://images.unsplash.com/photo-1502672260266-1c1e522d4d2c?w=500', 'AC, Kitchen, Security'),
            ('Elite Student Housing', 'PG', 'Mumbai', 15000, 4.9, True, True, 'https://images.unsplash.com/photo-1554995207-c18c203602cb?w=500', 'WiFi, Food, AC, Laundry')
        ]
        c.executemany('''
            INSERT INTO properties (title, type, city, price, rating, is_verified, uni_partner, image_url, amenities)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', sample_data)
        
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_database()
