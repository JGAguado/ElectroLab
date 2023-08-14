Getting started
===============

Assembly options 
----------------
The |Product| can be ordered fully assembled or partially, where all the :term:`SMD`
components are already assembled and you only need to assemble and solder the :term:`THT`
components, such as the pinheads or the potentiometers.

.. Note::
    Assembling all the :term:`THT` components is a tough job since there are more than 500 soldering points. 
    Order this version only if you have some experience with soldering electronics.

For making easier the :term:`THT` components assembly, the |Product| comes with a *Stencil board* that will 
help you with the pinheads positioning for soldering. For an optimal assembly, follow this steps:

    1. Mount the screws on the |Product| as indicated, with the screw head comming from the bottom side (the one with :term:`SMD` components)
    and add a nut on the top side of the board (the one with the QR code).

    2. Start with the pinheads. Place **all** the pinheads on the |Product| top side.     
    Make sure you introduce the short side of the pin on the :term:`PCB`.

    3. Once you have mounted all the pins, place gently the *Stencil board* over it. Be patient, some pins (like the individual pin from the signal generator
    or the Gas sensor) may become troubly rebels. Once they are all in place, screw the other 4 nuts to the screws to secure the two boards together.
    
    4. With the pinheads correctly secured, proceed to the soldering of each individual pin on the **ElectroLab's bottom side**. 
    Pay special attention to those solderings close to :term:`SMD` components for avoiding any damage.
    
    5. After soldering all the pinheads, the screws can be removed and the boards separated.
    
    6. Continue with each individual :term:`THT` component, starting from the smaller like the switches and sensors.
    In this case is highly recomended to:
        1. Place the component on top side of the board
        2. If it has long pins that can bend (like the :term:`LDR` sensor), bend the pins to keep it in place.
        3. If not, press it to hold it in position while soldering.
        4. Start by soldering just one of the pins. 
        5. Check if the sensor is still in the correct position and correct it if not.
        6. Solder the rest of the pins and cut the excess length of them.
  

How it works?
-------------
On the |Product|, each component is internally powered and it's :term:`I/O` are already routed to an accessible pinhead. 
This makes it very easy the quick prototyping of electronic circuits since you just need to interconnect them with female-female wires.

While working with the |Product|, make sure you follow this steps:

- ✅ Analyze and understand the schematic you want to assembly with the |Product|


- ✅ Check if you will be using polarized components (like the polarized capacitors or the microphone) for paying extra attention.

- ✅ Before plugging or unplugging any jumper wires, make sure the board is turned off:
    - If you are using the USB power, the switch has to be in position *AUX* and the USB cable disconnected.
    - In case you are powering it from the Auxiliar interface, the switch has to be in position *USB* and nothing is connected to the Auxiliar Interface connector.


- ✅ Assembly the circuit following a known order, it will save you time in case you get lost.

- ✅ Check that there are not any wire connecting 5V to :term:`GND`.

- ✅ Connect the USB cable or the Auxiliar Interface in order to power the board.

- ✅ Toggle the switch and check that the power led turns on.

- ✅ Play with your recently assembled circuit and experiment with safety!

.. Caution::
    If the Power LED indicator doesn't turn on, power off the board and check the circuit: you might have 
    a shortcircuit somewhere!