import re

type_mapping = {
    "SERIAL": "INT AUTO_INCREMENT",
    "BIGSERIAL": "BIGINT AUTO_INCREMENT",
    "BOOLEAN": "TINYINT(1)",
    "BYTEA": "BLOB",
    "REAL": "FLOAT",
    "DOUBLE PRECISION": "DOUBLE",
    "NUMERIC": "DECIMAL",
    "DATE": "DATE",
    "TIMESTAMP": "DATETIME",
    "VARCHAR": "VARCHAR",
    "TEXT": "TEXT",
    "CHAR": "CHAR",
    "TIME": "TIME",
    "INTERVAL": "VARCHAR",  
    "CHARACTER VARYING": "VARCHAR",
}

# Function to convert PostgreSQL types to MySQL types
def convert_pg_to_mysql(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='UTF8') as f:
            content = f.read()

        # Replace PostgreSQL types with MySQL equivalents using regex
        for pg_type, mysql_type in type_mapping.items():
            content = re.sub(rf"\b{pg_type}\b", mysql_type, content, flags=re.IGNORECASE)

        # Open the output file (MySQL schema) and write the converted content
        with open(output_file, 'w', encoding='UTF8') as f:
            f.write(content)

        print(f"Conversion complete. Output written to: {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Ask the user for input and output file paths
input_file = input("Enter the path to your PostgreSQL schema file: ")
output_file = input("Enter the path for the converted MySQL schema file: ")


convert_pg_to_mysql(input_file, output_file)
