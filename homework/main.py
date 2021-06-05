class Credentials:
  # we need to give an user and password
  def __init__(self, user, password):
    # save the variables to the object
    self.user = user
    self.password = password

# extend Credentials
class EmptyCredentials(Credentials):
  def __init__(self):
    # call the parent (Credential) constructor
    super().__init__("", "")

dict = {"amazon": Credentials("corman", "123456"),
        "netflix": Credentials("corman", "abcdefg"),
        "spotify": Credentials("corman", "12344321")}

def get_user_and_password(website_name):
  try:
    return dict[website_name]
  # if an exception of type KeyError occurs, execute the code in except
  except KeyError:
    return EmptyCredentials()