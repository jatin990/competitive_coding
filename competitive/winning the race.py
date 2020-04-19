# your code goes here
# Winning The Race
# Geek is organizing a race of N contestants.This is an interesting race in which a winner is predicted after checking at every odd seconds. If race time is 6 seconds, then we will look up who is leading at particular checktime, ie at 1st second, 3 second, and 5th second. Participant who is leading more number of times is considered to be the winner of a race. Note :

# At a particular timepoint, if two or more participants are at same distance, then both are considered to be leading the race. At the end of timepoints, if two or more participants have equal lead point, the one who comes first in input sequence is considered to be a winner.
# Input

# N, integer denoting number of participants. T, integer denoting total time in seconds of this marathon. Next N line follows : We have T+1 integers seperated by space. First T lines are as follows : i th integer denotes the number of steps taken by participant at i th second. (T+1)th integer denotes distance of each step.
# Output
# Index of Marathon winner, index starts from 1.

# Example
# Input:
# 2
# 3
# 2 3 1 3
# 1 1 1 4

# Output: 1

# Explanation:

# 2( No. of participants )
# 3( Total time of race )
# 2 3 1 3 ( data for first participant, First 3 integers denotes number of steps per second and last integer is distance covered in each step.) 1 1 1 4 ( similarly, data for second participant.)

# At time 1 : Participant 1 is leading. as (6)>(4)
# At time 3 : Participant 1 is leading. as 18 > 12
import sys
part=int(input())
winner=0
count=dict()
martime=int(input())
participants=[]
winners=dict()
for e in range(part):
	distance=0
	current_cal=[x for x in map(int,input().split())]
	participants.append([])
	for i in range(martime):
		x=current_cal[-1]
		distance+=current_cal[i]*x
		participants[e].append(distance)
if martime%2==0:
	n=martime
else:
	n=martime+1
for j in range(0,n,2):
	current_winner=-sys.maxsize-1
	for k in range(part):
		current_part=participants[k][j]
		if current_winner<current_part:
			dic=k
	winners[j+1]=dic
for u in winners.keys():
	if count.get(winners[u]):
		count[winners[u]]+=1
	else:
		count[winners[u]]=1
itemMaxValue = max(count.items(), key=lambda x : x[1])
print(itemMaxValue[0])