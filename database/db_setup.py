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
            ('Lake View PG for Boys', 'PG', 'Govindpuram, Ghaziabad', 10000, 4.6, False, False,
             'https://images.unsplash.com/photo-1502672260266-1c1e522d4d2c?w=500',
             'WiFi, Housekeeping, Food, Laundry, Kitchen, Power Backup', 'Meera Chauhan', '+91-9763547314'),
            ('Campus View PG for Boys', 'PG', 'Saket, Delhi', 19500, 4.1, True, False,
             'https://images.unsplash.com/photo-1560185893-a55cbc8c57e8?w=500',
             'Food, Security, Housekeeping', 'Pooja Jain', '+91-9977655280'),
            ('Sunrise Studio Flat', 'Flat', 'DLF Phase 3, Gurugram', 15000, 4.8, True, False,
             'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=500',
             'Housekeeping, Food, WiFi, Laundry', 'Deepak Deshmukh', '+91-9467356163'),
            ('Star Student Home', 'PG', 'Raj Nagar Extension, Ghaziabad', 17500, 3.8, True, False,
             'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=500',
             'Geyser, CCTV, AC', 'Preeti Verma', '+91-9205145492'),
            ('Radhe Krishna PG for Boys', 'PG', 'Sushant Lok, Gurugram', 16000, 4.8, False, True,
             'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=500',
             'Security, Power Backup, Food, Laundry, Gym', 'Divya Tiwari', '+91-9743914923'),
            ('Silicon PG for Boys', 'PG', 'Sector 29, Gurugram', 23500, 4.4, False, False,
             'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=500',
             'Gym, Laundry, AC, Kitchen, Parking, WiFi', 'Suresh Jain', '+91-9147093944'),
            ('Prime Boys Hostel', 'PG', 'Munirka, Delhi', 25000, 5.0, True, False,
             'https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=500',
             'CCTV, Food, Kitchen', 'Rekha Yadav', '+91-9804787726'),
            ('Heritage Homes', 'Flat', 'Vaishali, Ghaziabad', 6000, 4.9, False, True,
             'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=500',
             'Kitchen, Food, Power Backup, Housekeeping', 'Karthik Nair', '+91-9494489954'),
            ('Green Valley Residency', 'Flat', 'NIT, Faridabad', 17500, 4.8, False, False,
             'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=500',
             'Geyser, Food, CCTV, Parking', 'Priya Yadav', '+91-9154013729'),
            ('Om Sai Girls Hostel', 'PG', 'Sector 29, Gurugram', 19500, 5.0, False, False,
             'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=500',
             'Housekeeping, Power Backup, Security, Gym', 'Kavita Aggarwal', '+91-9751793861'),
            ('Comfort Zone PG for Girls', 'PG', 'Kaushambi, Ghaziabad', 6500, 4.4, True, True,
             'https://images.unsplash.com/photo-1502672260266-1c1e522d4d2c?w=500',
             'Laundry, Food, WiFi', 'Manoj Deshmukh', '+91-9320828372'),
            ('Maa Bhagwati PG for Boys', 'PG', 'Sector 50, Noida', 24000, 4.4, True, False,
             'https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?w=500',
             'Food, Housekeeping, Security, Gym', 'Rohit Krishnan', '+91-9413135695'),
            ('Golden Nest Enclave', 'Flat', 'Govindpuram, Ghaziabad', 9000, 3.9, True, False,
             'https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?w=500',
             'Power Backup, Parking, Laundry, Food', 'Kavita Chopra', '+91-9336362921'),
            ('Sunrise PG for Boys', 'PG', 'Sahibabad, Ghaziabad', 11000, 4.2, True, False,
             'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=500',
             'Security, WiFi, Housekeeping, Power Backup', 'Sandeep Chandra', '+91-9838050733'),
            ('Old Town PG', 'PG', 'Karol Bagh, Delhi', 24500, 4.6, True, False,
             'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=500',
             'Kitchen, Housekeeping, AC, WiFi, Food, Security', 'Sunita Deshmukh', '+91-9355565632'),
            ('Balaji PG for Boys', 'PG', 'Munirka, Delhi', 24500, 4.4, True, False,
             'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=500',
             'Power Backup, Laundry, Gym, CCTV, Housekeeping', 'Gaurav Nair', '+91-9658344493'),
            ('Star Girls Hostel', 'PG', 'Sector 62, Noida', 24000, 5.0, True, True,
             'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=500',
             'Gym, Food, Laundry, Housekeeping', 'Deepak Joshi', '+91-9327178299'),
            ('Silicon PG for Girls', 'PG', 'NIT, Faridabad', 9500, 4.8, False, True,
             'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=500',
             'Housekeeping, Gym, Laundry, Power Backup', 'Shweta Patil', '+91-9121817959'),
            ('Campus View PG for Girls', 'PG', 'Udyog Vihar, Gurugram', 10000, 4.5, True, False,
             'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=500',
             'Kitchen, WiFi, Food, Geyser, AC, Power Backup', 'Amit Bhatia', '+91-9337307721'),
            ('Urban Roots PG for Girls', 'PG', 'Sector 29, Gurugram', 7000, 4.9, True, True,
             'https://images.unsplash.com/photo-1502672260266-1c1e522d4d2c?w=500',
             'Kitchen, Security, Geyser, AC, Laundry', 'Neha Chopra', '+91-9448223804'),
            ('Golden Nest Boys Hostel', 'PG', 'DLF Phase 3, Gurugram', 13500, 4.0, False, True,
             'https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=500',
             'Parking, Laundry, CCTV', 'Sandeep Iyer', '+91-9197751519'),
            ('Royal PG for Girls', 'PG', 'Sahibabad, Ghaziabad', 14500, 4.8, False, True,
             'https://images.unsplash.com/photo-1484154218962-a197022b5858?w=500',
             'CCTV, Kitchen, Gym, WiFi, Food, AC', 'Sunita Mehta', '+91-9214016934'),
            ('Shanti Niwas Heights', 'Flat', 'Indirapuram, Ghaziabad', 16000, 4.2, False, True,
             'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=500',
             'Power Backup, WiFi, Security, CCTV', 'Alok Chopra', '+91-9388032749'),
            ('Golden Nest Girls Hostel', 'PG', 'Sector 50, Noida', 16000, 4.5, True, False,
             'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=500',
             'CCTV, Security, Gym, Housekeeping, Power Backup', 'Lakshmi Gupta', '+91-9933379850'),
            ('Radhe Krishna Enclave', 'Flat', 'Mukherjee Nagar, Delhi', 6000, 4.0, True, False,
             'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=500',
             'Parking, Housekeeping, CCTV, Laundry, Geyser', 'Neha Shetty', '+91-9565916135'),
            ('Sunrise PG for Boys', 'PG', 'Old Faridabad, Faridabad', 15500, 3.9, True, True,
             'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=500',
             'Geyser, Food, Parking, Security, Laundry, Gym', 'Swati Patil', '+91-9271649597'),
            ('Hill Top PG for Boys', 'PG', 'Laxmi Nagar, Delhi', 11500, 4.7, False, False,
             'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=500',
             'Food, Parking, AC, CCTV', 'Alok Chauhan', '+91-9785241552'),
            ('Heritage Heights', 'Flat', 'Sushant Lok, Gurugram', 21000, 4.2, False, False,
             'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=500',
             'CCTV, Laundry, Power Backup, Parking, Food, Gym', 'Deepak Malhotra', '+91-9646197480'),
            ('Silicon PG for Boys', 'PG', 'Sector 137, Noida', 13000, 4.1, True, True,
             'https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?w=500',
             'Gym, Kitchen, Parking, Security, WiFi, Food', 'Anita Subramaniam', '+91-9398724849'),
            ('Campus View Apartments', 'Flat', 'NIT, Faridabad', 15500, 4.7, False, False,
             'https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?w=500',
             'Parking, Laundry, Power Backup, Security', 'Vivek Kumar', '+91-9696509626'),
            ('Silicon Studio Flat', 'Flat', 'Sector 29, Gurugram', 23000, 3.6, True, False,
             'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=500',
             'CCTV, Security, AC', 'Sandeep Joshi', '+91-9551093815'),
            ('Star PG for Girls', 'PG', 'Udyog Vihar, Gurugram', 16500, 4.7, True, False,
             'https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=500',
             'Power Backup, Food, Parking, WiFi, Kitchen, AC', 'Naveen Tiwari', '+91-9206207369'),
            ('Lake View PG for Boys', 'PG', 'Indirapuram, Ghaziabad', 21000, 4.5, True, True,
             'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=500',
             'Gym, AC, Geyser, Food, CCTV', 'Farhan Rao', '+91-9348543202'),
            ('Royal Heights', 'Flat', 'Sector 137, Noida', 12000, 3.7, False, False,
             'https://images.unsplash.com/photo-1502672260266-1c1e522d4d2c?w=500',
             'CCTV, Geyser, Food, WiFi, Gym', 'Preeti Krishnan', '+91-9813617981'),
            ('Campus View Boys Hostel', 'PG', 'Indirapuram, Ghaziabad', 21500, 3.7, False, False,
             'https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=500',
             'Housekeeping, AC, Security, CCTV, Power Backup, Parking', 'Preeti Yadav', '+91-9737157327'),
            ('Lake View PG', 'PG', 'Udyog Vihar, Gurugram', 14500, 4.8, True, False,
             'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=500',
             'Gym, WiFi, Parking, Housekeeping, AC, Laundry', 'Divya Iyer', '+91-9872163119'),
            ('Radhe Krishna PG', 'PG', 'Sector 15, Noida', 22500, 4.9, True, False,
             'https://images.unsplash.com/photo-1567016432779-094069958ea5?w=500',
             'Housekeeping, Parking, CCTV, Geyser', 'Meera Deshmukh', '+91-9226373219'),
            ('Shree Ram PG for Girls', 'PG', 'Sector 29, Gurugram', 21000, 4.4, True, False,
             'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=500',
             'Gym, Parking, Power Backup, Geyser, Kitchen', 'Naveen Rao', '+91-9409789263'),
            ('Ganga Nivas PG for Boys', 'PG', 'Sector 62, Noida', 21000, 4.0, True, False,
             'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=500',
             'Food, Laundry, Power Backup, CCTV, Gym', 'Sunita Chandra', '+91-9965070134'),
            ('Scholars Nest PG', 'PG', 'Sector 15, Faridabad', 23500, 4.0, False, False,
             'https://images.unsplash.com/photo-1541971875076-8f970d573be6?w=500',
             'Food, WiFi, Geyser, Power Backup, Parking, Laundry', 'Kavita Kapoor', '+91-9551562863'),
            ('Royal Boys Hostel', 'PG', 'DLF Phase 3, Gurugram', 8000, 4.4, False, True,
             'https://images.unsplash.com/photo-1541971875076-8f970d573be6?w=500',
             'Food, Laundry, Housekeeping, Kitchen, Security', 'Naveen Yadav', '+91-9753939924'),
            ('Shree Ram Boys Hostel', 'PG', 'Sushant Lok, Gurugram', 15500, 4.4, True, False,
             'https://images.unsplash.com/photo-1502672260266-1c1e522d4d2c?w=500',
             'CCTV, Laundry, Power Backup, Food', 'Neha Malhotra', '+91-9132240118'),
            ('Nova Apartments', 'Flat', 'Raj Nagar Extension, Ghaziabad', 7000, 3.9, False, False,
             'https://images.unsplash.com/photo-1567016432779-094069958ea5?w=500',
             'CCTV, Laundry, Power Backup', 'Karthik Krishnan', '+91-9161090020'),
            ('Balaji PG for Girls', 'PG', 'Kaushambi, Ghaziabad', 20000, 3.8, False, False,
             'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=500',
             'Parking, Food, Geyser, WiFi, Security, Gym', 'Arjun Ali', '+91-9207532196'),
            ('Elite Student Girls Hostel', 'PG', 'Kaushambi, Ghaziabad', 7000, 4.7, True, False,
             'https://images.unsplash.com/photo-1567016432779-094069958ea5?w=500',
             'AC, Geyser, Security, Parking, Food', 'Nisha Iyer', '+91-9704880902'),
            ('Golden Nest Boys Hostel', 'PG', 'Sector 62, Noida', 21500, 4.0, False, False,
             'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=500',
             'Parking, Food, Gym', 'Mahesh Kapoor', '+91-9861303538'),
            ('Sunshine Residency', 'Flat', 'Sector 15, Faridabad', 12000, 4.3, True, False,
             'https://images.unsplash.com/photo-1567016432779-094069958ea5?w=500',
             'Laundry, Power Backup, Kitchen', 'Lakshmi Chandra', '+91-9829392834'),
            ('Heritage PG for Girls', 'PG', 'Govindpuram, Ghaziabad', 23500, 3.6, True, True,
             'https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=500',
             'Parking, Food, AC', 'Vivek Bhosale', '+91-9832468718'),
            ('Lake View Homes', 'Flat', 'Sushant Lok, Gurugram', 23500, 3.8, True, False,
             'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=500',
             'Food, Power Backup, Security, Gym', 'Shweta Reddy', '+91-9452423316'),
            ('Fresh Start Homes', 'Flat', 'Sector 15, Noida', 23000, 4.3, True, False,
             'https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?w=500',
             'Gym, Laundry, CCTV, Security, Geyser, Kitchen', 'Anita Sharma', '+91-9693234261'),
            ('Silicon Girls Hostel', 'PG', 'Saket, Delhi', 24500, 4.1, True, False,
             'https://images.unsplash.com/photo-1502672260266-1c1e522d4d2c?w=500',
             'WiFi, AC, Security, CCTV, Food, Laundry', 'Mahesh Kapoor', '+91-9758685768'),
            ('Comfort Zone PG for Boys', 'PG', 'Sector 50, Noida', 15000, 5.0, False, False,
             'https://images.unsplash.com/photo-1502672260266-1c1e522d4d2c?w=500',
             'Parking, AC, Power Backup', 'Meera Sharma', '+91-9553599753'),
            ('Fresh Start Flat', 'Flat', 'Sector 15, Noida', 22500, 4.2, False, True,
             'https://images.unsplash.com/photo-1554995207-c18c203602cb?w=500',
             'Geyser, Security, Housekeeping', 'Snehal Patil', '+91-9161468593'),
            ('Riverside Heights', 'Flat', 'Udyog Vihar, Gurugram', 6000, 4.9, True, True,
             'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=500',
             'Food, Parking, Gym, Power Backup', 'Rohit Bhosale', '+91-9636913099'),
            ('Nova Residency', 'Flat', 'Sector 18, Noida', 13500, 4.1, True, True,
             'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=500',
             'WiFi, CCTV, Security, Power Backup, Housekeeping', 'Suresh Ali', '+91-9849545733'),
            ('Tech Park Student Home', 'PG', 'Sector 18, Noida', 12000, 4.5, False, False,
             'https://images.unsplash.com/photo-1484154218962-a197022b5858?w=500',
             'CCTV, Food, WiFi, Power Backup', 'Kavita Sharma', '+91-9778421782'),
            ('Sky Blue Student Home', 'PG', 'Dwarka, Delhi', 19000, 3.8, True, False,
             'https://images.unsplash.com/photo-1560185893-a55cbc8c57e8?w=500',
             'AC, Power Backup, Parking, CCTV, Gym', 'Karan Hegde', '+91-9513559522'),
            ('Radhe Krishna Apartments', 'Flat', 'Karol Bagh, Delhi', 8500, 4.7, True, False,
             'https://images.unsplash.com/photo-1567016432779-094069958ea5?w=500',
             'CCTV, Housekeeping, Power Backup, Security, Gym', 'Ananya Shetty', '+91-9629922473'),
            ('Tech Park Student Home', 'PG', 'Indirapuram, Ghaziabad', 8000, 4.5, True, False,
             'https://images.unsplash.com/photo-1484154218962-a197022b5858?w=500',
             'Food, AC, WiFi, Geyser, Power Backup, Laundry', 'Karan Rao', '+91-9330874509'),
            ('Maa Bhagwati Boys Hostel', 'PG', 'Sushant Lok, Gurugram', 24500, 4.6, True, False,
             'https://images.unsplash.com/photo-1502672260266-1c1e522d4d2c?w=500',
             'Geyser, Security, Power Backup, WiFi, Gym, Food', 'Kavita Hegde', '+91-9508260336')
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
