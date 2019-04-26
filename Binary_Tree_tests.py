import unittest, random, Binary_Tree

def simple_tree_generator(size=3):
    #создаем простое дерево
    data=[]
    for i in range(0,size):
        key_Number=random.randint(10,10**4)
        data.append(key_Number)
    Root=Binary_Tree.BSTNode(data[0],"значение %i",None)  
    Tree=Binary_Tree.BST(Root)
    for i in range(1,size):
        Tree.AddKeyValue(data[i],"значение %i")
    data.append(Tree)
    return data

def tree_KeyNode_print(Tree):
    data=Tree.GetAllNodes()
    for node in data:
        print(node.NodeKey)


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
        new_data_key_big=random.randint(10**4+1,10**5)
        new_data_key_small=random.randint(0,9)
        finded_data_big=Tree.FindNodeByKey(new_data_key_big)
        finded_data_small=Tree.FindNodeByKey(new_data_key_small)
        self.assertEqual(finded_data_big.NodeHasKey,False)
        self.assertEqual(finded_data_small.NodeHasKey,False)
        max=Nodes[0].NodeKey
        min=Nodes[0].NodeKey
        for i in range(0,len(Nodes)-1):
            if max< Nodes[i].NodeKey:
                max=Nodes[i]
            parent_big=max
            if Nodes[i].NodeKey<min:
                min=Nodes[i]
            parent_small=min
        self.assertEqual(finded_data_big.Node.NodeKey, parent_big)
        self.assertEqual(finded_data_small.Node.NodeKey, parent_small.NodeKey)
        











        





if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()
