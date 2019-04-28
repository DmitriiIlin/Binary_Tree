import unittest, random, Binary_Tree

def simple_tree_generator(size=3):
    #создаем простое дерево
    data=[]
    for i in range(0,size):
        if i==0:
            key_Number=random.randint(10**3,10**4)
            data.append(key_Number)
        elif i==1:
            key_Number=random.randint(10**2,10**3-1)
            data.append(key_Number)
        elif i==2:
            key_Number=random.randint(10**4+1,10**5)
            data.append(key_Number)
        elif i==3:
            key_Number=random.randint(10**5+1,10**6)
            data.append(key_Number)    
        elif i==4:
            key_Number=random.randint(10**6+1,10**7)
            data.append(key_Number)    
        else:
            key_Number=random.randint(10**7+1,10**8)
            data.append(key_Number)
    Root=Binary_Tree.BSTNode(data[0],"значение %i",None)  
    Tree=Binary_Tree.BST(Root)
    for i in range(1,size):
        Tree.AddKeyValue(data[i],"значение %i")
    data.append(Tree)
    return data

def tree_KeyNode_print(Tree):
    data=Tree.GetAllNodes()
    output=[]
    for node in data:
        output.append(node.NodeKey)
    print(output)


class Binary_Tree_Tests(unittest.TestCase):

    # Тесты для класса Binary_Tree


    def test_Find(self):
        # Тест по поиску элемента
        data=simple_tree_generator()
        Tree=data[-1]
        Nodes=Tree.GetAllNodes()
        random_number=random.randint(0,len(data)-2)
        data_for_search=Nodes[random_number]
        finded_data=Tree.FindNodeByKey(data_for_search.NodeKey)
        self.assertEqual(finded_data.Node.NodeKey,data_for_search.NodeKey)
        self.assertEqual(finded_data.NodeHasKey,True)
        new_data_key_big=random.randint(10**5+1,10**6)
        new_data_key_small=random.randint(0,9)
        finded_data_big=Tree.FindNodeByKey(new_data_key_big)
        finded_data_small=Tree.FindNodeByKey(new_data_key_small)
        self.assertEqual(finded_data_big.NodeHasKey,False)
        self.assertEqual(finded_data_small.NodeHasKey,False)
        max=Nodes[0]
        min=Nodes[0]
        for i in range(0,len(Nodes)):
            if max.NodeKey< Nodes[i].NodeKey:
                max=Nodes[i]
            parent_big=max
            if Nodes[i].NodeKey<min.NodeKey:
                min=Nodes[i]
            parent_small=min
        self.assertEqual(finded_data_big.Node.NodeKey, parent_big.NodeKey)
        self.assertEqual(finded_data_small.Node.NodeKey, parent_small.NodeKey)

    def test_New_Node(self):
        #Тест по добавлению нового узла. 
        data=simple_tree_generator()
        Tree=data[-1]
        new_data_key_big=random.randint(10**5+1,10**6)
        res=Tree.FindNodeByKey(new_data_key_big)
        self.assertEqual(False,res.NodeHasKey)
        Tree.AddKeyValue(new_data_key_big,"New right child")
        res=Tree.FindNodeByKey(new_data_key_big)
        self.assertEqual(True,res.NodeHasKey)
        new_data_key_small=random.randint(0,9)
        res=Tree.FindNodeByKey(new_data_key_small)
        self.assertEqual(False,res.NodeHasKey)
        Tree.AddKeyValue(new_data_key_small,"New left child")
        res=Tree.FindNodeByKey(new_data_key_small)
        self.assertEqual(True,res.NodeHasKey)
        all_nodes_0=Tree.GetAllNodes()
        Tree.AddKeyValue(new_data_key_big,"New right child")
        all_nodes_1=Tree.GetAllNodes()
        self.assertEqual(all_nodes_0,all_nodes_1)

    def test_Max_Min(self):
        #Поиск минимального и максимального значений
        data=simple_tree_generator()
        Tree=data[-1]
        all_nodes=Tree.GetAllNodes()
        max=all_nodes[0]
        min=all_nodes[0]
        for i in range(0,len(all_nodes)):
            if max.NodeKey< all_nodes[i].NodeKey:
                max=all_nodes[i]
            if all_nodes[i].NodeKey<min.NodeKey:
                min=all_nodes[i]
        finMax=Tree.FinMinMax(Tree.Root)
        finMin=Tree.FinMinMax(Tree.Root,False)
        self.assertEqual(max,finMax) 
        self.assertEqual(min,finMin) 
        #Блок поиска мин. и макс элемента в под-дереве
        data=simple_tree_generator(5)
        Tree=data[-1]
        all_nodes=Tree.GetAllNodes()
        max=all_nodes[2]
        min=all_nodes[2]
        finMax=Tree.FinMinMax(max)
        finMin=Tree.FinMinMax(min,False)
        for i in range(2,len(all_nodes)):
            if max.NodeKey< all_nodes[i].NodeKey:
                max=all_nodes[i]
            if all_nodes[i].NodeKey<min.NodeKey:
                min=all_nodes[i]
        self.assertEqual(max,finMax) 
        self.assertEqual(min,finMin)
        
    def test_delete(self):
        # Тест удаления элемента
        data=simple_tree_generator()
        Tree=data[-1]
        key_for_delete=data[1]
        print(key_for_delete)
        tree_KeyNode_print(Tree)
        self.assertEqual(Tree.Root.LeftChild.NodeKey,key_for_delete)
        Tree.DeleteNodeByKey(key_for_delete)
        tree_KeyNode_print(Tree)
        self.assertEqual(Tree.Root.LeftChild,None)



    












        



        











        





if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()
