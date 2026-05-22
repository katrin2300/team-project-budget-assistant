from budget import BudgetManager
from stack import UndoStack
from tree import ExpenseTree
from utils import insertion_sort_by_amount

def main():
    manager = BudgetManager()
    undo_stack = UndoStack()
    
    while True:
        print("\n" + "=" * 40)
        print("      БЮДЖЕТНЫЙ ПОМОЩНИК")
        print("=" * 40)
        print("1. Добавить расход")
        print("2. Сумма за период (день A - B)")
        print("3. День с максимальным расходом")
        print("4. Топ категорий по сумме трат")
        print("5. Отменить последний расход")
        print("6. Показать дерево трат по дням")
        print("0. Выход")
        print("-" * 40)
        
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            try:
                day = int(input("   День (1-31): "))
                if day < 1 or day > 31:
                    print("   ❌ День должен быть от 1 до 31")
                    continue
                
                amount = float(input("   Сумма (руб): "))
                if amount < 0:
                    print("   ❌ Сумма не может быть отрицательной")
                    continue
                
                category = input("   Категория (еда/транспорт/кафе и т.д.): ")
                
                manager.add_expense(day, amount, category)
                undo_stack.push(day, amount, category)
                print(f"   ✅ Добавлено: {day}.{category} → {amount} руб.")
                
            except ValueError:
                print("   ❌ Ошибка! Введите число корректно")
        
        elif choice == "2":
            try:
                a = int(input("   День начала (A): "))
                b = int(input("   День конца (B): "))
                total = manager.get_sum_for_period(a, b)
                print(f"   💰 Сумма расходов с {a} по {b} день: {total:.2f} руб.")
            except ValueError:
                print("   ❌ Ошибка ввода")
        
        elif choice == "3":
            day = manager.find_day_with_max_expense()
            if day:
                print(f"   📊 День с максимальными тратами: {day}")
            else:
                print("   ❌ Нет данных. Добавьте хотя бы один расход.")
        
        elif choice == "4":
            totals = manager.get_category_totals()
            if not totals:
                print("   ❌ Нет данных. Добавьте хотя бы один расход.")
                continue
            
            sorted_cats = insertion_sort_by_amount(totals)
            print("   📊 Траты по категориям (от большего к меньшему):")
            for cat, amt in sorted_cats:
                print(f"      • {cat}: {amt:.2f} руб.")
        
        elif choice == "5":
            undone = undo_stack.pop()
            if undone:
                day, amount, category = undone
                # Удаляем последнее вхождение (поиск с конца)
                for i in range(len(manager.expenses) - 1, -1, -1):
                    e = manager.expenses[i]
                    if e.day == day and e.amount == amount and e.category == category:
                        manager.expenses.pop(i)
                        break
                manager._rebuild_prefix()
                print(f"   ↩️  Отменён расход: {day}.{category} → {amount} руб.")
            else:
                print("   ❌ Нечего отменять (стек пуст)")
        
        elif choice == "6":
            if not manager.expenses:
                print("   ❌ Нет данных. Добавьте хотя бы один расход.")
                continue
            
            # Собираем суммы по дням
            daily = {}
            for e in manager.expenses:
                daily[e.day] = daily.get(e.day, 0) + e.amount
            
            # Строим дерево
            tree = ExpenseTree()
            for day, total in daily.items():
                tree.insert(day, total)
            
            print("   🌳 Дерево трат (обход в порядке возрастания дней):")
            for day, total in tree.inorder():
                print(f"      День {day}: {total:.2f} руб.")
        
        elif choice == "0":
            print("\n   Спасибо за использование! До свидания 👋")
            break
        
        else:
            print("   ❌ Неверный выбор. Введите число от 0 до 6.")

if __name__ == "__main__":
    main()
