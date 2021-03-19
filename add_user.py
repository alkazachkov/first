import gitlab

gl = gitlab.Gitlab('http://127.0.0.1:8080', private_token='RnqybwHh3svn3p_ic28_')

user = gl.users.create({'email': 'ivanov@mycompany.com',
                        'password': 'scur3s3cr3T',
                        'username': 'ivanov',
                        'name': 'Ivan Ivanov'})

users = gl.users.list(active=True)

print(users)
