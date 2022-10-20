from rest_framework.decorators import api_view

from terminal.serializers import Command_serializer
from .models import Command_Bank
from rest_framework.response import Response
from rest_framework import status
from django.contrib.postgres.search import SearchVector, SearchQuery


@api_view(["post"])
def Add_command(request):
    if request.method == "POST":
        framework = request.data.get("framework")
        title = request.data.get("title")
        command = request.data.get("command")
        store = Command_Bank.objects.create(framework=framework, title=title, command=command)
        return Response(
                {
                    "status": True,
                    "message": "command saved under {0} collections".format(framework),
                },
                status=status.HTTP_201_CREATED,
            )

@api_view(["post"])
def search_command(request):
    if request.method == "POST":
        query = request.data.get("search")
        data = Command_Bank.objects.filter(title__icontains=query)
        data = Command_Bank.objects.annotate(search=SearchVector("title", "framework", "command")).filter(search=SearchQuery(query))
        serializer_class = Command_serializer(data,many=True)
        return Response(serializer_class.data)
