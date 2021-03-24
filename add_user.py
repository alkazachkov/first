import gitlab

gl = gitlab.Gitlab('http://127.0.0.1:8080', private_token='My_token')

user = gl.users.create({'email': 'ivanov@mycompany.com',
                        'password': 'super_pass',
                        'username': 'ivanov',
                        'name': 'Ivan Ivanov'})

users = gl.users.list(active=True)

print(users)
