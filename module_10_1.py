import threading
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count + 1):
            file.write(str(f'Какое-то слово № {i} \n'))
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


# Работа функций
time1 = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time2 = time.time()
end_time = time2 - time1
print(f'Работа потоков {end_time:.6f}')

# Работа потоков
time3 = time.time()
thread = threading.Thread(target=write_words, args=(10, 'example5.txt',))
thread.start()

thread1 = threading.Thread(target=write_words, args=(30, 'example6.txt',))
thread1.start()

thread2 = threading.Thread(target=write_words, args=(200, 'example7.txt',))
thread2.start()

thread3 = threading.Thread(target=write_words, args=(100, 'example8.txt',))
thread3.start()
thread.join()
thread1.join()
thread2.join()
thread3.join()
time4 = time.time()
end_time = time4 - time3
print(f'Работа потоков {end_time:.2f}')
