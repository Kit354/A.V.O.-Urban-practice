from multiprocessing import Pool
import time
import os


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line:
            all_data += line.strip()
            line = file.readline()
            if not line:
                break


start_time = time.time()
filenames = [f'./file {number}.txt' for number in range(1, 5)]
for second_file in filenames:
    read_info(second_file)
print(f'Линейное время выполнения:{time.time() - start_time: .2f}')

# if __name__ == '__main__':
#     start_time = time.time()
#     filenames = [f'./file {number}.txt' for number in range(1, 5)]
#     with Pool(processes=os.cpu_count()) as pool:
#         results = pool.map(read_info, filenames)
#     print(f'Многопроцессорное время выполнения:{time.time() - start_time: .2f}')
