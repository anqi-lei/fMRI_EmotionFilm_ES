from psychopy import core, event, gui, sound
from psychopy.sound import microphone
import os
from psychopy.hardware import keyboard 

# GUI to get participant info
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title='Speech Recording Experiment')
if not dlg.OK:
    core.quit()

# Create folder for saving audio
if not os.path.exists('recordings'):
    os.makedirs('recordings')

# Generate filename
filename = f"{expInfo['participant']}_session{expInfo['session']}.wav"
file_path = os.path.join('recordings', filename)

# Set up microphone
print("Starting voice recording for ESQ...")
mic= microphone.Microphone(audioLatencyMode=1,streamBufferSecs=10)

mic_onset=mic.start(when=0,waitForStart=1)

core.wait(5)
 
mic.stop()

audioClip=mic.getRecording()  

audioClip.save(filename)
print("Press SPACE to start recording...")

# Wait for spacebar
event.waitKeys(keyList=['space'])

# Start recording
print("Recording started...")
mic.start(when=0, waitForStart=True)
core.wait(5)  # record for 5 seconds
mic.stop()
print("Recording stopped.")

# Save audio
audioClip = mic.getRecording()
audioClip.save(file_path)
print(f"Recording saved to: {file_path}")

# End
core.quit()

