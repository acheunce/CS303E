# File: ControlGame.py
# Student: Aaron Cheung
# UT EID: ac77373
# Course Name: CS303E
# 
# Date: 04/01/2022
# Description of Program: 

class ControlGame:

    def __init__(self, turnsToPlay = 64):
        # This initializes the game with an empty board, the current
        # player set to 'Red' and the number of turns
        # specified by the user (defaults to 64).  turnsToPlay must
        # be an even number in the range [2..64].
        self.board = []
        for i in range(8):
            cells = [ "." for cell in range(8)]
            self.board.append(cells)
        self.currentPlayer = "Red"

    def __str__(self):
        # Permit displaying the header "Current board is:" following by the 
        # board.
        string = ("\nCurrent board is: \n  0 1 2 3 4 5 6 7")
        for row in range(len(self.board)):
            string += "\n" + str(row) + " "
            for cell in range(len(self.board)):
                string += self.board[row][cell] + " "
        return string 


    def getCurrentPlayer(self):
        # Return the current player, 'Red' or 'Blue'
        return self.currentPlayer
        pass

    def swapCurrentPlayer(self):
        # If the current player is 'Red', set it to 'Blue', and 
        # vice versa.
        if self.currentPlayer == "Red":
            self.currentPlayer == "Blue"
        else:
            self.currentPlayer == "Red"
    
    def getBoardState(self):
        # Return the current board.
        return self.board
        pass
    
    def takeTurn(self, row, col):
        # This attempts to add the current player's token to cell
        # (row, col).  Check whether the cell is legal and is not
        # occupied.  If the checks pass add the current player's
        # token to that cell.  Finally, return a Boolean value 
        # indicating whether or not the turn occurred.
        if row > 7 or row < 0 or col > 7 or col < 0:
            print("Invalid turn, Cannot place piece on occupied cell")
            return False
        else:
            if self.board[row][col] != "." or row > 7 or col > 7:
                print("Invalid turn. location is out of bounds.")
                return False
            else:
                if self.currentPlayer == "Blue":
                    self.board[row][col] = "B"
                elif self.currentPlayer == "Red":
                    self.board[row][col] = "R"
                return True
    
    def getScore(self):
        # Calculate the sum of rows, columns, and cells controlled by
        # Red and Blue.  Return this as a pair (red, blue).  This is
        # the most complicated method, so it's probably a good idea 
        # to write subsidiary functions for this.
        redRow = []
        blueRow = []
        redCol = []
        blueCol = []
        red = 0
        blue = 0
        index = 0

        for col in range(len(self.board)):

            if len(redCol) > len(blueCol):
                red += 1
            elif len(redCol) < len(blueCol):
                blue += 1

            if self.board[index][col] == "R":
                redCol.append("1")
            elif self.board[index][col] == "B":
                blueCol.append("1")

            for row in range(len(self.board)):
    
                if len(redRow) > len(blueRow):
                    red += 1
                elif len(redRow) < len(blueRow):
                    blue += 1

                if self.board[row][col] == "R":
                    redRow.append("1")
                elif self.board[row][col] == "B":
                    blueRow.append("1")
            index += 1
        
        return red, blue

        pass
