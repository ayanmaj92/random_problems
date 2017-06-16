'''
Function: is_possible()

Parameters: time, k (no. of agents), job (job array), n (number of jobs)
Returns: Returns TRUE or FALSE depending on if the jobs can be done by the specified 'k' number of agents
in the constrained time 'time'.

Description: This function checks if the 'k' number of agents can accomplish the jobs given in the job array,
provided the time 'time'. We have two local variables curr_time and cnt_agents that is set to 1. Now, we loop 
through the job array. As long as the curr_time added with the job[i] is less than or equal to the time limit 'time',
that single agent can take and do the job, so we add that to the curr_time.

If the curr_time + job[i] exceeds the time limit, then this agent can no longer take that job. So we go to the else, and
we reset the curr_time to this particular job time job[i], and go over to the next agent, so we increment the cnt_agents.

After looping, we get the total number of agents that would be required to finish the jobs in the array within the time limit
'time'. If this cnt_agents <= k (no. of agents given), then we return TRUE.
'''

def is_possible(time, k, job, n):
	curr_time = 0
	cnt_agents = 1
	for i in range(n): 
		if (curr_time + job[i]) <= time:
			curr_time += job[i]
		else:
			curr_time = job[i] 
			cnt_agents += 1
	return cnt_agents <= k
	
'''
Function: find_minimum()

Parameters: k (no. of agents), t (time required for one unit of job), job (job array), n (length of job array)

Returns: The minimum time that would be required with proper scheduling

Description: This function returns the actual minimum time that would be required after proper scheduling. Set start_time
as 0, end_time as the total cumulative time for all the jobs, and also find and keep the max_job that is the job that takes 
the max time. Now let us initialize the ans as the end_time or the cumulative sum of all job times, as this is max possible.

Now, we do a sort of binary search, and mid is the mid-point of start_time and end_time. If this mid-time is greater or equal 
to the max_job time, AND the jobs are possible to be completed by the k agents in that mid-time, then we update the ans to be 
the minimum of the current ans and the mid-time. Then according to BS, we set end_time as (mid-time - 1), as our target is to 
find minimum time.

However, if the mid-time is less than the max_job, then we simply update the start_time as (mid-time + 1), as we are doing BS.
The reason we do this is that if the mid-time is less than max_job time, then there is NO FREAKING WAY that we can accomplish
all the jobs in that mid-time. So, we should search for the tim in the period start_time + 1 to end_time.
'''

def find_minimum(k, t, job, n):
	start_time = 0
	end_time = sum(job)
	max_job = max(job)
	
	ans = end_time
	
	while (start_time <= end_time):
		mid = start_time + (end_time - start_time) // 2
		
		if mid >= max_job and is_possible(mid, k, job, n):
			ans = min(ans, mid)
			end_time = mid - 1
		else:
			start_time = mid + 1
			
	return ans * t
	
if __name__ == "__main__":
	# job = [10,7,8,12,6,8]
	job = [4, 5, 10]
	n = len(job)
	k, t = 2, 5
	res = find_minimum(k, t, job, n)
	print ("Answer: ",res)