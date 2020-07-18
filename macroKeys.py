import serial
import pyautogui
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

times = 50
aState = False
sState = False
dState = False
fState = False
qState = False
wState = False
eState = False
rState = False


arduino = serial.Serial('COM5', 9600, timeout=.1)

while times>0:
  data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
  if data:
    var = str(data)[2:].replace("'","").split("|")
    a = var[0]
    s = var[1]
    d = var[2]
    f = var[3]
    q = var[4]
    w = var[5]
    e = var[6]
    r = var[7]
    if ( a =='1' and aState == False):
      aState = True
      pyautogui.keyDown("alt")
      pyautogui.press("tab")
      pyautogui.keyUp("alt")
      print("aState: " + str(aState))
    if ( a != '1' and aState == True):
      aState = False
      print("aState: " + str(aState))
    if ( s =='1' and sState == False):
      sState = True
      pyautogui.keyDown("shift")
      pyautogui.keyDown("ctrl")
      pyautogui.press("m")
      pyautogui.keyUp("shift")
      pyautogui.keyUp("ctrl")
      print("sState: " + str(sState))
    if ( s != '1' and sState == True):
      sState = False
      print("sState: " + str(sState))


    #times = times - 1


  def main():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "spotify.exe":
            print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
            volume.SetMasterVolume(0.6, None)