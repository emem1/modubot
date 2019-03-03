from pyax12.connection import Connection
from pyax12.instruction_packet import InstructionPacket
import time

#initialise serial port S0
serial_connection = Connection(port="/dev/ttyS0", baudrate=1000000, rpi_gpio=True)

#disable torque for servo with ID 1
serial_connection.send(InstructionPacket(1, 0x03, bytes([0x18, 0x00])))

#initialise position array
position1 = []

#initialise time
init_time = time.time()

try:
    while True:
       print("1")
except KeyboardInterrupt:
    pass
