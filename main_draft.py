#main
#The master controller for all actions on this pico node.

#Base imports
import node, network, time, json, ledstrip_fire
import uasyncio as asyncio

# Debug mode
debug_mode = True

#Global variables

#Define the supported actions, along with default settings
#Todo: Later this will be converted to a json object
#
# Current schema for supported actions.  (name,on/off,repeat)
# example, ["ledstrip_fire",True,True] = ledstrip_fire action is "on" by default, and repeats with each loop
# supported_actions = [["ledstrip_fire",True,True]]

get_actions = open("supported_actions.json")
actions = json.load(get_actions)
get_actions.close()

get_tasks = open("tasks.json")
tasks = json.load(get_tasks)
get_tasks.close()

get_config = open("config.json")
config = json.load(get_config)
get_config.close()

# Connect to the network
ssid = 'AshXhome_New'
password = 'Andrew00'
wlan = network.WLAN(network.STA_IF)
myip = "10.0.0.xxx or 192.168.x.xxx"

def connect_to_network():
    global myip
    wlan.active(True)
    wlan.config(pm = 0xa11140)  # Disable power-save mode
    wlan.connect(ssid, password)

    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        if debug_mode:
            print('waiting for connection...')
        time.sleep(1)

    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        if debug_mode:
            print('connected')
        status = wlan.ifconfig()
        myip = str(status[0])
        if debug_mode:
            print('ip = ' + status[0])

#Todo - This section needs to be updated to respond to request from server
#Todo - Determine how to pass information from this function back to main loop
#       by updating the action config json

async def node_client(reader, writer):
    if debug_mode:
        print("Client connected")
    request_line = await reader.readline()
    if debug_mode:
        print("Request:", request_line)
    # We are not interested in HTTP request headers, skip them
    while await reader.readline() != b"\r\n":
        pass
    request = str(request_line)
    response = check_action(request)

    writer.write(b'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    writer.write(response)

    await writer.drain()
    await writer.wait_closed()
    if debug_mode:
        print("Client disconnected")


def check_action(request):
    response = "Nothing found"
    # find action in the supported actions json
    for action in actions['actions']:
        if debug_mode:
            print(action['api_path'])
        found = request.find(action['api_path'])
        if debug_mode:
            print("api found =" + str(found))
        if found > 0:
            new_task={"name" : action['name'],"source" : action['source'],"module" : action['module']}
            tasks.append(new_task)
            response = "Found Action: \n" + action['name'] + "\n\nAdding task..."
    
    # find status
    found = request.find("status")
    if found > 0:
        response = str(get_status())
        if debug_mode:
            print("\nstatus found =" + str(found) + "\n")

    if debug_mode:
        print(tasks)
    return response

def get_status():
    current_status = {"name":config["name"], "type":config["type"], "version":config["version"], "source ip":myip, "actions":actions["actions"]}
    if debug_mode:
        print(current_status)
    return current_status

async def main():
    if debug_mode:
        print('Connecting to Network...')
    connect_to_network()

    if debug_mode:
        print('Setting up webserver...')
    asyncio.create_task(asyncio.start_server(node_client, "0.0.0.0", 5000))
    ledstrip_fire.initialze()
    while True:
        await asyncio.sleep(0.25)
        ledstrip_fire.main()
        
try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()
