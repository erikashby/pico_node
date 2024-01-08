#main module
import node as node, machine, uasyncio as asyncio
#This module will run automatically when the pico starts up

#Define the possible actions that are supported by the pico

#

try:
    node.connect()
except KeyboardInterrupt:
    machine.reset()

#create a fire
ledstrip_fire = __import__('/actions/ledstrip_fire.py', globals(), locals(), ['main'], 0)
ledstrip_fire.main()

#asyncio.create_task(ledstrip_fire.main())

print("done")

while True:
    asyncio.sleep(1)
    print("waiting")


