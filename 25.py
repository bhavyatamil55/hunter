class Node1:
  def __init__(self,AB):
    self.value=AB
    self.right=None
    self.left=None

def insert(root,AB):
  if root is None:
    root=Node1(data)
  elif root.value > AB:
    if root.left is None:
      root.left=Node1(AB)
    else:
      insert(root.left,AB)
  elif root.value < AB:
    if root.right is None:
      root.right=Node1(AB)
    else:
      insert(root.right,AB)

def LCA(root,L_val,R_val):
  if root is None:
    return None
  elif L_val > root.value and R_val > root.value:
    return(LCA(root.right,L_val,R_val))
  elif L_val < root.value and R_val < root.value:
    return (LCA(root.left,L_val,R_val))
  else:
    return root.value

bhav=int(input())
val=list(map(eval,input().split()))
urn,van=map(eval,input().split())
RS=Node1(val[0])
for i in range(1,bhav):
  insert(RS,val[i])
print(LCA(R,urn,van))
