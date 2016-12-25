from collections import defaultdict
from xml.dom import minidom

import matplotlib.pyplot as plt
import numpy as np
from dateutil import parser

KEY_HEART_RATE = "HKQuantityTypeIdentifierHeartRate"
KEY_BP_DIA = "HKQuantityTypeIdentifierBloodPressureDiastolic"
KEY_BP_SYS = "HKQuantityTypeIdentifierBloodPressureSystolic"

d = defaultdict(list)
for item in minidom.parse('data/export.xml').getElementsByTagName('Record'):
    try:
        d[item.attributes['type'].value].append([parser.parse(item.attributes['startDate'].value), item.attributes['value'].value])
    except KeyError:
        print "Element has no value: ", item.attributes['type'].value

hr = np.array(d[KEY_HEART_RATE])
dia = np.array(d[KEY_BP_DIA])
sys = np.array(d[KEY_BP_SYS])

plt.plot(dia[:, 0], [int(h) for h in dia[:, 1]], "g^")
plt.plot(sys[:, 0], [int(h) for h in sys[:, 1]], "bs")
plt.plot(hr[:, 0], [int(h) for h in hr[:, 1]], "r--")
plt.show()
