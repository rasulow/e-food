from jwt import decode, InvalidTokenError
from django.contrib.auth.models import User
from django.conf import settings


def get_user(request):
    token = request.headers.get('Authorization')
    user = None
    
    if token:
        try:
            decoded_token = decode(token.split()[1], settings.SECRET_KEY, algorithms=["HS256"])
            print(decoded_token)
            if decoded_token.get('token_type') == 'access':
                user_id = decoded_token['user_id']
                if User.objects.filter(id=user_id).exists():
                    user = User.objects.get(id=user_id)
        except InvalidTokenError:
            pass
        
    return user