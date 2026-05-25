class ExpensesStack:
  def __init__(self, name):
    """
    создаёт узел дерева с названием категории
    у каждого узла есть левый и правый потомок (изначально None)
    """
    self.stack = []


def push(self, day, amount, category):
  """

  """
  self.stack.append((day, amount, category))

def pop(self):
  """

  """
  if not self.stack:
    return None
  return self.stack.pop()

def is_empty(self):
  """

  """
  return len(self.stack) == 0
