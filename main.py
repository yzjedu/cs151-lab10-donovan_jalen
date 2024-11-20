# Programmers:  Donovan, Jalen
# Course:  CS151,
# Due Date: november 20th
# Lab Assignment:  lab10
# Problem Statement:
# Data In: file name
# Data Out:  table #, seat # and name from list
# Credits:
# Input Files: [description of the format of the input files you need for this program to work]


# Purpose:  reading file to table
# Parameters: file name
# Return: data

def write_from_table(table, output_filename):
    outfile = open(output_filename, 'w')  # Open file for writing

    for row in table:

        # Calculate birth year and title length
        profits = row[2] - row[4]

        # Add the birth year and title length to row
        row.append(profits)

        # Create a line to the row
        line = ''
        for item in row:
            line += str(item) + ' '

        # Write line to the output file
        outfile.write(line + '\n')

    outfile.close()  # Close the file


def read_to_file(filename):
    table = []

    try:
        file = open(filename, "r")
        for line in file:
            row = line.split(',')
            row[2] = int(row[2])  # Convert year to integer
            row[4] = int(row[4])  # Convert age to integer
            table.append(row)

        file.close()  # Close the file after reading

    except FileNotFoundError:
        print("File doesn’t exist")

    return table



def main():
    table = read_to_file("movies.csv")
    write_from_table(table, "updated_movies.csv")

main()