

import wmi
import time
import requests
import keyboard


print('Enter server name')
name = ''
name = input()

print('Hold the x key to exit')

while True:
    w = wmi.WMI(namespace="root/OpenHardwareMonitor")
    infos = w.Sensor()
    cpuTemp = 0
    gpuTemp = 0
    gpuFan = 0
    cpuFan = 0
    motherFan = 0
    cpuLoad = 0
    gpuLoad = 0
    for sensor in infos:
        if sensor.SensorType == u'Temperature' and sensor.Name == u'CPU Package':
            print('CPU temp')
            print(sensor.Value)
            cpuTemp = sensor.Value
        if sensor.SensorType == u'Temperature' and sensor.Name == u'GPU Core':
            print('GPU temp')
            print(sensor.Value)
            gpuTemp = sensor.Value
        if sensor.SensorType == u'Fan' and sensor.Name == u'GPU Fan':
            print('GPU fan')
            print(sensor.Value)
            gpuFan = sensor.Value
        if sensor.SensorType == u'Fan' and sensor.Name == u'Fan #1':
            print('Mother fan')
            print(sensor.Value)
            motherFan = sensor.Value
        if sensor.SensorType == u'Fan' and sensor.Name == u'Fan #2':
            print('CPU fan')
            print(sensor.Value)
            cpuFan = sensor.Value
        if sensor.SensorType == u'Load' and sensor.Name == u'CPU Total':
            print('CPU Total')
            print(sensor.Value)
            cpuLoad = sensor.Value
        if sensor.SensorType == u'Load' and sensor.Name == u'GPU Core':
            print('GPU Core')
            print(sensor.Value)
            gpuLoad = sensor.Value
    url = 'http://192.168.31.107:8080/rest' #'https://projecttest0.000webhostapp.com/api/'
    response = requests.post(url, data=[('name', name), ('cpuTemp', cpuTemp), ('cpuFan', cpuFan), ('gpuTemp', gpuTemp), ('gpuFan', gpuFan), ('motherFan', motherFan), ('cpuLoad', cpuLoad), ('gpuLoad', gpuLoad)],)
    print(response.text)
    if keyboard.is_pressed('x'):
        break
    time.sleep(3)
