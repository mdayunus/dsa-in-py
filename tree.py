class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_children(self, child):
        child.parent = self
        self.children.append(child)

    def get_lvl(self):
        count = 0
        p = self.parent
        while p:
            count += 1
            p = p.parent
        return count

    def print_tree(self):
        prefix = "|-" if self.parent else ""
        lvl = 4 * self.get_lvl()
        st = ' ' * lvl
        st = st + prefix + self.data
        print(st)
        if self.children:
            for child in self.children:
                child.print_tree()


def electronic():
    root = TreeNode('Electronics')

    laptop = TreeNode('laptop')
    macbook = TreeNode('macbook')
    surface = TreeNode('surface')
    laptop.add_children(macbook)
    laptop.add_children(surface)
    mobile = TreeNode('mobile')
    iphone = TreeNode('iphone')
    oneplus = TreeNode('oneplus')
    mobile.add_children(iphone)
    mobile.add_children(oneplus)
    root.add_children(laptop)
    root.add_children(mobile)

    return root

if __name__ == '__main__':
    root = electronic()
    root.print_tree()
    # print(root.get_lvl())
