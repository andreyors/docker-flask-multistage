Feature: Check if sound is here

As a pragmatic developer
I want to check the behavior
So that I know that it works


Scenario: Listen to the silence
  Given I have my microphone fully functional
  And I hear no sound
  When I switch it on
  And I recorded the silence
  Then I have nothing hearable in the recording

