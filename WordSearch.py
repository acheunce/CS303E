#  File: WordSearch.py

#  Description:

#  Student Name: Aaron Cheung

#  Student UT EID: ac77373

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E 

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input():
  line = sys.stdin.readline()
  line = line.strip()
  grid_length = int(line)

  line = sys.stdin.readline()

  for i in range(grid_length):
    grid = []
    grid.append([])
    line = sys.stdin.readline()
    row = line.strip()
    grid[0].append(row)


  line = sys.stdin.readline()
  line = line.strip()
  word_length = int(line)

  line = sys.stdin.readline()

  for i in range(word_length):
    line = sys.stdin.readline()
    word = line.strip()
    words += [word]
  

def check_around(grid, row, column, letter):
  if grid[row+1][column] == letter:
    return row+1, column
  elif grid[row+1][column+1] == letter:
    return row+1, column+1
  elif grid[row][column+1] == letter:
    return row, column+1
  elif grid[row-1][column+1] == letter:
    return row-1, column+1
  elif grid[row-1][column] == letter:
    return row-1, column
  elif grid[row-1][column-1] == letter:
    return row-1, column-1
  elif grid[row][column-1] == letter:
    return row, column-1
  elif grid[row+1][column-1] == letter:
    return row+1, column-1
  return -1, -1

def search(grid, row, col, word):
  if grid[row][col] != word[0]:
    return False
  else:

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid

def find_word (grid, word):
  # parse (loop through for len(word)) through nxn grid for the first letter of the given word
  # If letter == word[0]
  #   Check up, diag up-right, right, diag down-right, down, diag down-left, left, diag up-left
  #   If letter == word[1]
  #      Check again-continue until 
  # length = len(word)
  # indicies = find_letter(grid, word[0])
  

  
  # for x, y in indicies:
  #   idx = check_around(grid, indicies, word[1])
  #   for j in range(len(word)):
  #     idx = check_around(grid, check_around(grid, indicies[i], word[j+2]), word[j+2])
        
  for row in range(len(grid)):
    for col in range(len(grid)):
      if search(grid, row, col, word):
        return (row, col)
  return ()

  # Recursive
  # base case
  # if len(word) == 0:
  #  return word
  #else:
  #  return find_word[grid, word]


def main():
  # read the input file from stdin
  word_grid, word_list = read_input()

  # find each word and print its location
  for word in word_list:
    location = find_word (word_grid, word)
  print (word + ": " + str(location))

if __name__ == "__main__":
  main()
