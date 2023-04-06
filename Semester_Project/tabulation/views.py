import datetime
import time

import numpy as np
from django.db import connection
from django.shortcuts import render


def index(request):
    return sine_wave(request)


def sine_wave(request):
    if "start_time" in request.GET:
        start_time = request.GET['start_time']
        start_time = datetime.datetime.strptime(start_time, '%H:%M')

        start_time = start_time.replace(year=datetime.datetime.now().year, month=datetime.datetime.now().month,
                                        day=datetime.datetime.now().day)
        start_time = time.mktime(start_time.timetuple())
    else:
        start_time = time.time()

    if 'records' in request.GET:
        records = request.GET['records']
    else:
        records = 5000
    data = Get_SineData(start_time, records)
    if data == [] or data == ():
        template = 'error.html'
        return render(request, template)
    data = np.array(data, dtype=float)
    FFT = fft_sine(data)
    render_data = []
    for i in range(len(data)):
        render_data.append({'label': i, 'value': data[i], "fft": FFT[i]})

    gets = {"fft_hide": request.GET.get('fft_hide')}

    start_time = datetime.datetime.fromtimestamp(start_time).strftime('%H:%M')

    if request.user.is_authenticated:
        profile_picture = request.user.profile.profile_picture
    else:
        profile_picture = "profile_pictures/user_placedholder.svg"

    context = {
        "data": render_data,
        "gets": gets,
        'start_time': start_time,
        'records': records,
        'profile_picture': profile_picture
    }
    page = 'tabulation/sinewave.html'
    return render(request, page, context)


def heart_beat(request):
    if "start_time" in request.GET:
        start_time = request.GET['start_time']
        start_time = datetime.datetime.strptime(start_time, '%H:%M')

        start_time = start_time.replace(year=datetime.datetime.now().year, month=datetime.datetime.now().month,
                                        day=datetime.datetime.now().day)
        start_time = time.mktime(start_time.timetuple())
    else:
        start_time = time.time()

    if 'records' in request.GET:
        records = request.GET['records']
    else:
        records = 5000
    data = Get_HeartBeat(start_time, records)
    if data == [] or data == ():
        template = 'error.html'
        return render(request, template)
    data = np.array(data)
    data[:, 1] = np.array(data[:, 1], dtype=float)
    FFT = fft_sine(data[:, 1])
    render_data = []
    for i in range(len(data)):
        render_data.append({'time_stamp': data[i, 0], 'value': data[i, 1], "fft": FFT[i]})

    gets = {"fft_hide": request.GET.get('fft_hide')}

    start_time = datetime.datetime.fromtimestamp(start_time).strftime('%H:%M')

    if request.user.is_authenticated:
        profile_picture = request.user.profile.profile_picture
    else:
        profile_picture = "profile_pictures/user_placedholder.svg"

    context = {
        "data": render_data,
        "gets": gets,
        'start_time': start_time,
        'records': records,
        'profile_picture': profile_picture
    }
    page = 'tabulation/heartbeat.html'
    return render(request, page, context)


def fft_sine(data):
    data = np.fft.fft(data)
    return data


def Get_SineData(time_stamps, records):
    cur = connection.cursor()
    command = "SELECT data_val from dashboard_sinedata where label between  FROM_UNIXTIME({time})-interval 1 minute and FROM_UNIXTIME({time}) limit {records}".format(
        time=time_stamps, records=records)
    cur.execute(command)
    return cur.fetchall()


def Get_HeartBeat(time_stamps, records):
    cur = connection.cursor()
    command = "SELECT time_stamp,value from dashboard_heartbeatdata where time_stamp between  FROM_UNIXTIME({time})-interval 1 minute and FROM_UNIXTIME({time}) limit {records}".format(
        time=time_stamps, records=records)
    cur.execute(command)
    return cur.fetchall()
