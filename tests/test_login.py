import sys


sys.path.append('.')
sys.path.append('..')


from McDaily.account import McDailyAccount


username = input('Username : ')
password = input('Password : ')


account  = McDailyAccount()
response = account.login(username, password)


print(response.json())
print('Token : ' + account.access_token)
