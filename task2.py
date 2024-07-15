from collections import deque

def is_palindrome(s: str) -> bool:
    # Видаляємо пробіли та переводимо рядок до нижнього регістру
    s = ''.join(s.split()).lower()
    
    # Створюємо двосторонню чергу
    dq = deque(s)
    
    # Порівнюємо символи з обох кінців черги
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    
    return True

# Приклади використання функції
print(is_palindrome("A man a plan a canal Panama")) # True
print(is_palindrome("racecar"))                     # True
print(is_palindrome("hello"))                       # False
