 Job Sequencing Problem

Given a set of N jobs where each jobi has a deadline and profit associated with it. Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit if and only if the job is completed by its deadline. The task is to find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.

Example 1:

Input:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60
Explanation:
Job1 and Job3 can be done with
maximum profit of 60 (20+40).
Example 2:

Input:
N = 5
Jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
Output:
2 127
Explanation:
2 jobs can be done with
maximum profit of 127 (100+27).

Your Task :
You don't need to read input or print anything. Your task is to complete the function JobScheduling() which takes an integer N and an array of Jobs(Job id, Deadline, Profit) as input and returns the count of jobs and maximum profit.


Expected Time Complexity: O(NlogN)
Expected Auxilliary Space: O(N)


Constraints:
1 <= N <= 105
1 <= Deadline <= 100
1 <= Profit <= 500

Solution

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        res,count = 0,0
        
        #sorting all jobs according to decreasing order of profit.
        Jobs = sorted(Jobs , key = lambda x: x.profit, reverse=True)
        
        #array to store result (Sequence of jobs).
        result = [0 for i in range(n)]
        #boolean array to keep track of free time slots 
        #and initializing all slots to free.
        slot = [False for i in range(n)]
    
        
        #iterating through all given jobs.
        for i in range(n):
            
            #finding a free slot for current job (Note that we start 
        	#from the last possible slot).
            for j in range(min(n,Jobs[i].deadline)-1,-1,-1):
                
                #if free slot is found, we add current job to result array
        		#and make the current slot occupied.
                if not slot[j]:
                    result[j] = i
                    slot[j] = True 
                    break
                
        #if slot is occupied, we update the counter and 
	    #add its profit in final result.
        for i in range(n):
            if slot[i]:
                res+=Jobs[result[i]].profit
                count+=1
    
        #storing the count of jobs and max profit in a list and returning it.
        ans = []
        ans.append (count)
        ans.append (res)
        return ans
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends