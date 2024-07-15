import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()

# Унікальний ідентифікатор для заявок
request_id = 0

def generate_request():
    global request_id
    request_id += 1
    request = f"Request-{request_id}"
    request_queue.put(request)
    print(f"Generated: {request}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processing: {request}")
        # Імітація обробки заявки (наприклад, затримка)
        time.sleep(random.uniform(0.5, 2.0))
        print(f"Completed: {request}")
    else:
        print("Queue is empty")

def main():
    while True:
        # Перевірка користувацького вводу
        user_input = input("Enter 'exit' to quit or press Enter to continue: ")
        if user_input.lower() == "exit":
            print("Exiting program...")
            break
        
        # Імітація генерації нових заявок
        generate_request()
        
        # Імітація обробки заявок
        process_request()
        
        # Затримка між ітераціями головного циклу
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    main()
