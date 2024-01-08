#main module
import node as node, machine, uasyncio as asyncio, ledstrip_fire, utime
#This module will run automatically when the pico starts up

#Define the possible actions that are supported by the pico

#

try:
    node.connect()
except KeyboardInterrupt:
    machine.reset()

#create a fire
#ledstrip_fire_run = __import__('ledstrip_fire.py', globals(), locals(), ['main'], 0)
#ledstrip_fire.main()
async def main():
    asyncio.create_task(ledstrip_fire.main_fire())

    print("done")

    while True:
        asyncio.sleep(1)
        print("waiting")

asyncio.run(main())