class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_on = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_on == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_user_page(user):
    print(f"Hi {user.name}....You page has been created..")

new_user = User("kumaresan")
new_user.is_logged_on = True
create_user_page(new_user)
