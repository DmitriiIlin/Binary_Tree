"""
Реализация бинарного дерева

"""
class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
    
    def hasLeftChild(self):
        #Возвращает BSTNode левого потомка
        return self.LeftChild

    def hasRightChild(self):
        #Возвращает BSTNode левого потомка
        return self.RightChild

    def isRoot(self):
        #Возвращает True если BSTNode является корнем 
        return not self.Parent

    def isLeaf(self):
        #Возвращает True если элемент не имеет потомков
        return not(self.LeftChild or self.RightChild)

class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если не найден узел
        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо 
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        if self.Root==None:
            return None
        elif self.Root:
            return self._FindNodeByKey(key,self.Root)
        else:
            return None
            
    def _FindNodeByKey(self,key,currentNode):
        # приватный метод поиска
        if not currentNode:
            return None 
        elif currentNode.NodeKey==key:
            nodeRes=BSTFind()
            nodeRes.Node=currentNode
            nodeRes.NodeHasKey=True
            nodeRes.ToLeft=None
            return nodeRes
        elif key<currentNode.NodeKey:
            if currentNode.hasLeftChild():
                return self._FindNodeByKey(key,currentNode.LeftChild)
            else:
                nodeRes=BSTFind()
                nodeRes.Node=currentNode
                nodeRes.NodeHasKey=False
                nodeRes.ToLeft=True
                return nodeRes
        else:
            if currentNode.hasRightChild():
                return self._FindNodeByKey(key,currentNode.RightChild)
            else:
                nodeRes=BSTFind()
                nodeRes.Node=currentNode
                nodeRes.NodeHasKey=False
                nodeRes.ToLeft=False
                return nodeRes


    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        if key==None:
            return None
        allNodes=self.GetAllNodes()
        for node in allNodes:
            if node.NodeKey==key:
                return False 
        if self.Root:
            self._AddKeyValue(key,val,self.Root)
            return True
        else:
            Node=BSTNode(key,val,None)
            self.Root=Node
            return True
        
    def _AddKeyValue(self,key,val,currentNode):
        # приветный метод добавления Node
        if key<currentNode.NodeKey:
            if currentNode.hasLeftChild()!=None:
                self._AddKeyValue(key,val,currentNode.LeftChild)
            else:
                currentNode.LeftChild=BSTNode(key,val,currentNode)
        elif key>currentNode.NodeKey:
            if currentNode.hasRightChild()!=None:
                self._AddKeyValue(key,val,currentNode.RightChild)
            else:
                currentNode.RightChild=BSTNode(key,val,currentNode)
        elif key==currentNode.NodeKey:
            pass
        else:
            pass

  
    def FinMinMax(self, FromNode, FindMax=True):
        # ищем максимальное/минимальное (узел) в поддерева
        if FromNode==None or not isinstance(FromNode,BSTNode):
            return None
        key=FromNode.NodeKey
        bst=self.FindNodeByKey(key)
        if bst.NodeHasKey==True:
            if FindMax==True:
                if FromNode.RightChild==None:
                    return FromNode
                while FromNode.RightChild!=None:
                    FromNode=FromNode.RightChild
                    if FromNode.RightChild==None:
                        return FromNode
            elif FindMax==False:
                if FromNode.LeftChild==None:
                    return FromNode
                while FromNode.LeftChild!=None:
                    FromNode=FromNode.LeftChild
                    if FromNode.LeftChild==None:
                        return FromNode
            else: 
                pass
        else: 
            pass

    def GetAllNodes(self,allNodes=None):
        #Получаем все элементы дерева
        if allNodes is None:
            allNodes=[]
        if self.Root is None:
            return allNodes
        else:
            Root=self.Root
            if not (self.Root in allNodes):
                allNodes.append(self.Root)
            if Root.LeftChild!=None and Root.RightChild!=None:
                self.Root=Root.LeftChild
                allNodes.extend(self.GetAllNodes())
                self.Root=Root.RightChild
                allNodes.extend(self.GetAllNodes())
            elif Root.LeftChild!=None and Root.RightChild==None:
                self.Root=Root.LeftChild
                allNodes.extend(self.GetAllNodes())
            elif Root.LeftChild==None and Root.RightChild!=None:
                self.Root=Root.RightChild
                allNodes.extend(self.GetAllNodes())
            self.Root=allNodes[0]
            return allNodes    

    def CompareTwo(self, node_1, node_2):
        #Сравниваем ключи двух элементов
        if node_1.NodeKey>node_2.NodeKey:
            return True
        else:
            return False
    
    def TargetSearch(self,key):
        #Поиск подходящего элемента для замены
        output=[]
        nodeexist=self.FindNodeByKey(key)
        if nodeexist.NodeHasKey!=True:
            pass
        elif nodeexist.NodeHasKey==True:
            node=nodeexist.Node
            parent=node.Parent
            nodeLeftChildren=node.LeftChild
            nodeRightChildren=node.RightChild
            output.append(parent)
            output.append(nodeLeftChildren)
            output.append(nodeRightChildren)
            if nodeRightChildren!=None:
                if nodeRightChildren.LeftChild!=None:
                    leftChild=nodeRightChildren.LeftChild
                    while leftChild!=None:
                        target=leftChild
                        leftChild=leftChild.LeftChild
                    if target.RightChild!=None:
                        target=target.RightChild
                elif nodeRightChildren.LeftChild==None:
                    target=nodeRightChildren
                output.append(target) 
                return output
            elif nodeRightChildren==None and nodeLeftChildren!=None:
                return False
            elif nodeRightChildren==None and nodeLeftChildren==None:
                target=None
                output.append(target)
                return output
        else:
            return False

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        data=self.TargetSearch(key)
        if data==False: 
            return False
        else:
            parent=data[0]
            deletedLeftChildren=data[1]
            deletedRightChildren=data[2]
            target=data[3]
            if target!=None:
                target_parent=target.Parent
            #Определяем каким ребенком была цель и назначаем в это поле None
                if self.CompareTwo(target_parent, target)==True:
                    target_parent.LeftChild=None
                elif self.CompareTwo(target_parent, target)==False:
                    target_parent.RightChild=None
                else:
                    pass
            #Проверка каким ребенком родителя удаляемого элемента будет цель
                if self.CompareTwo(parent,target)==True:
                    parent.LeftChild=target
                elif self.CompareTwo(parent,target)==False:
                    parent.RightChild=target
                else:
                    pass
            #Назначение детей удаляемого элемента для подходящей цели
                if deletedLeftChildren!=None:
                    if deletedLeftChildren.NodeKey==target.NodeKey:
                        target.LeftChild=None
                    else: 
                        target.LeftChild=deletedLeftChildren
                if deletedRightChildren!=None:
                    if deletedRightChildren.NodeKey==target.RightChild:
                        target.RightChild=None
                    else:
                        target.RightChild=deletedRightChildren
            # Действия у удаляемого эл-та нет детей            
            elif deletedLeftChildren==None and deletedRightChildren==None:
                deleted=self.FindNodeByKey(key).Node
                if self.CompareTwo(parent,deleted)==True:
                    parent.LeftChild=None
                elif self.CompareTwo(parent,target)==False:
                    parent.RightChild=None
                else:
                    pass 


        
    
    def printAll(self):
        all=self.GetAllNodes()
        for node in all:
            print("*Ключ",node.NodeKey,"*Значение",node.NodeValue,"*Родитель",node.Parent,"*левый потомок",node.LeftChild,"*правый потомок",node.RightChild,"*")

    def Count(self):
        # количество узлов в дереве
        q_ty=0
        allElements=self.GetAllNodes()
        for element in allElements:
            if element.NodeKey!=None:
                q_ty+=1
        return q_ty

         

"""

A=BSTNode(9,"значение 1",None)


BT=BST(A)
print(BT.Count())
BT.AddKeyValue(3,"значение 2")
print(BT.Count())
BT.AddKeyValue(1,"значение 3")
print(BT.Count())
BT.AddKeyValue(12,"значение 4")
print(BT.Count())
BT.AddKeyValue(3,"значение 5")
print(BT.Count())
BT.AddKeyValue(47,"значение 6")
BT.AddKeyValue(59,"значение 6")
BT.AddKeyValue(42,"значение 6")
print(BT.Count())
BT.AddKeyValue(47,"значение 6")
print(BT.Count())
BT.DeleteNodeByKey(42)
print(BT.Count())

print(BT.Root.NodeKey)
print(BT.Root.NodeValue)
print(BT.Root.Parent)
print(BT.Root.LeftChild)
print(BT.Root.RightChild)
print("*********")
print(BT.Root.LeftChild.NodeKey)
print(BT.Root.LeftChild.NodeValue)
print(BT.Root.LeftChild.Parent)
print(BT.Root.LeftChild.LeftChild)
print(BT.Root.LeftChild.RightChild)
print("*********")

Z=BT.FindNodeByKey(9)
print(Z,Z.NodeHasKey)
print("*********")
ZZ=BT.FindNodeByKey(6)
print(ZZ,ZZ.NodeHasKey,ZZ.ToLeft)
print("*********")
print(BT.FinMinMax(A).NodeKey)
print(BT.FinMinMax(A,False).NodeKey)
print(BT.GetAllNodes())

print(BT.printAll())

BT.DeleteNodeByKey(1)
print("*********")
print(BT.printAll())
print(BT.Count())
"""