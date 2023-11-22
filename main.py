import calendar
from datetime import date
from colorama import Fore, Style


def display_calendar_with_tasks(year, month, days_with_tasks, description_to_tasks):

    task_day_color = Fore.YELLOW + Style.BRIGHT
    reset_color = Style.RESET_ALL


    display_month = calendar.monthcalendar(year, month)


    print(f'{task_day_color}{calendar.month_name[month]} {year}{reset_color}')


    print('Mo Tu We Th Fr Sa Su')


    for week in display_month:
        for day in week:
            if day == 0:
                print('  ', end=' ')
            elif day in days_with_tasks:
                print(f'{task_day_color}{day:2}{reset_color}', end=' ')
            else:
                print(f'{day:2}', end=' ')
        print()


current_date = date.today()
current_month = current_date.month
current_year = current_date.year


days_with_tasks = []
description_to_tasks = {}

while True:

    display_calendar_with_tasks(current_year, current_month, days_with_tasks, description_to_tasks)
    print("Enter")
    print("1 - if you want to assign task to day")
    print("2 - if you want to delete task")
    print("3 - if you want to display task from selected day")
    decision = input(">")
    if decision == "1":
        print("Enter the day number you want to add a task")
        task = int(input(">"))
        days_with_tasks.append(task)
        print("Add description to task")
        description = input(">")
        description_to_tasks[task] = description
    elif decision == "2":
        print("Enter the day number you want to remove")
        day_to_remove = int(input(">"))
        if day_to_remove in days_with_tasks:
            days_with_tasks.remove(day_to_remove)
            del description_to_tasks[day_to_remove]
        else:
            print("Day not found in the list.")
    elif decision == "3":
        print("Enter the day number")
        day_to_show = int(input(">"))
        if day_to_show in days_with_tasks:
            print(description_to_tasks.get(day_to_show, "No description available."))
        else:
            print("Day not found in the list.")
