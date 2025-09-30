# tasks/task2.py

def solve():
# Ниже пишите решение задачи

    # Читаем входные данные
    x, y, z = map(int, input().split())
    
    # Известные цены
    pencil_price = 3  # цена карандаша
    pen_price = pencil_price + 2  # цена ручки (на 2 рубля больше карандаша)
    marker_price = pen_price + 7  # цена фломастера (на 7 рублей больше ручки)
    
    # Вычисляем общую стоимость
    total_cost = x * pencil_price + y * pen_price + z * marker_price
    
    # Выводим результат
    print(total_cost)

if __name__ == "__main__":
    solve()
   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()