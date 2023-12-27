from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def endpoint(request):
    data = ['advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def advocate_list(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''

        advocates = Advocate.objects.filter(Q(bio__icontains=query)|Q(username__icontains=query)|Q(id__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)   
        return Response(serializer.data)

    if request.method == 'POST':
        advocate = Advocate.objects.create(
            username = request.data['username'],
            bio = request.data['bio'],
            id = request.data['id'],
        )
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)


# class view based API
class AdvoctaesDetail(APIView):

    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            return JsonResponse({'message': 'User does not exist'}, status=404)
        

    def get(self, request, username):
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def put(self, request, username):
        advocate = self.get_object(username)

        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.id = request.data['id']

        serializer = AdvocateSerializer(advocate, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def delete(self, request, username):
        advocate = self.get_object(username)
        advocate.delete()

        return Response('User was deleted')

# @api_view(['GET','PUT','DELETE'])
# def advocates_detail(request, username):
#     advocate = Advocate.objects.get(username=username)
    
#     if request.method == 'GET':
#         serialize = AdvocateSerializer(advocate, many=False)
#         return Response(serialize.data)

#     if request.method == 'PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
#         advocate.id = request.data['id']

#         advocate.save()

#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)
    
#     if request.method == 'DELETE':
#         advocate.delete()

#         return Response('User was deleted')


@api_view(['GET'])

def company_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)