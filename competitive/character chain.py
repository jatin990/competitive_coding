# Characters Chain

# A bracket may be any character between [a-z] or [A-Z]. Generally, we consider lowercase characters as opening brackets and uppercase characters as closing brackets. Two brackets are considered to be a stable pair if the an opening bracket of the exact same type. For instance, stable pairs of brackets: a,A | b,B | t.T . A pair of brackets is not stable if the set of brackets it encloses are not matched. For example, abcCBA is stable whereas BcCb is not. A sequence of brackets is stable if the following conditions are met:

# It contains no unmatched brackets. The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets. You are provided with N strings, your job is to find whether it is stable or not. Print Y for yes or N for No.

# Constraint : 1 <= N <= 10^4

# Input

# Integer N, denoting number of strings. Each N lines, includes a string of character.

# Output Print Y for yes or N for No for each string in new line.

# Example

# Input: 2
# ababBABA
# aaacccCCCAA

# Output: Y
# N



# your code goes here
for _ in range(int(input())):
	count=0
	count1=0
	string=input()
	lowe=[]
	flag=False
	if string[0].isupper():
		print('N')
	else:
		for i in string:
			if i.islower():
				lowe.append(i)
				count1+=1
			else:
				count+=1
				if not i.lower()==lowe.pop(-1):
					flag=True
		if flag or count!=count1:
			print('N')
		else:
			print('Y')
				
		
