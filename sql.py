import sqlite3

# Connect to database
connection=sqlite3.connect("retail_data.db")

# Create cursor object to interact with database
cursor=connection.cursor()

# Create table
table_info = """CREATE TABLE retail_data (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2),
    quantity_sold INT,
    total_sales DECIMAL(12, 2) AS (price * quantity_sold) STORED,
    customer_id INT,
    customer_name VARCHAR(100),
    customer_age INT,
    sale_date DATE,
    store_location VARCHAR(100)
);
"""

cursor.execute(table_info)

# Insert data into table
cursor.execute("""INSERT INTO retail_data (product_id, product_name, category, price, quantity_sold, customer_id, customer_name, customer_age, sale_date, store_location)
VALUES
(1, 'Smartphone A', 'Electronics', 299.99, 10, 101, 'John Doe', 34, '2024-09-01', 'New York'),
(2, 'Laptop B', 'Electronics', 899.99, 5, 102, 'Jane Smith', 29, '2024-09-02', 'Los Angeles'),
(3, 'T-shirt C', 'Apparel', 19.99, 50, 103, 'Alice Brown', 22, '2024-09-03', 'Chicago'),
(4, 'Headphones D', 'Electronics', 59.99, 15, 104, 'Bob Davis', 40, '2024-09-04', 'San Francisco'),
(5, 'Shoes E', 'Apparel', 49.99, 30, 105, 'Charlie Wilson', 28, '2024-09-05', 'Miami'),
(6, 'Watch F', 'Accessories', 199.99, 20, 106, 'David Miller', 33, '2024-09-06', 'Houston'),
(7, 'Smartwatch G', 'Electronics', 129.99, 18, 107, 'Eve Adams', 35, '2024-09-07', 'Boston'),
(8, 'Tablet H', 'Electronics', 399.99, 7, 108, 'Frank Garcia', 45, '2024-09-08', 'New York'),
(9, 'Jacket I', 'Apparel', 89.99, 25, 109, 'Grace Lee', 27, '2024-09-09', 'Chicago'),
(10, 'Jeans J', 'Apparel', 39.99, 40, 110, 'Hank Patel', 31, '2024-09-10', 'San Diego'),
(11, 'Bluetooth Speaker K', 'Electronics', 49.99, 12, 111, 'Ivy Martinez', 38, '2024-09-11', 'Dallas'),
(12, 'Gaming Console L', 'Electronics', 499.99, 3, 112, 'Jack Thomas', 42, '2024-09-12', 'Atlanta'),
(13, 'Sunglasses M', 'Accessories', 29.99, 35, 113, 'Karen Hernandez', 24, '2024-09-13', 'Las Vegas'),
(14, 'Perfume N', 'Beauty', 59.99, 28, 114, 'Larry Johnson', 37, '2024-09-14', 'Phoenix'),
(15, 'Handbag O', 'Accessories', 149.99, 10, 115, 'Mona Lewis', 29, '2024-09-15', 'Philadelphia'),
(16, 'Sweater P', 'Apparel', 69.99, 22, 116, 'Nina Clark', 26, '2024-09-16', 'Seattle'),
(17, 'Smart TV Q', 'Electronics', 699.99, 6, 117, 'Oscar White', 39, '2024-09-17', 'Denver'),
(18, 'Running Shoes R', 'Apparel', 59.99, 45, 118, 'Paul Walker', 36, '2024-09-18', 'Detroit'),
(19, 'Keyboard S', 'Electronics', 49.99, 8, 119, 'Quincy Young', 34, '2024-09-19', 'Austin'),
(20, 'Mouse T', 'Electronics', 24.99, 16, 120, 'Rachel Turner', 30, '2024-09-20', 'San Jose'),
(21, 'Headphones U', 'Electronics', 79.99, 10, 121, 'Steve Lee', 41, '2024-09-21', 'Washington DC'),
(22, 'Charger V', 'Electronics', 19.99, 50, 122, 'Tracy Adams', 23, '2024-09-22', 'Portland'),
(23, 'Shoes W', 'Apparel', 99.99, 20, 123, 'Uma Richards', 27, '2024-09-23', 'Orlando'),
(24, 'Jacket X', 'Apparel', 129.99, 15, 124, 'Victor Moore', 31, '2024-09-24', 'Nashville'),
(25, 'Shirt Y', 'Apparel', 29.99, 60, 125, 'Wendy Garcia', 25, '2024-09-25', 'Raleigh'),
(26, 'Blender Z', 'Appliances', 79.99, 12, 126, 'Xander Gomez', 43, '2024-09-26', 'Salt Lake City'),
(27, 'Microwave A1', 'Appliances', 99.99, 8, 127, 'Yasmine Carter', 38, '2024-09-27', 'Kansas City'),
(28, 'Air Fryer B1', 'Appliances', 129.99, 7, 128, 'Zane Collins', 32, '2024-09-28', 'Charlotte'),
(29, 'Vacuum C1', 'Appliances', 149.99, 6, 129, 'Alex Johnson', 40, '2024-09-29', 'Cleveland'),
(30, 'Coffee Maker D1', 'Appliances', 59.99, 20, 130, 'Brian Phillips', 33, '2024-09-30', 'Tampa'),
(31, 'Tablet E1', 'Electronics', 229.99, 9, 131, 'Carmen King', 36, '2024-09-29', 'Indianapolis'),
(32, 'Smartwatch F1', 'Electronics', 199.99, 12, 132, 'David Murphy', 30, '2024-09-28', 'Milwaukee'),
(33, 'Headphones G1', 'Electronics', 59.99, 18, 133, 'Ella Fisher', 28, '2024-09-27', 'Omaha'),
(34, 'Shirt H1', 'Apparel', 39.99, 55, 134, 'Frank Bell', 44, '2024-09-26', 'Columbus'),
(35, 'Pants I1', 'Apparel', 49.99, 40, 135, 'Gina Ward', 37, '2024-09-25', 'Cincinnati'),
(36, 'Socks J1', 'Apparel', 9.99, 100, 136, 'Harry Clark', 29, '2024-09-24', 'Buffalo'),
(37, 'Shoes K1', 'Apparel', 79.99, 30, 137, 'Ivy Flores', 34, '2024-09-23', 'Sacramento'),
(38, 'Sweater L1', 'Apparel', 89.99, 20, 138, 'Jackie Coleman', 32, '2024-09-22', 'Fresno'),
(39, 'Watch M1', 'Accessories', 299.99, 10, 139, 'Karen Brooks', 42, '2024-09-21', 'Louisville'),
(40, 'Laptop N1', 'Electronics', 1199.99, 4, 140, 'Leo Morris', 38, '2024-09-20', 'Baltimore'),
(41, 'Blender O1', 'Appliances', 49.99, 16, 141, 'Mary Ward', 31, '2024-09-19', 'Albuquerque'),
(42, 'Smartphone P1', 'Electronics', 799.99, 7, 142, 'Nick Reed', 27, '2024-09-18', 'Tucson'),
(43, 'Jeans Q1', 'Apparel', 59.99, 25, 143, 'Olivia Scott', 36, '2024-09-17', 'Mesa'),
(44, 'Bag R1', 'Accessories', 119.99, 18, 144, 'Patrick Sanders', 41, '2024-09-16', 'Long Beach'),
(45, 'Gaming Console S1', 'Electronics', 399.99, 8, 145, 'Quinn Stewart', 33, '2024-09-15', 'Virginia Beach'),
(46, 'Sunglasses T1', 'Accessories', 69.99, 25, 146, 'Rachel Martin', 29, '2024-09-14', 'Oklahoma City'),
(47, 'Handbag U1', 'Accessories', 199.99, 8, 147, 'Sarah Perry', 39, '2024-09-13', 'New Orleans'),
(48, 'T-shirt V1', 'Apparel', 19.99, 65, 148, 'Tom Harris', 26, '2024-09-12', 'San Antonio'),
(49, 'Shoes W1', 'Apparel', 89.99, 35, 149, 'Uma Ross', 34, '2024-09-11', 'Memphis'),
(50, 'Perfume X1', 'Beauty', 79.99, 12, 150, 'Victor Clark', 40, '2024-09-10', 'Atlanta'),
(51, 'Tablet Y1', 'Electronics', 499.99, 10, 151, 'Wendy Bell', 28, '2024-09-09', 'Jacksonville'),
(52, 'Sweater Z1', 'Apparel', 99.99, 14, 152, 'Xander Gomez', 27, '2024-09-08', 'Colorado Springs'),
(53, 'Smart TV A2', 'Electronics', 999.99, 5, 153, 'Yasmine Robinson', 35, '2024-09-07', 'Arlington'),
(54, 'Shoes B2', 'Apparel', 119.99, 20, 154, 'Zack Hunter', 38, '2024-09-06', 'Fort Worth'),
(55, 'Keyboard C2', 'Electronics', 49.99, 15, 155, 'Alex Johnson', 31, '2024-09-05', 'El Paso'),
(56, 'Mouse D2', 'Electronics', 29.99, 40, 156, 'Brian Cooper', 36, '2024-09-04', 'San Diego'),
(57, 'Jacket E2', 'Apparel', 149.99, 8, 157, 'Carmen Evans', 25, '2024-09-03', 'Las Vegas'),
(58, 'Blender F2', 'Appliances', 69.99, 12, 158, 'David Allen', 45, '2024-09-02', 'Phoenix'),
(59, 'Microwave G2', 'Appliances', 129.99, 5, 159, 'Ella Ward', 29, '2024-09-01', 'Portland'),
(60, 'Air Fryer H2', 'Appliances', 99.99, 7, 160, 'Frank Turner', 34, '2024-08-31', 'Seattle'),
(61, 'Vacuum I2', 'Appliances', 179.99, 6, 161, 'Grace Wright', 27, '2024-08-30', 'Boston'),
(62, 'Coffee Maker J2', 'Appliances', 79.99, 15, 162, 'Hank Taylor', 39, '2024-08-29', 'Detroit'),
(63, 'Jeans K2', 'Apparel', 49.99, 30, 163, 'Ivy Hall', 32, '2024-08-28', 'San Francisco'),
(64, 'Shirt L2', 'Apparel', 29.99, 70, 164, 'Jackie Wright', 28, '2024-08-27', 'Chicago'),
(65, 'T-shirt M2', 'Apparel', 14.99, 100, 165, 'Karen Bell', 23, '2024-08-26', 'Los Angeles'),
(66, 'Shoes N2', 'Apparel', 89.99, 40, 166, 'Leo Ward', 37, '2024-08-25', 'New York'),
(67, 'Watch O2', 'Accessories', 249.99, 8, 167, 'Mona Stewart', 40, '2024-08-24', 'San Antonio'),
(68, 'Sunglasses P2', 'Accessories', 59.99, 20, 168, 'Nick White', 33, '2024-08-23', 'Dallas'),
(69, 'Handbag Q2', 'Accessories', 129.99, 9, 169, 'Olivia Johnson', 31, '2024-08-22', 'Miami'),
(70, 'Perfume R2', 'Beauty', 69.99, 10, 170, 'Paul Thomas', 35, '2024-08-21', 'Philadelphia'),
(71, 'Smartphone S2', 'Electronics', 699.99, 6, 171, 'Quincy Lewis', 29, '2024-08-20', 'Austin'),
(72, 'Tablet T2', 'Electronics', 299.99, 8, 172, 'Rachel Lee', 41, '2024-08-19', 'Denver'),
(73, 'Smartwatch U2', 'Electronics', 149.99, 12, 173, 'Steve Clark', 30, '2024-08-18', 'Nashville'),
(74, 'Gaming Console V2', 'Electronics', 499.99, 7, 174, 'Tracy Turner', 28, '2024-08-17', 'Washington DC'),
(75, 'Bluetooth Speaker W2', 'Electronics', 69.99, 10, 175, 'Uma Roberts', 36, '2024-08-16', 'Raleigh'),
(76, 'Blender X2', 'Appliances', 59.99, 15, 176, 'Victor Nelson', 44, '2024-08-15', 'Salt Lake City'),
(77, 'Microwave Y2', 'Appliances', 109.99, 6, 177, 'Wendy Adams', 27, '2024-08-14', 'Tucson'),
(78, 'Air Fryer Z2', 'Appliances', 139.99, 5, 178, 'Xander Carter', 38, '2024-08-13', 'Cleveland'),
(79, 'Vacuum A3', 'Appliances', 199.99, 8, 179, 'Yasmine Ross', 45, '2024-08-12', 'Kansas City'),
(80, 'Coffee Maker B3', 'Appliances', 49.99, 20, 180, 'Zane Phillips', 32, '2024-08-11', 'Indianapolis'),
(81, 'Tablet C3', 'Electronics', 349.99, 9, 181, 'Alex Brooks', 29, '2024-08-10', 'Columbus'),
(82, 'Smartwatch D3', 'Electronics', 129.99, 12, 182, 'Brian Stewart', 31, '2024-08-09', 'Omaha'),
(83, 'Headphones E3', 'Electronics', 69.99, 18, 183, 'Carmen Wright', 35, '2024-08-08', 'Louisville'),
(84, 'Shirt F3', 'Apparel', 19.99, 65, 184, 'David Clark', 40, '2024-08-07', 'New Orleans'),
(85, 'Shoes G3', 'Apparel', 99.99, 25, 185, 'Ella Brooks', 33, '2024-08-06', 'Portland'),
(86, 'Perfume H3', 'Beauty', 59.99, 10, 186, 'Frank Lee', 28, '2024-08-05', 'Philadelphia'),
(87, 'Handbag I3', 'Accessories', 149.99, 8, 187, 'Grace Bell', 42, '2024-08-04', 'Phoenix'),
(88, 'Jacket J3', 'Apparel', 129.99, 15, 188, 'Hank Roberts', 36, '2024-08-03', 'Orlando'),
(89, 'Jeans K3', 'Apparel', 49.99, 40, 189, 'Ivy Harris', 27, '2024-08-02', 'Cleveland'),
(90, 'Shirt L3', 'Apparel', 29.99, 55, 190, 'Jack Cooper', 45, '2024-08-01', 'Las Vegas'),
(91, 'Bluetooth Speaker M3', 'Electronics', 79.99, 12, 191, 'Karen Nelson', 37, '2024-07-31', 'Chicago'),
(92, 'Laptop N3', 'Electronics', 999.99, 3, 192, 'Leo Collins', 41, '2024-07-30', 'Dallas'),
(93, 'Tablet O3', 'Electronics', 429.99, 6, 193, 'Mona Scott', 32, '2024-07-29', 'San Diego'),
(94, 'Smart TV P3', 'Electronics', 799.99, 4, 194, 'Nick Stewart', 34, '2024-07-28', 'Raleigh'),
(95, 'Watch Q3', 'Accessories', 199.99, 10, 195, 'Olivia Carter', 29, '2024-07-27', 'Salt Lake City'),
(96, 'Sunglasses R3', 'Accessories', 79.99, 20, 196, 'Paul Evans', 30, '2024-07-26', 'San Antonio'),
(97, 'Handbag S3', 'Accessories', 119.99, 10, 197, 'Quincy Hall', 40, '2024-07-25', 'Denver'),
(98, 'Perfume T3', 'Beauty', 89.99, 9, 198, 'Rachel Lee', 36, '2024-07-24', 'Portland'),
(99, 'Smartphone U3', 'Electronics', 799.99, 7, 199, 'Steve Clark', 42, '2024-07-23', 'Phoenix'),
(100, 'Gaming Console V3', 'Electronics', 599.99, 5, 200, 'Tom Harris', 31, '2024-07-22', 'Los Angeles');
""")

# Display records

print("The Inserted Records Are")

data = cursor.execute("SELECT * FROM retail_data")
for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()