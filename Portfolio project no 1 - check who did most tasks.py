
'''
[PL]:
Napisz program, ktory pobierze dane ze wskazanej strony, przetworzy je za pomoca
JSONa, nastepnie przetworzy je i wyszuka ktory uzytkownik wykonal najwiecej
zadan ze swojej ToDoList

[EN]:
Write a program, which takes data from website, process them with JSON and then
it will find which user did the mosts of planned tasks from his "To Do List"
'''

import requests
import json


#Created functions//-----------------------------------------------------//
def get_nr_of_completed_tasks(toDo):
    numberOfCompletedTasksByUsers = dict()
    for element in toDo:
        if element['completed'] == True:
            try:
                numberOfCompletedTasksByUsers[element['userId']] += 1
            except KeyError:
                numberOfCompletedTasksByUsers[element['userId']] = 1
    return numberOfCompletedTasksByUsers

def get_best_users_by_completed_tasks(get_nr_of_completed_tasks):
    bestUsersbyCompletedTasks = []           
    for userId, numberOfTasksDone in get_nr_of_completed_tasks.items():
        if numberOfTasksDone == max(get_nr_of_completed_tasks.values()):
            bestUsersbyCompletedTasks.append(userId)
    return bestUsersbyCompletedTasks
#Created functions//-----------------------------------------------------//


#Actual program    
try:
    websiteToDo = requests.get("https://jsonplaceholder.typicode.com/todos")
    toDo = websiteToDo.json()
    
except:
    print("Niepoprawny format, lub nie udalo sie nawiazac polaczenia ze wskazanym url")
    
else:
    get_nr_of_completed_tasks(toDo)
    get_best_users_by_completed_tasks(get_nr_of_completed_tasks(toDo))


    websiteUsers = requests.get("https://jsonplaceholder.typicode.com/users")
    users = websiteUsers.json()
    for element in users:
        nameOfBestUsers = [
                            element['name']
                            for element in users
                            if element['id'] in get_best_users_by_completed_tasks(get_nr_of_completed_tasks(toDo)) #bestUsersbyCompletedTasks
                            ]

    print("[PL]: Mistrzem/ami konczenia zadan jest/sa uzytkownik/cy:", nameOfBestUsers, "gratulujemy!\n")
    print("[EN]: Master/s of tasks completion is/are user/s:", nameOfBestUsers, "congratulations!")
            

