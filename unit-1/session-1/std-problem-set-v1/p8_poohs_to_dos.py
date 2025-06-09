'''
U-nderstand:
i/p = tasks: list[str]
o/p = str

Edge cases:
[] 

P-lan:
enumerate(1, tasks)

I-mplement:
'''
def print_todo_list(task):
    print("Pooh's To Dos:")
    if task:
        for number, item in enumerate(task, start = 1):
            print(f"{number}. {item}")


task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)