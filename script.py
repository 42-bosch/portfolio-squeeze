import psycopg2

# Define your data to be inserted into the database
data = [
    {"maker": "Acura", "quantity": 55, "year_birth": 1986},
    {"maker": "Alfa Romeo", "quantity": 17, "year_birth": 1910},
    {"maker": "Alpheon", "quantity": 1, "year_birth": 2010},
    {"maker": "Audi", "quantity": 93, "year_birth": 1909},
    {"maker": "AVGM", "quantity": 3, "year_birth": 2001},
    {"maker": "Bentley", "quantity": 20, "year_birth": 1919},
    {"maker": "BMW", "quantity": 158, "year_birth": 1916},
    {"maker": "Buick", "quantity": 219, "year_birth": 1903},
    {"maker": "Cadillac", "quantity": 180, "year_birth": 1902},
    {"maker": "Chevrolet", "quantity": 515, "year_birth": 1911},
    {"maker": "Chrysler", "quantity": 56, "year_birth": 1925},
    {"maker": "Daewoo", "quantity": 6, "year_birth": 1937},
    {"maker": "Dodge", "quantity": 119, "year_birth": 1900},
    {"maker": "Ferrari", "quantity": 7, "year_birth": 1939},
    {"maker": "Fiat", "quantity": 30, "year_birth": 1899},
    {"maker": "Ford", "quantity": 297, "year_birth": 1903},
    {"maker": "Freightliner", "quantity": 2, "year_birth": 1942},
    {"maker": "Geo", "quantity": 5, "year_birth": 1989},
    {"maker": "GM", "quantity": 3, "year_birth": 1908},
    {"maker": "GMC", "quantity": 173, "year_birth": 1911},
    {"maker": "Holden", "quantity": 183, "year_birth": 1856},
    {"maker": "Honda", "quantity": 97, "year_birth": 1948},
    {"maker": "HSV", "quantity": 44, "year_birth": 1987},
    {"maker": "Hummer", "quantity": 13, "year_birth": 1992},
    {"maker": "Infiniti", "quantity": 60, "year_birth": 1989},
    {"maker": "Isuzu", "quantity": 14, "year_birth": 1916},
    {"maker": "Jeep", "quantity": 89, "year_birth": 1941},
    {"maker": "Karma", "quantity": 3, "year_birth": 2014},
    {"maker": "Lamborghini", "quantity": 17, "year_birth": 1963},
    {"maker": "Lancia", "quantity": 10, "year_birth": 1906},
    {"maker": "Lexus", "quantity": 18, "year_birth": 1989},
    {"maker": "Lincoln", "quantity": 94, "year_birth": 1917},
    {"maker": "Maserati", "quantity": 26, "year_birth": 1914},
    {"maker": "Mazda", "quantity": 96, "year_birth": 1920},
    {"maker": "Mercedes-Benz", "quantity": 138, "year_birth": 1926},
    {"maker": "Mercury", "quantity": 31, "year_birth": 1938},
    {"maker": "MINI", "quantity": 41, "year_birth": 1959},
    {"maker": "Mitsubishi", "quantity": 41, "year_birth": 1870},
    {"maker": "Nissan", "quantity": 157, "year_birth": 1933},
    {"maker": "Oldsmobile", "quantity": 54, "year_birth": 1897},
    {"maker": "Opel", "quantity": 6, "year_birth": 1862},
    {"maker": "Pagani", "quantity": 2, "year_birth": 1992},
    {"maker": "Pontiac", "quantity": 122, "year_birth": 1926},
    {"maker": "Porsche", "quantity": 8, "year_birth": 1931},
    {"maker": "RAM", "quantity": 37, "year_birth": 2010},
    {"maker": "Rolls-Royce", "quantity": 33, "year_birth": 1904},
    {"maker": "Saab", "quantity": 9, "year_birth": 1945},
    {"maker": "Saturn", "quantity": 36, "year_birth": 1985},
    {"maker": "Scion", "quantity": 8, "year_birth": 2003},
    {"maker": "Smart", "quantity": 6, "year_birth": 1994},
    {"maker": "SRT", "quantity": 3, "year_birth": 1989},
    {"maker": "Sterling", "quantity": 2, "year_birth": 1997},
    {"maker": "Subaru", "quantity": 75, "year_birth": 1953},
    {"maker": "Suzuki", "quantity": 28, "year_birth": 1909},
    {"maker": "Toyota", "quantity": 121, "year_birth": 1937},
    {"maker": "Volkswagen", "quantity": 151, "year_birth": 1937},
    {"maker": "Volvo", "quantity": 47, "year_birth": 1927}
]

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="db_api",
    user="postgres",
    password="password"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Iterate through your data and execute INSERT queries
for item in data:
    maker = item["maker"]
    quantity = item["quantity"]
    year_birth = item["year_birth"]
    
    query = f"INSERT INTO cars (maker, quantity, year_birth) VALUES ('{maker}', {quantity}, {year_birth})"
    cursor.execute(query)

# Commit the changes and close the connection
conn.commit()
conn.close()
