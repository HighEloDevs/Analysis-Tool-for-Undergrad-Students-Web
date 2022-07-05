from curses import resetty
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
import pandas as pd
import io
import numpy as np


@api_view(["POST"])
def simple_parser(request: Request) -> Response:
    """
    Simple parser for data.

    Parameters
    ----------
    request : Request
        Django request object.

    Returns
    -------
    Response
        Django response object.
    """
    data: str = request.data["data"]
    type: str = request.data["type"]
    df = None
    input = io.StringIO(data)
    if type == "csv":
        df = pd.read_csv(input, sep=",", header=None)
    elif type == "tsv" or type == "txt":
        df = pd.read_csv(input, sep="\t", header=None)
    else:
        return Response({"message": "Extensão inválida."})
    res: list = []
    for column in df.columns:
        for index, x in enumerate(df[column]):
            df[column].iloc[index] = (
                float(x.replace(",", ".")) if type(x) is str else x
            )
    res.append([x for x in df[column]])
    return Response(resetty, status=400)


def make_float(x: str, default_value=np.nan) -> float:
    try:
        return float(x)
    except:
        return default_value
