from psychopy import core, event, gui, sound
from psychopy.sound import microphone
import os
from psychopy.hardware import keyboard 

# GUI to get participant info
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title='Speech Recording Testing')
if not dlg.OK:
    core.quit()

# Create folder for saving audio
if not os.path.exists('recordings'):
    os.makedirs('recordings')

# Generate filename
filename = f"{expInfo['participant']}_session{expInfo['session']}.wav"
file_path = os.path.join('recordings', filename)


print('recording now')
continueRoutine = True
mic= microphone.Microphone()
mic_onset=mic.start()
kb = keyboard.Keyboard()

while continueRoutine:
    keys = kb.getKeys(keyList=['return', 'escape'], waitRelease = False)  # Wait for return key press
    for key in keys:
        if key.name == 'return':
            continueRoutine = False
            mic.stop()
            print('stop')
        elif key.name == 'escape':
            core.quit()


audioClip=mic.getRecording()  
audioClip.save(filename)
# End
core.quit()

