import datetime
import time
from http import HTTPStatus

import numpy as np
from django.db import connection
from django.shortcuts import render
from scipy.fft import fft, fftfreq
from scipy.signal.windows import blackman


def index(request):
    if "start_time" in request.GET:
        start_time = request.GET['start_time']
        start_time = datetime.datetime.strptime(start_time, '%H:%M')

        start_time = start_time.replace(year=datetime.datetime.now().year, month=datetime.datetime.now().month,
                                        day=datetime.datetime.now().day)
        start_time = time.mktime(start_time.timetuple())
    else:
        start_time = time.time()

    if 'queries' in request.GET:
        queries = request.GET['queries']
    else:
        queries = 1000
    data = get_sin_data(start_time, queries)

    if data == [] or data == ():
        template = 'error.html'
        return render(request, template)

    f_min = 25  # Minimum freq for sample, usually 25Hz
    f_max = 50e3  # Maximum freq for sample, usually 50kHz

    fft_data = data
    fft_data = fourier_transform(fft_data, f_min, f_max)
    fft_data['y'] = fft_data['y'][:, 0]
    fft_window = data
    fft_window = fourier_windowed_transform(fft_window, f_min, f_max)
    fft_window['y'] = fft_window['y'][:, 0]

    template = 'fourier/sinewave.html'
    start_time = datetime.datetime.fromtimestamp(start_time).strftime('%H:%M')
    # if request.user.is_authenticated:
    #     profile_picture = request.user.profile.profile_picture
    # else:
    #     profile_picture = "profile_pictures/user_placeholder.svg"
    context = {
        "queries": queries,
        "start_time": start_time,
        'fft_data': fft_data,
        'fft_window': fft_window,
        # 'profile_picture': profile_picture
    }
    return render(request, template, context)


def sin_wave(request):
    return index(request)


def heart_beat(request):
    if "start_time" in request.GET:
        start_time = request.GET['start_time']
        start_time = datetime.datetime.strptime(start_time, '%H:%M')

        start_time = start_time.replace(year=datetime.datetime.now().year, month=datetime.datetime.now().month,
                                        day=datetime.datetime.now().day)
        start_time = time.mktime(start_time.timetuple())
    else:
        start_time = time.time()

    if 'queries' in request.GET:
        queries = request.GET['queries']
    else:
        queries = 300
    data = get_sin_data(start_time, queries)

    if data == [] or data == ():
        template = 'error.html'
        return render(request, template)

    f_min = 25  # Minimum freq for sample, usually 25BPM
    f_max = 180  # Maximum freq for sample, usually 180BPM

    fft_data = fourier_transform(data, f_min, f_max)
    fft_data['y'] = fft_data['y'][:, 0]
    fft_window = fourier_windowed_transform(data, f_min, f_max)
    fft_window['y'] = fft_window['y'][:, 0]

    template = 'fourier/heartbeat.html'
    start_time = datetime.datetime.fromtimestamp(start_time).strftime('%H:%M')
    # if request.user.is_authenticated:
    #     profile_picture = request.user.profile.profile_picture
    # else:
    #     profile_picture = "profile_pictures/user_placeholder.svg"
    context = {
        "queries": queries,
        "start_time": start_time,
        'fft_data': fft_data,
        'fft_window': fft_window,
        # 'profile_picture': profile_picture
    }
    return render(request, template, context)


def get_sin_data(time_stamps, records):
    cur = connection.cursor()
    command = "SELECT data_val from dashboard_sinedata where label between  FROM_UNIXTIME({time})-interval 1 minute and FROM_UNIXTIME({time}) limit {records}".format(
        time=time_stamps, records=records)
    cur.execute(command)
    return cur.fetchall()


def get_heartbeat_data(time_stamps, records):
    cur = connection.cursor()
    command = "SELECT value,time_stamp from dashboard_heartbeatdata where label between  FROM_UNIXTIME({time})-interval 1 minute and FROM_UNIXTIME({time}) limit {records}".format(
        time=time_stamps, records=records)
    cur.execute(command)
    return cur.fetchall()


def fourier_transform(data, f_min, f_max):
    data = np.array(data, dtype=float)  # Converts decimal to float for pythonification
    T = float(f_min / f_max)
    N = data.shape[0]
    yf = fft(data)
    xf = fftfreq(N, T)[:N // 2]
    yf = 2.0 / N * np.abs(yf[1:N // 2])
    fft_data = {'x': xf[1:N // 2], 'y': yf}
    return fft_data


def fourier_windowed_transform(data, f_min, f_max):
    data = np.array(data, dtype=float)  # Converts decimal to float for pythonification
    T = float(f_min / f_max)
    N = data.shape[0]
    w = blackman(N)
    ywf = fft(data * w)
    xf = fftfreq(N, T)[:N // 2]
    fft_window = {'x': xf[1:N // 2], 'y': 2.0 / N * np.abs(ywf[1:N // 2])}
    return fft_window


def HttpTeapotResponse(HttpResponse):
    status_code = HTTPStatus.IM_A_TEAPOT
    return status_code
