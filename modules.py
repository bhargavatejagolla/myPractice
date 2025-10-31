import cowsay
# print(cowsay.trex("I'm a T-Rex!"))
# print(cowsay.dragon("I'm a dragon with fire!"))
# print(cowsay.kitty("Meow!"))
# from cowpy import cow

# # Create a Cow instance
# c = cow.Cowacter()

# # Generate a message
# message = c.milk("Python is awesome!")
# print(message)
# print(cowsay.daemon("I'm a ghost cow!"))
# from decimal import Decimal, ROUND_HALF_UP
# a = input()
# # Round to 2 decimal places
# num = Decimal(a).quantize(Decimal("0.0000000001"), rounding=ROUND_HALF_UP)
# print(num)  # Output: 3.14
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow
# import sys


# def window():
#     app = QApplication(sys.argv)
#     win = QMainWindow()
#     win.setGeometry(2000, 2000, 300, 300)
#     win.setWindowTitle("bhargava TEja")
#     win.show()
#     sys.exit(app.exec_())
#


# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
freq = 44100

# Recording duration
duration = 120

# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
wv.write("recording1.wav", recording, freq, sampwidth=2)



# window()
