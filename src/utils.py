def find_day_with_max_expense(daily_expenses):
  """

  """
  max_day = None
  max_amount = -1.0

  #
  for day in range(1, len(daily_expenses)):
    amount = daily_expenses[day]
    if amount > max_amount:
      max_amount = amount
      max_day = day

  #
  if max_day is None or max_amount <= 0:
    return None

  return max_day, max_amount

def insertion_sort_categories_by_total(daily_expenses, daily_categories):
  """

  """
  #1. 
  category_totals = {} #

  for day in range(1, len(daily_expenses)):
    category = daily_categories[day]
    amount = daily_expenses[day]

    if category = '':
      continue #

    if category not in category_totals:
      category_totals[category] = 0.0

    category_totals[category] += amount

  #
  categories = list(category_totals.items())

  #2. 
  #
  n = len(categories)
  for i in range(1, n):
    key_cat, key_amt = categories[i]
    j = i - 1

    #
    while j >= 0 and categories[j][1] > key_amt:
      categories[j + 1] = categories[j]
      j -= 1

    #
    categories[j + 1] = (key_cat, key, amt)

  return categories
