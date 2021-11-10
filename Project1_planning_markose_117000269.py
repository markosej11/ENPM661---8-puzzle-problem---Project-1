import numpy as np

#CREATING A 3X3 MATRIX TO STORE THE INITIAL STATE FROM THE USER
R = 3 
C = 3
first_node = [] 
initial_node = []
for i in range(R):        
	a =[] 
	for j in range(C): 
		 print("Enter the entrie in position (", i ,j,")")  #Accepting input from user row wise   
		 a.append(int(input()))
	initial_node.append(a)

print()
node_goal = np.matrix('1,2,3;4,5,6;7,8,0')
node_goal = np.array(node_goal)					#Creating goal node
first_node = np.array(initial_node)

Q = []  #Used to store the nodes which are to be explored
Vn = []	#Used to store the nodes that have been visited
X = []	#Used to store the first node in Q and then to find the all the posible new nodes
X_prime = [] #Used to store all the new nodes after moving the blank tile 
node_store = []

#FUNCTION USED TO COMPARE THE NODE IN X WITH THE GOAL NODE
def compare(Z,node_comp):
	A1 = np.copy(Z)
	A2 = np.copy(node_comp)
	result = (A1==A2).all()
	return result

#FUNCTION USED TO CHECK IF X_PRIME HAS ALREADY BEEN EXPLORED OR NOT
def compare1(B1,B2):
	flag = 0
	for i in range(len(B1)):
		for j in range(len(B2)):
			if(B1[i][j]==B2[i][j]):
				flag = 0
			else:
				flag = 1
				break
		if(flag==1):
			break
	return flag

#FUNCTION USED TO BACKTRACK BY COMPARING THE NODES IN BT 
def compare2(c1,c2):
	flag = 0
	for i in range(len(c1)):
		for j in range(len(c2)):
			if(c1[i][j]==c2[i][j]):
				flag = 0
			else:
				flag = 1
				break
		if(flag==1):
			break
	return flag

#FUNCTION USED TO FIND THE LOCATION OF BLANK TILE
def blank_tile_location(node):
	for i in range(len(node)):
		for j in range(len(node)):
			if node[i][j] == 0:
				print('The position of 0 is ',i,j)
				return i,j

#FUNCTION USED TO FIND OUT IN HOW MANY DIRECTIONS THE BLANK TILE CAN MOVE
def options(i,j):
	if(i == 0 and j == 0):
		return 1
	elif(i == 0 and j == 1):
		return 2
	elif(i == 0 and j == 2):
		return 3
	elif(i == 1 and j == 0):
		return 4
	elif(i == 1 and j == 1):
		return 5
	elif(i == 1 and j == 2):
		return 6
	elif(i == 2 and j == 0):
		return 7
	elif(i == 2 and j == 1):
		return 8
	elif(i == 2 and j == 2):
		return 9
	else:
		print("Invalid entry")

#FUNCTION TO MOVE THE BLANK TILE BASED ON ITS LOCATION
def movements(node,num,i,j):
	if(num == 1):
		new_node = action_move_down(node,i,j)
		new_node2 = action_move_right(node,i,j)
		node_store.append(new_node)
		node_store.append(new_node2)
		return node_store
	elif(num == 2):
		new_node = action_move_right(node,i,j)
		new_node2 = action_move_left(node,i,j)
		new_node3 = action_move_down(node,i,j)
		node_store.append(new_node)
		node_store.append(new_node2)
		node_store.append(new_node3)
		return node_store
	elif(num == 3):
		new_node = action_move_down(node,i,j)
		new_node2 = action_move_left(node,i,j)
		node_store.append(new_node)
		node_store.append(new_node2)
		return node_store
	elif(num == 4):
		new_node = action_move_right(node,i,j)
		new_node2 = action_move_up(node,i,j)
		new_node3 = action_move_down(node,i,j)
		node_store.append(new_node)
		node_store.append(new_node2)
		node_store.append(new_node3)
		return node_store
	elif(num == 5):
		new_node = action_move_right(node,i,j)
		new_node2 = action_move_up(node,i,j)
		new_node3 = action_move_down(node,i,j)
		new_node4 = action_move_left(node,i,j)
		node_store.append(new_node)
		node_store.append(new_node2)
		node_store.append(new_node3)
		node_store.append(new_node4)
		return node_store
	elif(num == 6):
		new_node = action_move_left(node,i,j)
		new_node2 = action_move_up(node,i,j)
		new_node3 = action_move_down(node,i,j)
		node_store.append(new_node)
		node_store.append(new_node2)
		node_store.append(new_node3)
		return node_store
	elif(num == 7):
		new_node = action_move_right(node,i,j)
		new_node2 = action_move_up(node,i,j)
		node_store.append(new_node)
		node_store.append(new_node2)
		return node_store
	elif(num == 8):
		new_node = action_move_right(node,i,j)
		new_node2 = action_move_up(node,i,j)
		new_node3 = action_move_left(node,i,j)
		node_store.append(new_node)
		node_store.append(new_node2)
		node_store.append(new_node3)
		return node_store
	elif(num == 9):
		new_node = action_move_left(node,i,j)
		new_node2 = action_move_up(node,i,j)
		node_store.append(new_node)
		node_store.append(new_node2)
		return node_store
	else:
		print("Something wrong!!")

#FUNCTION TO MOVE THE BLANK TILE LEFT
def action_move_left(node,i,j):
	copy_node = np.copy(node)
	temp = copy_node[i,j]
	temp2 = copy_node[i,j-1]
	copy_node[i,j-1] = temp
	copy_node[i,j] = temp2
	return copy_node

#FUNCTION TO MOVE THE BLANK TILE RIGHT
def action_move_right(node,i,j):
	copy_node = np.copy(node)
	temp = copy_node[i,j]
	temp2 = copy_node[i,j+1]
	copy_node[i,j+1] = temp
	copy_node[i,j] = temp2
	return copy_node

#FUNCTION TO MOVE THE BLANK TILE UP
def action_move_up(node,i,j):
	copy_node = np.copy(node)
	temp = copy_node[i,j]
	temp2 = copy_node[i-1,j]
	copy_node[i-1,j] = temp
	copy_node[i,j] = temp2
	return copy_node

#FUNCTION TO MOVE THE BLANK TILE DOWN
def action_move_down(node,i,j):
	copy_node = np.copy(node)
	temp = copy_node[i,j]
	temp2 = copy_node[i+1,j]
	copy_node[i+1,j] = temp
	copy_node[i,j] = temp2
	return copy_node

#FUNCTION TO PRINT THE NODE PATH
def print_matrix(state):
	print("-------------")
	print("|", end=" ")
	print(int(state[0]), "|", int(state[1]), "|", int(state[2]), "|")
	print("-------------")
	print("|", end=" ")
	print(int(state[3]), "|", int(state[4]), "|", int(state[5]), "|")
	print("-------------")
	print("|", end=" ")
	print(int(state[6]), "|", int(state[7]), "|", int(state[8]), "|")
	print("-------------")
				
#---------------------MAIN FUNCTION--------------------------------------
BT = []
Q.append(first_node)
while(Q!=[]):								#while Q is not empty
	X = np.copy(Q.pop(0))					#Poping the initial node in Q and storing it in node X
	check = False
	check = compare(X,node_goal)			#Checking if X is the goal state
	if check == True :
		print("SUCCESS!!!")
		ans = X
		break
	a,b = blank_tile_location(X)			#finding the blank tile location
	opt = options(a,b)						#finding how many movemnts is possible
	print(opt)
	X_prime = movements(X,opt,a,b)			#finding the new nodes after moving the blank tile
	for k in range(len(X_prime)):
		A = []
		A.append(X_prime[k])
		A.append(X)
		BT.append(A)						#storing the parent and child node in BT
	for i in range(len(X_prime)):
		y = 1
		for j in range(len(Vn)):
			y = compare1(X_prime[i],Vn[j])	#checking if the new node has been explored or not
			if(y == 0):
				break
		if(y == 1):
			Vn.append(X_prime[i])			#if new node hasn't been explored then storing it in Vn
			Q.append(X_prime[i])			#Storing the new node in Q as it hasn't been explored
	del X_prime[:]							#emptying X_prime

#BACK TRACKING
path = []
path.append(ans)							#initialising the list with the goal node
for i in range(len(BT)):
	r=0
	for j in range(len(BT)):
		r = compare2(path[i],BT[j][0])		#checking to find previous node
		if(r==0):
			path.append(BT[j][1])
			break
	s=compare(first_node,BT[j][1])			#checking if initial node has been reached or not
	if(s==True):
		break
		
node_path = []								#chreating a list to store the path
for i in reversed(path):
	node_path.append(i)						#saving the path into the list

#Writing the node path into a text file
f = open("Nodepath.txt",'w')
for i in range(len(node_path)):
	temp1 = node_path[i][0][0]
	temp2 = node_path[i][0][1]
	temp3 = node_path[i][0][2]
	temp4 = node_path[i][1][0]
	temp5 = node_path[i][1][1]
	temp6 = node_path[i][1][2]
	temp7 = node_path[i][2][0]
	temp8 = node_path[i][2][1]
	temp9 = node_path[i][2][2]
	f.write("\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n "  %(temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9))
f.close()

#Writing the explored nodes into a text file
f = open("Nodes.txt",'w')
for i in range(len(Vn)):
	temp1 = Vn[i][0][0]
	temp2 = Vn[i][0][1]
	temp3 = Vn[i][0][2]
	temp4 = Vn[i][1][0]
	temp5 = Vn[i][1][1]
	temp6 = Vn[i][1][2]
	temp7 = Vn[i][2][0]
	temp8 = Vn[i][2][1]
	temp9 = Vn[i][2][2]
	f.write("\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n "  %(temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9))
f.close()     


#Displaying the node path to the used
fname = 'Nodepath.txt'
data1 = np.loadtxt(fname)
if len(data1[1]) is not 9:
	print("Format of the text file is incorrect, retry ")
else:
	for i in range(0, len(data1)):
		if i == 0:
			print("Start Node")
		elif i == len(data1)-1:
			print("Achieved Goal Node")
		else:
			print("Step ",i)
		print_matrix(data1[i])
		print()
		print()