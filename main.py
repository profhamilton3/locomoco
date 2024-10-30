def on_button_pressed_a():
    wuKong.set_motor_speed(wuKong.MotorList.M1, 50)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    wuKong.stop_motor(wuKong.MotorList.M1)
input.on_button_pressed(Button.B, on_button_pressed_b)

music._play_default_background(music.built_in_playable_melody(Melodies.CHASE),
    music.PlaybackMode.UNTIL_DONE)