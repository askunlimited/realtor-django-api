from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
# ...
@csrf_exempt
def my_view(request):
    if request.method == 'POST':
        # ...
        return Response(status=204)
    else:
        return Response(status=405)


class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']


        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})
            else:
                if len(password) < 8:
                    return Response({'error': 'Password must be at least 8 characters long'})
                else:
                    user = User.objects.create_user(email=email, password=password, name=name)
                    user.save()
                    return Response({'success': 'Successfully created user'})

        else:
            return Response({'error': 'Passwords must match'})