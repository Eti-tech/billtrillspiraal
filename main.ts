input.onButtonPressed(Button.A, function () {
    teller = input.runningTime()
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(input.runningTime() - teller)
    basic.showNumber(touchcount)
})
let touchcount = 0
let teller = 0
teller = 0
touchcount = 0
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P8) == 1) {
        basic.showIcon(IconNames.No)
        touchcount += 1
    } else {
        basic.showIcon(IconNames.Yes)
    }
})
basic.forever(function () {
    if (touchcount == 3) {
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    }
})
