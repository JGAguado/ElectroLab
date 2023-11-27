💬 :term:`FAQ`
=============================

After connecting everything and turning on the |Product|, I don't see any :term:`LED` on.
    If the board is correctly powered and you cannot see the power :term:`LED` on, disconnect the power immediately: 
    there is a short-circuit in your board, meaning that there is a wire (with very little resistance) connecting the 
    Vcc (3.3V) and the :term:`GND`.

After assembling everything and powering the board, the circuit doesn’t do what I expected, why?
    The more complex the assembled circuit is, the easier to make a mistake. If the circuit has 
    been tested before, the most likely answer is that there is some error at a certain connection. 
    The solution is to check node by node that everything is correctly connected.

I accidentally inverted the polarity of a component that was marked as polarized, what can I do?
    If the component seems damaged from outside or the circuit doesn’t work after fixing it, it 
    is clear that you will need to replace it or send it for repair (check :ref:`support`).

I want to expand the set of sensors to play with other, can I do it?
    Of course! Just make sure are components rated for 3.3V. Remember to connect both :term:`GND` 
    together and in case the sensor needs a power supply connect it to the 3.3V bus-bar.

Can I connect multiple ElectroLab together for making more complex circuits?
    Yes, some of the circuits can become so complex that you might need to do it like this. In 
    this case just connect the 3.3V of one ElectroLab to the 3.3V of the other and the :term:`GND` of one to 
    the :term:`GND` of the other, so both are powered correctly.