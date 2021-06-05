from abc import ABC, abstractmethod
from typing import List


class TaskStore(ABC):
  @abstractmethod
  def get_all(self) -> List[dict]:
    pass

  @abstractmethod
  def add(self, task_info: dict):
    pass

  @abstractmethod
  def delete(self, task_name: str):
    cursor.execute(command)
    connection.commit()

  def update(self, old_name: str, new_name: str):
    with self.__get_connection() as connection:
      cursor = connection.cursor()
      command = f"UPDATE tasks SET name='{new_name}' WHERE name='{old_name}'"
      cursor.execute(command)
      connection.commit()