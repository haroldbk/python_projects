from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

app = QCoreApplication([])
r = QAudioRecorder()
print('Inputs: ', r.audioInputs())
print('Codecs: ', r.supportedAudioCodecs())
print('Sample rates: ' , r.supportedAudioSampleRates())
print('containers: ', r.supportedContainers() )