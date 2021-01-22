Occurence of an integer in a Linked List 

Given a singly linked list and a key, count the number of occurrences of given key in the linked list.

Example 1:

Input:
N = 7
Link List = 1->2->1->2->1->3->1
search_for = 1
Output: 4
Explanation:1 appears 4 times.
 

Your Task:

You dont need to read input or print anything. Complete the function count() which takes the head of the link list and search_for i.e- the key as input parameters and returns the count of occurrences of the given key.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
0 ≤ N ≤ 10^4

Solution

"""  Return the no. of times search_for value is there in a linked list.
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
def count(head, search_for):
    # Code here
    c=0
    while(head!=None):
        if head.data == search_for:
            c=c+1
        head = head.next
    return c



#{ 
#  Driver Code Starts
# Do not delete this comment
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        m = int(input())
        k = count(llist.head, m)
        print(k)
        t -= 1
# Contributed by:Harshit Sidhwa
# } Driver Code Ends