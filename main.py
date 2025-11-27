def on_button_pressed_a():
    global teller
    teller = input.running_time()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(input.running_time() - teller)
    basic.show_number(touchcount)
input.on_button_pressed(Button.B, on_button_pressed_b)

touchcount = 0
teller = 0
teller = 0
touchcount = 0

def on_forever():
    global touchcount
    if pins.digital_read_pin(DigitalPin.P8) == 1:
        basic.show_icon(IconNames.NO)
        touchcount += 1
    else:
        basic.show_icon(IconNames.YES)
basic.forever(on_forever)

def on_forever2():
    if touchcount == 3:
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever2)
