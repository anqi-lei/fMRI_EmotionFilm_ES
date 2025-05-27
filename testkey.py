from psychopy import visual, event, core

win = visual.Window()
while True:
    keys = event.getKeys()
    if keys:
        print("Key(s) pressed:", keys)
    if 'escape' in keys:
        core.quit()