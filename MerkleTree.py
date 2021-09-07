from hashlib import sha256
from random import randint

# In bitcoin, block information is stored as a hash. To achieve this, the transactions of the block
# are run through an algorithm to get a merkle root. In this process, each transactions is hashed 
# and the hashed transactions make up the leaves of the merkle tree.
# The leaves are then paired up and hashed to form the next nodes. This happens recursively.
# In the end we will end up with one node (the parent of the binary merkle tree) which is known as the merkle root.
# The merkle root represents the hashed block.


#Nodes in the blockchain
nodes=['N1','N2','N3','N4','N5','N6','N7','N8','N9','N10','N11','N12']

#Transaction state
transactions=[]

#Number of nodes
n = len(nodes)

number_of_transactions = 100000

for _ in range(number_of_transactions):
    transactions.append((nodes[randint(0,n-1)]+" paid "+str(randint(100,900))+" rupees to "+nodes[randint(0,n-1)]).encode())

#SHA256 hash function. Output is a bytes object.
def nodeHash(node):
    return sha256(node).digest()

#Hashing the transactions  to form the leaves.
leaves = []
for t in transactions:
    leaves.append(nodeHash(t)) 

#If number of leaves is odd, the last leaf is duplicated.
if len(leaves)%2==1:
    leaves.append(leaves[-1])

#Recursive hashing to get merkle root.
def MerkleRoot(state):
    state_size=len(state)
    
    #Reject empty states.
    if state_size==0:
        return "stateError: Empty leaf state."
    
    # All leaves converged to one parent which is the merkle root.
    if state_size==1:
        print("Merkle root computed: ")
        return state[0]
        
    node_state=[]

    for i in range(0,state_size-1,2):
        node_state.append(nodeHash(state[i]+state[i+1]))
    
    return MerkleRoot(node_state)

#Output in few seconds for 100,000 transactions
print(MerkleRoot(leaves))
        









