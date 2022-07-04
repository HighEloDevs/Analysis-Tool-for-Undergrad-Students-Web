from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
import pandas as pd


@api_view(["POST"])
def simple_parser(request: Request) -> Response:
    print(request.data)
    return Response({"message": "simple_parser"}, status=400)
