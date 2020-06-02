# McDaily

> Please note that this app might stop working in the near future, as
> they have changed the hashing algorithm from simple MD5 to
> AES encryption + Base64 hashing using a differently formatted string.

API wrapper for interacting with the Taiwan McDaily app.

# Installation

```sh
$ python setup.py install
```

## Example

Obtains the login token
```py
from McDaily import McDailyAccount


# Input
username = input('Username : ')
password = input('Password : ')

# Login
account = McDailyAccount()
response = account.login(username, password)

# Print the results
print('')
print('Login status : ' + response['rm'])
print('Username     : ' + response['results']['member_info']['name']['last_name'] + response['results']['member_info']['name']['first_name'])
print('Token        : ' + response['results']['member_info']['access_token'])
```

You can also fill in the token yourself
```py
from McDaily import McDailyAccount


account = McDailyAccount()
account.set_token('Your token')

# Lottery
print(account.lottery_get_item())

# Get coupon list
print(account.lottery_get_item())
```

## Contributing

Thanks Still34
