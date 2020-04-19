from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
from django.contrib.auth.models import User

class RegisterView(APIView):

    def post(self, request):
        content = {'message':'Invalid password'}

        username = request.data['username']
        password = request.data['password']
        
        try:
            get_user = User.objects.get(username=username)
        except Exception as e:
            get_user= None


        if get_user:
            content = {'message':'user created', 'data':request.data}
            return Response({'message':"user already present. please try other username", 'success':"false"})

        try:
            user = User.objects.create_user(username, password)
        except Exception as e:
            return Response({'message':"failed to register user", 'success':'false'})
        
        if user:
            content = {'message':'user created', 'data':request.data, 'success':'true'}
            return Response(content)