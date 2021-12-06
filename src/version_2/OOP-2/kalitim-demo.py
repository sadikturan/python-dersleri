# User      
# Moderator


class User:
    active_users = 0
    
    @classmethod
    def display_active_users(cls):
        return f"şu anda aktif {cls.active_users} user var."

    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        User.active_users += 1
    
    def fullname(self):
        return f"{self.firstname} {self.lastname}"


class Moderator(User):
    active_moderators = 0

    @classmethod
    def display_active_moderators(cls):
        return f"şu anda aktif {cls.active_moderators} moderator var."

    def __init__(self,firstname,lastname,community):
        super().__init__(firstname,lastname)
        self.community = community
        Moderator.active_moderators += 1

    def remove_post(self):
        return f"{self.fullname()} {self.community} grubundan bir post sildi."

    def update_post(self):
        return f"{self.fullname()} {self.community} grubunda bir post güncelledi."

print(User.display_active_users())
print(Moderator.display_active_moderators())

u1 = User("Ali","Korkmaz")
m1 = Moderator("Yağmur","Korkmaz","yazılım")
m2 = Moderator("Canan","Korkmaz","kozmetik")

print(m1.remove_post())
print(m2.update_post())

print(User.display_active_users())
print(Moderator.display_active_moderators())

# print(u1.fullname())
# print(m1.fullname())

# print(isinstance(u1, User))
# print(isinstance(u1, Moderator))

# print(isinstance(m1, User))
# print(isinstance(m1, Moderator))