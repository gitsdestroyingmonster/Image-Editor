class MagicList :
	def __init__(self):
		self.data = [0]
	
	def findMin(self):
		M = self.data
		''' you need to find and return the smallest
			element in MagicList M.
			Write your code after this comment.
		'''
		if len(self.data) == 1:
			return None
		else:
			return M[1]

	
	def insert(self, E):
		M = self.data
		''' you need to insert E in MagicList M, so that
			properties of the MagicList are satisfied. 
			Return M after inserting E into M.
			Write your code after this comment.
		'''
		M.append(E)
		i = len(M)-1

		while (M[i // 2] > M[i]) and i>1:
			(M[i],M[i//2])=(M[i//2],M[i])
			i = i // 2
		return M
	
	def deleteMin(self):
		M = self.data
		''' you need to delete the minimum element in
			MagicList M, so that properties of the MagicList
			are satisfied. Return M after deleting the 
			minimum element.
			Write your code after this comment.
		'''
		(M[1],M[len(M)-1])=(M[len(M)-1],M[1])
		M.pop()
		i=1
		while True:
			if 2*i>len(M)-1:
				break
			elif 2*i<=len(M)-1 and (2*i)+1>len(M)-1:
				(M[i],M[2*i])=(M[2*i],M[i])
				i=2*i
			else:
				if (M[i]<M[2*i]) and (M[i]<M[(2*i)+1]):
					break
				elif (M[i]>min(M[2*i],M[(2*i)+1])):
					if min(M[2*i],M[(2*i)+1])==M[2*i]:
						(M[i],M[2*i])=(M[2*i],M[i])
						i=2*i
					else:
						(M[i],M[(2*i)+1])=(M[(2*i)+1],M[i])
						i=(2*i)+1				
		return M

		
	
def K_sum(L, K):
	''' you need to find the sum of smallest K elements
		of L using a MagicList. Return the sum.
		Write your code after this comment.
	'''    
	M=MagicList()
	for i in L:
		M.insert(i)
	sum1= 0
	for i in range(K):
		sum1+=M.data[1]
		M.deleteMin()
	return sum1
	
if __name__ == "__main__" :
	'''Here are a few test cases'''
	
	'''insert and findMin'''
	M = MagicList()
	M.insert(4)
	M.insert(3)
	M.insert(5)
	x = M.findMin()
	if x == 3 :
		print("testcase 1 : Passed")
	else :
		print("testcase 1 : Failed")
		
	'''deleteMin and findMin'''
	M.deleteMin()
	x = M.findMin()
	if x == 4 :
		print("testcase 2 : Passed")
	else :
		print("testcase 2 : Failed")
		
	'''k-sum'''
	L = [2,5,8,3,6,1,0,9,4]
	K = 4
	x = K_sum(L,K)
	if x == 6 :
		print("testcase 3 : Passed")
	else :
		print("testcase 3 : Failed")