from jwt import decode, InvalidTokenError
from rest_framework_simplejwt.tokens import AccessToken

def decode_jwt_token(token):
    try:
        decoded_token = decode(token, None, False)
        if decoded_token.get('token_type') == 'access':
            access_token = AccessToken(decoded_token['access'])
            # Extract user ID from the decoded access token
            user_id = access_token.payload['user_id']
            return user_id
    except InvalidTokenError:
        pass

# Example usage:
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExMzAzNDk4LCJpYXQiOjE3MTEzMDMxOTgsImp0aSI6IjBkYTk4MjFkNTA4ZjQ2Yjg5YjcwM2NkZWE1ZTA4YTE4IiwidXNlcl9pZCI6Mn0.o1A-X-tmKetXPELal8mJzYCYc_EAHce036gIMuojYAA"
user_id = decode_jwt_token(token)
if user_id:
    print("User ID:", user_id)
else:
    print("Invalid token or token type")