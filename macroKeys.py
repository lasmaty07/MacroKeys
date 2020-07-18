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

def setSpotifyVol(vol):
  sessions = AudioUtilities.GetAllSessions()
  for session in sessions:
      volume = session._ctl.QueryInterface(ISimpleAudioVolume)
      if session.Process and session.Process.name() == "Spotify.exe":
          volume.SetMasterVolume(vol, None)

def muteTeams():
  sessions = AudioUtilities.GetAllSessions()
  for session in sessions:
      volume = session._ctl.QueryInterface(ISimpleAudioVolume)
      if session.Process and session.Process.name() == "Spotify.exe":
          b = volume.GetMute()
          volume.SetMute(not b,None)


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
    if ( q =='1' and qState == False):
      qState = True
      setSpotifyVol(1.0)
      print("qState: " + str(qState))
    if ( q != '1' and qState == True):
      qState = False
      print("qState: " + str(qState))
    if ( w =='1' and wState == False):
      wState = True
      setSpotifyVol(0.5)
      print("wState: " + str(wState))
    if ( w != '1' and wState == True):
      wState = False
      print("wState: " + str(wState))

    if ( r =='1' and rState == False):
      rState = True
      muteTeams()
      print("rState: " + str(rState))
    if ( r != '1' and rState == True):
      rState = False
      print("rState: " + str(rState))


    #times = times - 1
