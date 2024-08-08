from admin import *

drake = Admin('Aubrey', 'Graham', 37, 'anitamaxwynn@gmail.com', 'Toronto')
drake.privileges = ['Can delete post', 'Can ban user', 'Can add post', 'Can time out user', 'Can kick user', 'Can ban user']

drake.show_privileges()