import os
class User:
  # constructor of class, receives its username
  def __init__(self, username):
    self.username = username
    self.file_path = "user_" + self.username # we generate the file path here
  def save(self):
    file_path = "user_" + self.username
    try:
      # try to open file will succeed if already exists
      file = open(self.file_path)
      file.close()
      return ("User already exists")
    except:
      # if the file does not exist and we can't open it, we create it
      file = open(self.file_path, "w")
      file.close()
      return "User added"
  def remove(self):
    file_path = "user_" + self.username
    try:
      os.remove(file_path) # try to remove the file with name user_
      print("Removed user")
      return True
    except:
      print("User does not exist")
      return False
  def rename(self, new_username):
    succes = self.remove()# delete the current file
    if not succes:
      return
    self.username = new_username
    self.file_path = "user_" + self.username # change the file path variable
    self.save() # save the new file

