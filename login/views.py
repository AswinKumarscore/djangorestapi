from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
from django.contrib.auth.models import User

class LoginView(APIView):

    def get(self, request):
        username = request.GET['username']
        password = request.GET['password']
        try:
            get_user = User.objects.get(username=username)
        except Exception as e:
            return Response({'message':"user not found", 'success':"false"})
        
        if get_user:
            if(get_user.password == password):
                content = {'message':'Logged in', 'username':get_user.username}
                return Response(content)
            content = {'message':'Invalid password'}
            return Response(content)