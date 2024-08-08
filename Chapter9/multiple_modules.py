from module1 import User
from module2 import Admin, Privileges

drake = Admin('Aubrey', 'Graham', 37, 'anitamaxwynn@gmail.com', 'Toronto')
drake.describe_user()

print("\nAdding privileges...")
drake_privileges = [
    'can ban users',
    'can add discussions',
    'can time out accounts',
]
drake.privileges.privileges = drake_privileges
drake.privileges.show_privileges()