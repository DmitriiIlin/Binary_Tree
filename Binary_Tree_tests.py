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

Z=simple_tree_generator()
tree_KeyNode_print(Z[-1])


class Binary_Tree_Tests(unittest.TestCase):

    # Тесты для класса Binary_Tree


    def test_Find(self):
        # Тест по поиску элемента
        Tree_data=simple_tree_generator()
        Root=Tree_data[0].NodeKey

        





if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()
