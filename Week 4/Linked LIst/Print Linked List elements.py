Print Linked List elements 

You are given the pointer to the head node of a linked list. You have to print all of its elements in order in a single line.

Input:
You have to complete a method which takes one argument: the head of the linked list. You should not read any input from stdin/console. The struct Node has a data part which stores the data and a next pointer which points to the next element of the linked list. There are multiple test cases. For each test case, this method will be called individually.

Output:
Print the elements of the linked list in a single line separated by a single space.

Your Task:

You don't need to read input or print anything. Your task is to complete the function display() which takes the head (the head node of the linked list) and You have to print the elements of the linked list.
 

Example:

Input:
N=2
LinkedList={1 , 2}
Output:
1 2
Explanation:
Here the first line denotes an integer 'N' the no of nodes 
of linked list .Then the line after that contains N space
separated integers denoting the values of the nodes of
the linked list.

Solution

#Your task is to complete this function
#Your function should print the data in one line only
#You need not to print new line

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def printlist(node):
    #code here
    while(node!=None):
        print(node.data,end=" ")
        node = node.next




#{ 
#  Driver Code Starts
class node:
    def __init__(self):
        self.data = None
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        llist = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            llist.insert(i)
        printlist(llist.get_head())
        print('')
 #Contributed by:Harshit Sidhwa
# } Driver Code Ends