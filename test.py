from tree import Tree
from node import Node
from colours import Colour, Colours


# root = Node(Colours.BLUE)
# b = Node(Colours.BLUE)
# c = Node(Colours.BLUE)
# d = Node(Colours.BLUE)
# e = Node(Colours.BLUE)
# f = Node(Colours.BLUE)
# g = Node(Colours.BLUE)

# tree = Tree(root)
# tree.put(root, b)
# tree.put(root, c)
# tree.put(b, d)
# tree.put(b, e)
# tree.put(b, f)
# tree.put(c, g)

#print(root.children, " should be ", b,c)

# tree.rm(b)

#print(root.children, " should be ",c)

# print(b.parent, " should be ", None)


# print(tree.is_coloured_to_depth_k(root,Colours.BLUE,2))

# print("root",root.propagated_colour.NAME)
# print("b",b.propagated_colour.NAME)
# print("c",c.propagated_colour.NAME)
# print("d",d.propagated_colour.NAME)
# print("e",e.propagated_colour.NAME)
# print("f",f.propagated_colour.NAME)
# print("g",g.propagated_colour.NAME)





# # print("\n\n\n Swapping")
# # tree.swap(b,g)

# # tree.rm(b)

# # # print("\n\nroot",root.propagated_colour.NAME)
# # # print("b",b.propagated_colour.NAME)
# # # print("c",c.propagated_colour.NAME)
# # # print("d",d.propagated_colour.NAME)
# # # print("e",e.propagated_colour.NAME)
# # # print("f",f.propagated_colour.NAME)
# # # print("g",g.propagated_colour.NAME)

# # print(c.children, " should be ", b)

# # print("g is ", g)


# # print(root.children, " should be ", g, " and ", c)


A = Node(Colours.GREEN)
B = Node(Colours.GREEN)
C = Node(Colours.GREEN)
D = Node(Colours.GREEN)
E = Node(Colours.GREEN)
F = Node(Colours.RED)
G = Node(Colours.RED)

tree = Tree(A)
tree.put(A,B)
tree.put(A,D)
tree.put(B,C)
tree.put(B,F)
tree.put(F,G)
tree.put(D,E)

# print(tree.is_coloured_to_depth_k(A, Colours.BLUE, 1)) #=> FALSE

# print(tree.is_coloured_to_depth_k(A, Colours.GREEN, 0)) #=> True
# print(tree.is_coloured_to_depth_k(A, Colours.RED, 0)) #=> False
# print(tree.is_coloured_to_depth_k(A, Colours.GREEN, 1)) #=> True
# print(tree.is_coloured_to_depth_k(A, Colours.GREEN, 2)) #=> False


print(tree.is_coloured_to_depth_k(A, Colours.GREEN, 2)) #=> False