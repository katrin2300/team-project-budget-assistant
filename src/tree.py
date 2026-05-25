class Node:
  def __init__(self, day, amount, category):
    """

    """
    self.day = day
    self.amount = amount
    self.category = category
    self.left = None
    self.right = None

class TreeNode:
  def __init__(self):
    """

    """
    self.root = None

  def insert(self, day, amount, category):
    """

    """
    if self.root is None:
      self.root = Node(day, amount, category)
      return

    cur = self.root
    while True:
      if day < cur.day:
        #влево
        if cur.left is None:
          cur.left = Node(day, amount, category)
          return
        cur = cur.left
      elif day > cur.day:
        #вправо
        if cur.right is None:
          cur.right = Node(day, amount, category)
          return
        cur = cur.right
      else:
        #день есть, тогда обновляем данные
        cur.amount = amount
        cur.category = category
        return

  def find(self, day):
    """

    """
    cur = self.root
    while cur is not None:
      if day == cur.day:
        return cur.amount, cur.category
      elif day < cur.day:
        cur = cur.left
      else:
        cur = cur.right
    return None

  def inorder_days(self):
    """

    """
    result = []

    def inorder(node):
      if node is None:
        return
      inorder(node.left)
      result.append(node.day)
      inorder(node.right)

    inorder(self.root)
    return result
