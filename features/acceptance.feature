Feature: Check if web server works

Scenario: Run HTTP requests
  Given we have web server started
  When we do a HTTP request to "http://nginx:8080"
  Then we receive "Hello, world"

