# def process_student(name):
#     std = Student(name)
#     # std是局部變量，但是每個函數都要用它，因此必須傳進去
#     do_task_1(std)
#     do_task_2(std)
#
#
# def do_task_1(std):
#     do_subtask_1(std)
#     do_subtask_2(std)
#
#
# def do_task_2(std):
#     do_subtask_2(std)
#     do_subtask_2(std)
#
#
# global_dict = {}
#
#
# def std_thread(name):
#     std = Student(name)
#     # 把std放到全局變量global_dict中：
#     global_dict[threading.current_thread()] = std
#     do_task_1()
#     do_task_2()
#
#
# def do_task_1():
#     # 不傳入std,而是根據當前線程查找
#     std = global_dict[threading.current_thread()]
#
#
# def do_task_2():
#     # 任何函數都可以查找出當前線程的std變量
#     std = global_dict[threading.current_thread()]


import threading


# 創建全局ThreadLocal對象
local_school = threading.local()

def process_student():
    # 獲取當前純種關聯的student:
