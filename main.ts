input.onButtonPressed(Button.A, function on_button_pressed_a() {
    wuKong.setMotorSpeed(wuKong.MotorList.M1, 50)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    wuKong.stopMotor(wuKong.MotorList.M1)
})
music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Chase), music.PlaybackMode.UntilDone)
