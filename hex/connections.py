from .constants import BLACK, BLUE, RED

class Connections:
    """
    A class representing the connection between nodes with trees.
    The nodes that are connected are in the same tree.

    Attributres
    -----------
    trees : list of dictionaries, containing parent, number of children and color of each node
    """

    def __init__(self, row, col):
        self.trees = [{"parent": i, "num_child": 0, "color": "BLACK"} for i in range(row*col+4)]
        self.trees[row*col]["color"] = "BLUE"
        self.trees[row*col + 1]["color"] = "BLUE"
        self.trees[row*col + 2]["color"] = "RED"
        self.trees[row*col + 3]["color"] = "RED"

    def __repr__(self):
        return self.trees.__repr__()

    def find_root(self, x):
        """Find the root of the node x, using a recursive approch

        Parameters
        ----------
        x : int
            A node

        Returns
        -------
        int
            The root of x
        """
        if self.trees[x]["parent"] == x:
            return x
        return self.find_root(self.trees[x]["parent"])

    def union(self, x, y):
        """Combine the two trees containing the nodes x and y, only if they are
        of the same color

        Parameters
        ----------
        x : int
            The first node
        y : int
            The second node
        """
        xRoot = self.find_root(x)
        yRoot = self.find_root(y)

        if (xRoot != yRoot
            and self.trees[xRoot]["color"] == self.trees[yRoot]["color"]):
            #We use the number of child to determine which root should become
            #the parent of the other root. The idea is to have trees that are
            #flat.
            if self.trees[xRoot]["num_child"] < self.trees[yRoot]["num_child"]:
                self.trees[xRoot]["parent"] = yRoot
            else:
                self.trees[yRoot]["parent"] = xRoot
                if self.trees[xRoot]["num_child"] == self.trees[yRoot]["num_child"]:
                    self.trees[xRoot]["num_child"] += 1

        self.flatten()
    
    def flatten(self):
        """Flatten the tree by passing the root as the parent for each node"""
        for i in range(len(self.trees)):
            self.trees[i]["parent"] = self.find_root(i)