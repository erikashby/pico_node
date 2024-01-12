# This outlines the possiple actions supported on a PICO device
# Action Format

http://(ip address):5000/action/type?(action API) see documentation

Example: http://ipaddress):5000/action/ledstrip_fire?on  (Turns the ledstrip_fire ON)

Full Example

## Action "ledstrip_fire"
# Supported actions
   - ?on  - This will turn on the ledstrip_fire and it will contiune to remain on.
   - ?off - This will turn the ledstrip_fire off and it will remain off
