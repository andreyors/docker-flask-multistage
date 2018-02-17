from aloe import step


@step(r'I have my microphone fully functional')
def check_if_device_is_working(self):
    pass


@step(r'I hear no sound')
def check_if_it_is_quiet_here(self):
    pass


@step(r'I switch it on')
def check_if_device_is_on(self):
    pass


@step(r'I recorded the silence')
def check_if_it_is_recording(self):
    pass


@step(r'I have nothing hearable in the recording')
def check_if_the_voice_detection_reports_silence(self):
    pass
