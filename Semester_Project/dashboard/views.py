import json

import numpy as np
from django.shortcuts import render


class SineWaveData:
    values: int = []
    labels: str = []

    def __init__(self):
        labels = np.linspace(0, 1000, 1000, dtype=int)
        values = np.sin(labels * np.pi ** 2)
        self.values = json.dumps(values.tolist())
        self.labels = json.dumps(labels.tolist())


def index(request):
    template = 'dashboard/sinewave.html'
    data = SineWaveData()
    context = {
        "data": data,
    }
    return render(request, template, context)


def sinewave(request):
    template = 'dashboard/sinewave.html'
    data = SineWaveData
    context = {
        "data": data,
    }
    return render(request, template, context)
