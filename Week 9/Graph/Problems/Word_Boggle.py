Word Boggle 

Given a dictionary of distinct words and an M x N board where every cell has one character. Find all possible words from the dictionary that can be formed by a sequence of adjacent characters on the board. We can move to any of 8 adjacent characters, but a word should not have multiple instances of the same cell.


Example 1:

Input: 
N = 1
dictionary = {"CAT"}
R = 3, C = 3
board = {{C,A,P},{A,N,D},{T,I,E}}
Output:
CAT
Explanation: 
C A P
A N D
T I E
Words we got is denoted using same color.
Example 2:

Input:
N = 4
dictionary = {"GEEKS","FOR","QUIZ","GO"}
R = 3, C = 3 
board = {{G,I,Z},{U,E,K},{Q,S,E}}
Output:
GEEKS QUIZ
Explanation: 
G I Z
U E K
Q S E 
Words we got is denoted using same color.

Your task:
You don’t need to read input or print anything. Your task is to complete the function wordBoggle() which takes the dictionary contaning N space-separated strings and R*C board as input parameters and returns a list of words that exist on the board.


Expected Time Complexity: O(N*W + R*C^2)
Expected Auxiliary Space: O(N*W + R*C)


Constraints:
1 ≤ N ≤ 15
1 ≤ R, C ≤ 50
1 ≤ length of Word ≤ 60

Solution

#User function Template for python3

class Solution:
    def search( self ,board,  word,  index,  i,  j):
        n = len(board)
        m = len(board[0])
        
        # If position of the cell is inside the board or not
        if i < 0 or i > n - 1 or j < 0 or j > m - 1 : 
            return False
        
        # If the current cell does not match the letter at index  
        if  word[index] != board[i][j] :
            return False
    
        # If each character is matched
        if index == len(word) - 1 :
            return True
        
        ch = board[i][j]
        board[i][j] = '#'
        
        # Search for adjacent indices
        dx = [-1,0,+1,-1,+1,-1,0,+1]
        dy = [+1,+1,+1,0,0,-1,-1,-1]
        
        for x in range(len(dx)) :
            if self.search(board,word,index + 1,i+dx[x],j+dy[x]) :
                board[i][j] = ch
                return True

        board[i][j] = ch        
        return False
    
    def exist(self, board, word):
        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if self.search(board,word,0,i,j) : 
                    return True
        
        return False
    
    
    def wordBoggle(self, board,  dictionary):
        wordslist = [] 
        for i in range(len(dictionary)):
            if self.exist(board,dictionary[i]) :
                wordslist.append(dictionary[i])
            
        return wordslist
#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        N=int(input())
        dictionary=[x for x in input().strip().split()]
        line=input().strip().split()
        R=int(line[0])
        C=int(line[1])
        board=[]
        for _ in range(R):
            board.append( [x for x in input().strip().split()] )
        obj = Solution()
        found = obj.wordBoggle(board,dictionary)
        if len(found) is 0:
            print(-1)
            continue
        found.sort()                               # sorting output
        for i in found:
            print(i,end=' ')
        print()
# } Driver Code Ends