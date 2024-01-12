# pico_node
We Geek Together Code for the Pico Nodes

# Folder Structure
## / Root /<br>
  - main.py (This will auto-start when the pico is started)  (note: during development, main.py will be renamed to main_draft.py to prevent it from running by default)<br>
### supporting libaries<br>
   - neopixel.py (used for lighting up lights)
   - node.py (connection functions)

## / Root / actions  << place for action scripts>>
Current Supported Actions <br>
   - ledstrip_fire - Simulates a fire on an LED strip

## / Root / events << place for handling of events >>

## API
This node will support the following APIs<br>
/status <- this will return a status object</br>
/action <- this will perform specific actions (See action API)
