import sqlite3

try:
    # 1. Connect to the database
    conn = sqlite3.connect("company.db")
    
    # 2. CRITICAL: Enforce foreign key constraints for this connection
    conn.execute("PRAGMA foreign_keys = ON;")
    
    cursor = conn.cursor()
    
    # 3. Create the Parent Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
            dept_name TEXT NOT NULL
        )
    """)
    
    # 4. Create the Child Table with Foreign Key
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_name TEXT NOT NULL,
            department_id INTEGER,
            FOREIGN KEY (department_id) REFERENCES departments(dept_id)
        )
    """)
    conn.commit()
    
    # 5. Insert valid data
    cursor.execute("INSERT INTO departments (dept_name) VALUES ('Engineering')")
    valid_dept_id = cursor.lastrowid
    
    # This works because department_id exists
    cursor.execute("INSERT INTO employees (emp_name, department_id) VALUES ('Alice', ?)", (valid_dept_id,))
    conn.commit()
    print("Successfully inserted valid data.")

    # 6. Try to insert invalid data (Will throw an IntegrityError)
    print("Attempting to insert an employee with a non-existent department ID...")
    cursor.execute("INSERT INTO employees (emp_name, department_id) VALUES ('Bob', 999)")
    conn.commit()

except sqlite3.IntegrityError as e:
    print(f"Database error caught: {e}")

finally:
    if conn:
        conn.close()
