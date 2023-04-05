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


class ECGSignalData:
    values: int = []
    labels: str = []

    def __init__(self):
        amplitude = 1  # 1V
        frequency = 1.25  # 1.25Hz
        plot_freq = 1000  # 1ms
        noise_level = 0.5  # 0.5V
        t = np.linspace(0, 1, plot_freq)

        labels = np.linspace(0, 1000, 1000, dtype=int)
        y = amplitude * (np.sin(2 * np.pi * frequency * t) + 0.5 * np.sin(2 * np.pi * 2 * frequency * t))

        noise = np.random.normal(0, noise_level, len(y))
        values = noise + y
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


def ecgsignal(request):
    template = 'dashboard/ecgsignal.html'
    data = ECGSignalData
    context = {
        "data": data,
    }
    return render(request, template, context)
