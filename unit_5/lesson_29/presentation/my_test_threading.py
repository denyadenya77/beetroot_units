import threading
import concurrent.futures
import time

start = time.perf_counter()


# ---------------------------------------------------------------

# функция не принимает аргументов
# def do_something():
#     print('Sleeping one second...')
#     time.sleep(1)
#     print('Done sleeping...')

# вызов функций без использования потоков
# do_something()
# do_something()

# создание потоков вручную

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

# ---------------------------------------------------------------

# функиця принмиает аргумент и ничего не возвращает
# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     print('Done sleeping...')
#
# # создание потоков с помощью цикла
# threads = []
#
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()


# ---------------------------------------------------------------

# функиця принмиает аргумент и возвращает строку
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'


# использование потоков с помощью модуля concurrent.futures
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]

    # создание потоков вручную
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)
    # print(f1.result())
    # print(f2.result())

    # создание потоков с помощью списковых включений и метода .submit()
    # возвращает результат в порядке завершения работы потоков
    # results = [executor.submit(do_something, sec) for sec in secs]
    #
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())



    # создание потоков с помощью метода .map()
    # возвращает результат в порятке создания потоков
    results = executor.map(do_something, secs)
    for result in results:
        print(result)

# ---------------------------------------------------------------

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s).')
