from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Expense:
    day: int
    amount: float
    category: str

class BudgetManager:
    def __init__(self):
        self.expenses: List[Expense] = []
        self.prefix_sums: List[float] = []
    
    def add_expense(self, day: int, amount: float, category: str):
        self.expenses.append(Expense(day, amount, category))
        self._rebuild_prefix()
    
    def _rebuild_prefix(self):
        if not self.expenses:
            self.prefix_sums = []
            return
        max_day = max(e.day for e in self.expenses)
        daily = [0.0] * (max_day + 2)
        for e in self.expenses:
            daily[e.day] += e.amount
        self.prefix_sums = [0.0] * (max_day + 2)
        for i in range(1, len(self.prefix_sums)):
            self.prefix_sums[i] = self.prefix_sums[i-1] + daily[i]
    
    def get_sum_for_period(self, day_a: int, day_b: int) -> float:
        if day_a > day_b:
            day_a, day_b = day_b, day_a
        if day_a <= 0:
            day_a = 1
        if day_b >= len(self.prefix_sums):
            day_b = len(self.prefix_sums) - 1
        if day_b < day_a:
            return 0.0
        return self.prefix_sums[day_b] - self.prefix_sums[day_a - 1]
    
    def find_day_with_max_expense(self) -> Optional[int]:
        if not self.expenses:
            return None
        daily_sum = {}
        for e in self.expenses:
            daily_sum[e.day] = daily_sum.get(e.day, 0) + e.amount
        return max(daily_sum, key=daily_sum.get)
    
    def get_category_totals(self):
        totals = {}
        for e in self.expenses:
            totals[e.category] = totals.get(e.category, 0) + e.amount
        return list(totals.items())
