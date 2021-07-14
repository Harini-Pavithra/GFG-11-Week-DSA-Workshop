Huffman Decoding 

Given a encoded binary string and a Huffman MinHeap tree, your task is to complete the function decodeHuffmanData(), which decodes the binary encoded string and return the original string. 

Note: Each node of the min heap contains 2 data members, a character and an integer to denote its frequency. The character '$' is the special character used for internal nodes whose min heap node only need a integer field.


Example 1:

Input :
binaryString = 
0000000000001100101010101011111111010101010
Min Heap Tree =  
                $(20)
              /      \
            /          \
         $(8)            \
       /     \             \
    $(3)      \            $(12)
    /  \       \           /    \
B(1)    D(2)    E(5)    C(6)    A(6)

Output: AAAAAABCCCCCCDDEEEEE

Explanation:
The following chart can be made from the 
given min heap tree.
character    frequency    code
    A             6        00                 
    B             1        110
    C             6        01
    D             2        111    
    E             5        10

Example 2:

Input :
binaryString =
01110100011111000101101011101000111
Min Heap Tree =  
                         $(13)
                      /        \
                    /            \
                  /                \
               $(5)                  \
             /      \                  \
            /        \                   \
         $(3)         \                  $(8)
        /    \         \                /    \
     $(2)     \         \            $(4)     \
    /   \      \         \          /   \      \
f(1)    o(1)    r(1)    g(2)    k(2)    s(2)    e(4)

Output: geeksforgeeks

Explanation:
The following chart can be made from the 
given min heap tree.
character    frequency    code
    f             1        0000                 
    o             1        0001
    r             1        001
    g             2        01    
    k             2        100
    s             2        101
    e             4        11

Your Task:  
You dont need to read input or print anything. Complete the function decodeHuffmanData() which takes the root of the Huffman min heap tree and the encoded Binary String as input parameters and returns the decoded string.


Expected Time Complexity: O(N log N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 10^3

Solution

#User function Template for python3

'''
class MinHeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None
'''



#Function to return the decoded string.
def decodeHuffmanData(root, binaryString):
    ans = ""
    curr = root
    
    #iterating over the string.
    for i in range(len(binaryString)):
        
        #if character is "0" then moving to left child of parent node
	    #else to the right child.
        if binaryString[i]=='0':
            curr = curr.left
        else:
            curr = curr.right
            
            
        #if both the child of current node are null, we add the data 
		#at current node in our result and update current node.
        if(curr.left==None and curr.right==None):
            ans+=curr.data
            curr=root
            
    #returning the resultant string.
    return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import heapq
minheap = []
heapq.heapify(minheap)
cnt=0
codes = {}
freq = {}

class MinHeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

def printCodes(root, strr):
    if root==None:
        return
    if root.data is not '$':
        print(str(root.data)+": "+strr)
    printCodes(root.left, strr+"0")
    printCodes(root.right, strr+"1")

def storeCodes(root, strr):
    if root==None:
        return
    if root.data is not '$':
        codes[root.data]=strr
    storeCodes(root.left, strr+"0")
    storeCodes(root.right, strr+"1")

def huffmanCodes(s):
    global cnt
    for v in freq:
        heapq.heappush(minheap, (freq[v], freq[v]+cnt, MinHeapNode(v, freq[v])))
        cnt+=1
    while(len(minheap) is not 1):
        left = minheap[0][2]
        heapq.heappop(minheap)
        right = minheap[0][2]
        heapq.heappop(minheap)
        top = MinHeapNode('$', left.freq+right.freq)
        top.left = left
        top.right = right
        heapq.heappush(minheap, (top.freq, top.freq+cnt, top))
        cnt+=1
    storeCodes(minheap[0][2], "")


def calcFreq(strr, n):
    for i in range(n):
        if strr[i] not in freq:
            freq[strr[i]]=1
        else:
            freq[strr[i]]+=1


if __name__ == "__main__":
    t = int(input())
    while(t>0):
        strr = input()
        encodedString = ""
        decodedString = ""
        calcFreq(strr, len(strr))
        #print(freq)
        huffmanCodes(len(strr))
        #print(codes)
        for i in strr:
            encodedString += codes[i]

        decodedString = decodeHuffmanData(minheap[0][2], encodedString)
        print(decodedString)
        t=t-1


# } Driver Code Ends