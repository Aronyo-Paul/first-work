class User:
  activities = ["Post", "Like", "Comment"]
  def __init__(self, name,email):
    self.name = name
    self.email = email
  def UserActivity(self, activityType):
    if activityType in User.activities:
      return True
    else:
      return False
  def userDetail(self):
    return f"User Detail:\nName:{self.name}\nEmail: {self.email}"

class BracbookUser(User):
  def __init__(self,name,email,no = "Not set", active = False):
    super().__init__(name,email)
    self.no = no
    self.active = active
    self.activelog = []
  def UserActivity(self,activity):
    if super().UserActivity(activity):
      self.activelog.append(activity)
      self.active = True
      print(f"{self.name} has {activity}(d/ed) successfully")
    else:
      print(f"No activities found like {activity}")
  def userDetail(self):
    return super().userDetail() +f"\nPhone: {self.no}\nActivity: {(', ').join(self.activelog) if self.active else 'No recent activity.'}" 


user1 = BracbookUser("Rakait","xyz@gmail.com")
print("1===========================")
print(user1.userDetail())
print("2===========================")
user2 = BracbookUser("Sazzad","abc@gmail.com",
"01727xxxxxx")
print("3===========================")
print(user2.userDetail())
print("4===========================")
user1.UserActivity("Like")
print("5===========================")
user1.UserActivity("Comment")
print("6===========================")
print(user1.userDetail())
print("7===========================")
user2.UserActivity("Share")
print("8===========================")
user2.UserActivity("Comment")
print("9===========================")
print(user2.userDetail())
