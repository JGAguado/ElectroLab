🛠 Assembly 
===========

    .. image:: images/assembly/CQN23016K_kits_02.png
        :width: 40%
        :align: left
        :alt: Kit contain
        
The |Product| can be ordered partially assembled, where all the :term:`SMD`
components are already assembled and you only need to assemble and solder the :term:`THT`
components, such as the pinheads and the rest of the components on the top side.


.. Caution::
    If you have never soldered any electronic component before, this kit may result quite challenging for you and therefore is highly 
    recommended to do it accompanied by someone with some experience.

.. Note::
    Assembling all the :term:`THT` components can take some time (1-2h) since there are more than 500 soldering points.


Tools
-----
.. Tip:: 
    Investing in quality tools will ensure a smoother and more precise soldering and electronics assembly experience, making your projects more efficient and successful in the long run.


1. Soldering Iron/Soldering Station:
    :Price range: $15 to $50 for a soldering iron, $50 to $150 for a station
    Essential for joining electronic components. A soldering iron in the range of 25-60 watts and 
    with a temperature range of around 300°C to 400°C (572°F to 752°F) should cover most electronics soldering tasks. 
    
    Regarding the tip, a fine conical or chisel tip is generally recommended for electronics work, as it provides precision and control.    
    Tip size can vary, but a tip with a width of around 1mm is often a good starting point for most projects. 
    Some soldering stations offer interchangeable tips, allowing you to select the most suitable one for your task. 

    .. image:: images/assembly/VTSSC40N.png
        :width: 60%
        :align: center
        :alt: VTSSC40N

2. Solder Wire:
    :Price range: $5 to $15 (100g spool)
    Material used to create electrical connections. 
    Common diameters for electronics work include 0.8mm (0.031"), 1.0mm (0.039"), and 1.2mm (0.047"). 
    Thinner solder (e.g., 0.8mm) is suitable for fine, delicate work, like the **ElectroLab** soldering, 
    while thicker solder (e.g., 1.2mm) can be used for larger components and wires.

    .. image:: images/assembly/solder-wire.png
        :width: 60%
        :align: center

    There are two main types of solder: leaded and lead-free. Each has its own considerations:

    - Leaded Solder (e.g., 60/40 or 63/37):

        - Leaded solder contains a small percentage of lead, which can provide smoother solder joints and easier flow.
        - It has a lower melting point (typically around 183°C or 361°F), making it easier to work with.
        - **Ensure proper ventilation** or use a fume extractor when using leaded solder to avoid inhaling lead fumes.
        - **Wash your hands** thoroughly after handling leaded solder and components.

    - Lead-Free Solder:

        - Lead-free solder is environmentally friendly and complies with :term:`RoHS` regulations.
        - It has a higher melting point (typically around 217°C or 422°F) compared to leaded solder, so you may need to adjust your soldering iron's temperature settings accordingly.
        - Lead-free solder may require slightly different techniques, such as holding the soldering iron tip on the joint for a slightly longer time.
        - It's generally considered safer in terms of health and environmental impact but can be less forgiving for beginners due to its higher melting point.


3. Cutting Pliers:
    :Price range: $5 to $20
    Used for trimming excess leads and wires after soldering. 
    Look for sharp, precision-ground jaws, ergonomic handles, and corrosion-resistant materials.

    .. image:: images/assembly/Pliers.png
        :width: 60%
        :align: center

4. PCB Clamp:
    :Price range: $10 to $30
    Althoug this is more of a personal choice and not a required tool, a good PCB clamp will secure your board during soldering and help you on the assembly. 
    Choose one with adjustable clamping pressure, a non-marring surface, and a stable base or attachment mechanism.

    .. image:: images/assembly/Clamp.png
        :width: 60%
        :align: center


.. admonition:: And, by the way...

    For making easier the :term:`THT` components assembly, the |Product| comes with a *Stencil board* that will 
    help you with the pinheads positioning for soldering. 

    .. image:: images/assembly/Top_stencil.png
        :width: 49%

    .. image:: images/assembly/Bottom_stencil.png
        :width: 49%



Steps
-----

1. Mount 2 screws on the |Product| diagonally, with the screw head comming from the bottom side (the one with :term:`SMD` components) and add a nut on the top side of the board (the one with the QR code).

    .. image:: images/assembly/1.PNG
        :width: 60%
        :align: center


2. Start with the pinheads. Place **all** the pinheads on the |Product| top side. Make sure you introduce the short side of the pin on the :term:`PCB`.

    .. image:: images/assembly/2.PNG
        :width: 60%
        :align: center

3. Once you have mounted all the pins, place gently the *Stencil board* over it. Be patient, some pins (like the individual pin from the signal generator or the Gas sensor) may become troubly rebels. Once they are all in place, screw the other 2 nuts to the screws to secure the two boards together.

    .. image:: images/assembly/3.PNG
        :width: 49%

    .. image:: images/assembly/4.PNG
        :width: 49%

4. With the pinheads correctly secured, proceed to the soldering of each individual pin on the **ElectroLab's bottom side**. Pay special attention to those solderings close to :term:`SMD` components for avoiding any damage.
    
    .. image:: images/assembly/6.gif
        :width: 60%
        :align: center
        
5. After soldering all the pinheads, the screws can be removed and the boards separated.

    .. image:: images/assembly/8.PNG
        :width: 60%
        :align: center
        
6. Continue with each individual :term:`THT` component, starting from the smaller like the switches and sensors. In this case is highly recomended to:

    .. WARNING:: 
        Some components have **polarity**, which means they have to be assembled on a specific way, pay attention to the marks under the sensor.
        Those :term:`THT` components are the speaker, the microphone, the RGB led and the 7 segments display.

    1. Place the component on top side of the board

        .. image:: images/assembly/9.PNG
            :width: 60%
            :align: center

    2. If it has long pins that can bend (like the :term:`LDR` sensor), bend the pins to keep it in place. 
    If not, press it to hold it in position while soldering (like the speaker).

    3. Start by soldering just one of the pins. 
            
        .. image:: images/assembly/10.PNG
            :width: 60%
            :align: center

    4. Check if the sensor is still in the correct position and correct it if not.
    5. Solder the rest of the pins and cut the excess length of them.
            
        .. image:: images/assembly/13.gif
            :width: 60%
            :align: center

    .. Attention:: 
        Please exercise caution when trimming the excess metal from soldered pins.  
        Wearing safety glasses or goggles while performing this task is strongly recommended to avoid potential eye injury.