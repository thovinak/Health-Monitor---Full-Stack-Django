import numpy as np
from django.shortcuts import render


def index(request):
    data = []
    values = np.linspace(0, 1000, 1000)
    values = np.sin(values * np.pi ** 2)
    FFT = fft_sine(values)
    for i in range(len(values)):
        data.append({'label': i, 'value': values[i], "fft": FFT[i]})

    if (request.method == "GET"):
        pass
    gets = {"fft_hide": request.GET.get('fft_hide')}
    debug = request.method
    context = {
        "data": data,
        "gets": gets,
        "debug": debug
    }
    page = 'tabulation/sinewave.html'  # just a variable to make it easier to change the page
    return render(request, page, context)


def sine_wave(request):
    data = []
    values = np.linspace(0, 1000, 1000)
    values = np.sin(values * np.pi ** 2)
    FFT = fft_sine(values)
    for i in range(len(values)):
        data.append({'label': i, 'value': values[i], "fft": FFT[i]})

    gets = {"fft_hide": request.GET.get('fft_hide')}
    debug = request.method
    context = {
        "data": data,
        "gets": gets,
        "debug": debug
    }
    page = 'tabulation/sinewave.html'
    return render(request, page, context)

def ecg_signal(request):
    data = []
    amplitude = 1  # 1V
    frequency = 1.25  # 1.25Hz
    plot_freq = 1000  # 1ms
    noise_level = 0.5  # 0.5V
    t = np.linspace(0, 1, plot_freq)

    values = amplitude * (np.sin(2 * np.pi * frequency * t) + 0.5 * np.sin(2 * np.pi * 2 * frequency * t))
    noise = np.random.normal(0, noise_level, len(values))
    values = noise + values
    FFT = fft_sine(values)
    for i in range(len(values)):
        data.append({'label': i, 'value': values[i], "fft": FFT[i]})

    gets = {"fft_hide": request.GET.get('fft_hide')}
    debug = request.method
    context = {
        "data": data,
        "gets": gets,
        "debug": debug
    }
    page = 'tabulation/ecgsignal.html'
    return render(request, page, context)

def fft_sine(data):
    data = np.fft.fft(data)
    return data