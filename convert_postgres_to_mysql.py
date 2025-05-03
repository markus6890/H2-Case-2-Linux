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

def read_file(input_file):
    # Check if file ends with .gz and open accordingly
    if input_file.endswith('.gz'):
        print(f"Detected gzip-compressed file: {input_file}")
        with gzip.open(input_file, 'rt', encoding='ISO-8859-1') as f:
            return f.read()
    else:
        with open(input_file, 'r', encoding='ISO-8859-1') as f:
            return f.read()

# Function to convert PostgreSQL types to MySQL types
def convert_pg_to_mysql(input_file, output_file):
    try:
        content = read_file(input_file)

        # Replace PostgreSQL types with MySQL equivalents using regex (case-insensitive)
        for pg_type, mysql_type in type_mapping.items():
            content = re.sub(rf"\b{pg_type}\b", mysql_type, content, flags=re.IGNORECASE)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Conversion complete. Output written to: {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Ask the user for input and output file paths
input_file = input("Enter the path to your PostgreSQL schema file (.sql or .sql.gz): ")
output_file = input("Enter the path for the converted MySQL schema file: ")

# Call the function to convert
convert_pg_to_mysql(input_file, output_file)
