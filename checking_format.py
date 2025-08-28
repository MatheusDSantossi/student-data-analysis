import csv
import unicodedata

def remove_accents(input_str):
    """Removes diacritical marks (accents) from a string."""
    
    def remove_accents(input_str):
        """Removes diacritical marks (accents) from a string."""
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return "".join([c for c in nfkd_form if not unicodedata.combining(c)])
    
    def process_csv_file(input_filepath, output_filepath, encoding='utf-8'):
        """Reads a CSV, removes accents from all fields, and writes to a new CSV."""
        with open(input_filepath, 'r', encoding=encoding, newline='') as infile, \
             open(output_filepath, 'w', encoding=encoding, newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
    
            for row in reader:
                processed_row = [remove_accents(field) for field in row]
                writer.writerow(processed_row)
    
    # Example usage:
    input_csv_file = 'input.csv'
    output_csv_file = 'output_no_accents.csv'
    
    # Create a sample input.csv for demonstration
    with open(input_csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'City', 'Description'])
        writer.writerow(['Frédéric', 'Montréal', 'This is a test with accents like é, à, ç.'])
        writer.writerow(['José', 'São Paulo', 'Another example with diacritics: ñ, ü.'])
    
    process_csv_file(input_csv_file, output_csv_file)
    print(f"Accents removed from '{input_csv_file}' and saved to '{output_csv_file}'.")
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def process_csv_file(input_filepath, output_filepath, encoding='utf-8'):
    """Reads a CSV, removes accents from all fields, and writes to a new CSV."""
    with open(input_filepath, 'r', encoding=encoding, newline='') as infile, \
         open(output_filepath, 'w', encoding=encoding, newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            processed_row = [remove_accents(field) for field in row]
            writer.writerow(processed_row)

# Example usage:
input_csv_file = 'alunos-por-cidade-de-origem.csv'
output_csv_file = 'output_no_accents.csv'



process_csv_file(input_csv_file, output_csv_file)
print(f"Accents removed from '{input_csv_file}' and saved to '{output_csv_file}'.")