# Algorithm Document

#### THINK before you code...
#### Write down the list of tasks to help you think

### Purpose: reading file 
    ### Name: read_file_to_table
    ### Parameters: file
    ### Return: table 
    ### Algorithm: 
1. create an empty table
2. try
   1. open the file for reading
   2. for every line in the file
      1. the row is split by every ','
      2. typecast row index 2 to an int
      3. typecast row index 4 to an int
      4. append the table
   3. except if the file isn't found
      1. output the file doesn't exist
3. return the table

### Purpose: finding the highest movie 
    ### Name: find_highest_profit
    ### Parameters: table
    ### Return: highest profit movie row 
    ### Algorithm: 
1. set the highest row to the first row of the table
2. for every row in the table
   1. if the row index 5 is greater than highest profit index 5 
   2. the highest row is that row
3. format the row
1. return the highest row

### Purpose: finding the lowest movie 
    ### Name: find_lowest_profit
    ### Parameters: table
    ### Return: lowest profit movie row 
    ### Algorithm: 
1. set the lowest row to the first row of the table
2. for every row in the table
   1. if the row index 5 is greater than lowest profit index 5 
   2. the lowest row is that row
3. format the row
1. return the lowest row


### Purpose: update the table and write it into a file
    ### Name: write_from_table
    ### Parameters: table
    ### Return: file name
    ### Algorithm: 
1. open the file for writing and set it to a variable
2. for every row in the table
   1. profit is row[2]- row[4]
   2. append the row for profits
   3. line is an empty string
   4. for every item in the row
      1. the line is the string of the item + and empty space ' '
   5. write the line to the output file and move to a new line
3. close the file

### Purpose: call functions
    ### Name: main
    ### Parameters: 
    ### Return: new file
    ### Algorithm: 
1. table is set to read files to table with the file movies.csv
2. call write from table using table and update movies.csv
3. ask for if the user wants the highest or lowest row
4. error check 
5. print the users decision
6. print thank you message