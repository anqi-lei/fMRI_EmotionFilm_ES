from psychopy import visual, core, event, microphone

# Setup window
win = visual.Window(fullscr=True, color='grey', units='norm')

# Instruction text style
def show_text(text):
    msg = visual.TextStim(win, text=text, color='black', height=0.06, wrapWidth=1.6)
    msg.draw()
    win.flip()

# Countdown (3,2,1)
def countdown():
    for i in ['3', '2', '1']:
        show_text(i)
        core.wait(1)


# Main routine
show_text("You will verbally recall the events that happened in the movies you watched in the scanner.\n\nYour voice will be automatically recorded.\n\nPress 'Return' to start recalling the first movie.")
event.waitKeys(keyList=['return'])

#countdown()
# 1 Recording screen
show_text("*** Recording in Progress ***\n\nPress 'Return' when you finish.")

# Wait until user presses return
event.waitKeys(keyList=['return'])
win.flip()

#2
show_text("Now please recall the events in the second movie.\n\nPress 'Return' to start.")
event.waitKeys(keyList=['return'])
win.flip()

#countdown()
# 2 Recording screen
show_text("*** Recording in Progress ***\n\nPress 'Return' when you finish.")

# Wait until user presses return
event.waitKeys(keyList=['return'])
win.flip()

show_text("Thank you! The recall session is complete.")
core.wait(1)

win.close()
core.quit()
