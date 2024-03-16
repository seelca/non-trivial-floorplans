#path: "C:/Users/silvi/Desktop/nexus/stream.txt"
#output: "C:/Users/silvi/Desktop/nexus/output.csv"

# Specify the filename for the input data file
input_filename = "C:/Users/silvi/Desktop/nexus/stream.txt"

# Specify the filename for the CSV file
output_filename = "C:/Users/silvi/Desktop/nexus/output.csv"

# Read data from the input file and write to CSV
with open(input_filename, mode="r") as txt_file, open(output_filename, mode="w", newline="") as csv_file:
    # Skip the header line
    next(txt_file)

    # Write the header to the CSV file
    header = "ID,Label,Source,Target\n"
    csv_file.write(header)

    # Loop through the txt data and write each row to the CSV file
    for line in txt_file:
        csv_file.write(line)

print(f'Data exported to {output_filename}')


