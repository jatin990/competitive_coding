
# Illuminating Lights

# Geek wants to decorate his house, with a bunch of 'n' led lights. Each light has its own illuminating value. Geek wants to arrange these led's in the increasing order of their illuminating value. To do this, he is allowed to shuffle(interchange) a pair of any two led's. He can perform this operating any number of times. Find the number of operations needed to obtain the required pattern.

# Note : Illuminating values are consecutive integers.

# Input n, integer denoting number of led's in a bunch. led[], array of integers denoting illuminating value of 'n' led's. Output Find the number of operations needed to obtain the required pattern.

# Example

# Input:

# 3 2 3 1

# Output:

# 2

# Explanation :

# Our required pattern is 1 2 3, we can do this with two operations. First Operation : Shuffle 2 & 1, array becomes 1 3 2. Second Operation : Shuffle 3 & 2, array becomes 1 2 3.



# your code goes here
lights=[x for x in map(int,input().split())]
n=lights[0]
lights=lights[1:]
count=0
i=0
while i<n-1:
    min_index=i
    for j in range(i+1,n):
        if lights[min_index]>lights[j]:
            min_index=j
    if not min_index==i:
        lights[i],lights[min_index]=lights[min_index],lights[i]
        count+=1
    while i<n-1:
        if lights[i]+1==lights[i+1]:
            i+=1
        else:
            i+=1
            break
print(count)
        
