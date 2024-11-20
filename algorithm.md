# Algorithm Document

#### THINK before you code...
#### Write down the list of tasks to help you think

### Purpose: reading file 
    ### Name: read_file_to_table
    ### Parameters: file
    ### Return: table name
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
