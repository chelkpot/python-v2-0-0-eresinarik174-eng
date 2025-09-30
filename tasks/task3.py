# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    
    a, b = map(int, input().split())
    total = a + b - 1
    print(total - a, total - b)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()