import first_task
import second_task


task_number = int(input('Enter task number: '))

while task_number < 1 or task_number > 2:
    print('>:')
    task_number = int(input('Enter task number: '))

if task_number == 1:
    is_sublist = first_task.Sublist(
        input('Enter list items separated by spaces:\n').split(),
        input('Enter sublist:\n').split()
    ).is_sublist()

    if is_sublist:
        print('Second list is sublist')
    else:
        print('Second list isn\'t sublist')
if task_number == 2:
    print(
        second_task.Words(
            input('Enter words separated by comma: ')
        ).find_smallest_word()
    )
