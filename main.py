# Programmers:  Donovan, Jalen
# Course:  CS151,
# Due Date: november 20th
# Lab Assignment:  lab10
# Problem Statement:
# Data In: file, decisons
# Data Out:  table, updsated file, highest or lowest
# Credits:
# Input Files: [description of the format of the input files you need for this program to work]


# Purpose:  use the table to write onto a file with proper formatting
# Parameters: output_filename, table
# Return: updated movies

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
            line += str(item) + ', '

        # Write line to the output file
        outfile.write(line + '\n')

    outfile.close()  # Close the file

# Purpose:  read the file into a table and change index 2 and 4 to integers
# Parameters: filename
# Return: table
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

# Purpose:  find the highest profit
# Parameters: table
# Return: movie line with the highest profit
def find_highest_profit(table):
    highest_profit_row = table[0]

    for row in table:
        if row[5] > highest_profit_row[5]:  # Assuming age is at index 3
            highest_profit_row = row

            # Create a line to the row
        highest_line = ''
        for item in row:
            highest_line += str(item) + ', '

    return highest_line

# Purpose:  find the lowest profit
# Parameters: table
# Return: movie line with the lowest profit
def find_lowest_profit(table):
    lowest_profit_row = table[0]

    for row in table:
        if row[5] < lowest_profit_row[5]:  # Assuming age is at index 3
            lowest_profit_row = row

        # Create a line to the row
        lowest_line = ''
        for item in row:
            lowest_line += str(item) + ', '



    return lowest_line

def main():
    table = read_to_file("/home/zyalew/Courses/FA_24_CS151/cs151-lab10-submissions/cs151-lab10-donovan_jalen/movies.csv")
    write_from_table(table, "updated_movies.csv")

    # determine which movie had either the highest profit or the lowest profi
    #ask the user to decide whether they want the highest or lowest
    user_decision = input('If you want to know the highest profit, type "x"\n'
          'If you want to know the lowest profit, type "y"\n')

    #error check
    while user_decision not in ['x', 'y']:
        user_decision = input('If you want to know the highest profit, type "x"\n'
                              'If you want to know the lowest profit, type "y"\n')
    #output based off of my decision
    if user_decision == 'x':
        highest = find_highest_profit(table)
        print(highest)

    elif user_decision == 'y':
        lowest = find_lowest_profit(table)
        print(lowest)
        #thank the user
    print('Thank you for using this program.')

main()