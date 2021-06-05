import requests

# requests.delete("http://127.0.0.1:5000/task/3")
from src.persistance.repository import TaskRepository
from src.persistance.task_store_sql import TaskStoreSql

if __name__ == "__main__":
  store = TaskStoreSql('..\\src\\database\\task_db')
  tasks = store.get_all("type2")
  print(tasks)
  # repo = TaskRepository(TaskStoreSql())
  # tasks = repo.get()
  # print(tasks)
  # tasks_of_type = [t.name for t in tasks if t.task_type == "cooding"]
  # print(tasks_of_type)