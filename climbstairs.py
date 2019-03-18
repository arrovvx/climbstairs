

N = 4
X = {1,3,5}
X = {1,2}

def climb(steps, stairsNum):
	sum = 0
	
	for step in steps:
		stairsLeft = stairsNum - step
		
		if stairsLeft > 0:
			sum += climb(steps, stairsNum - step)
			
		if stairsLeft == 0:
			sum += 1
			
	return sum
	
print(climb(X,N))