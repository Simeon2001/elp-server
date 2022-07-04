from rest_framework.decorators import api_view

from terminal.serializers import Command_serializer
from .models import Command_Bank
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


@api_view(["post"])
def Add_command(request):
    if request.method == "POST":
        framework = request.data.get("framework")
        print(framework)
        title = request.data.get("title")
        command = request.data.get("command")
        store = Command_Bank.objects.create(framework=framework, title=title, command=command)
        return Response(
                {
                    "status": True,
                    "message": "command saved under {0}".format(framework),
                },
                status=status.HTTP_201_CREATED,
            )

@api_view(["post"])
def search_command(request):
    if request.method == "POST":
        query = request.data.get("search")
        print(query)
        data = Command_Bank.objects.filter(Q(framework__icontains=query) | Q(title__icontains=query))
        serializer_class = Command_serializer(data,many=True)
        return Response(serializer_class.data)
        print(data)
