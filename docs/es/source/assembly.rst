🛠 Montaje 
===========

    .. imagen:: images/assembly/CQN23016K_kits_02.png
        :width: 40%
        :align: left
        :alt: Contenido del kit

la |Product| se puede pedir parcialmente ensamblada, donde todos los componentes :term:`SMD` ya están ensamblados y solo necesitas montar y soldar los componentes :term:`THT`, como los pines y el resto de los componentes en la cara superior.

.. Caution::
    Si nunca antes has soldado ningún componente electrónico, este kit puede resultarte bastante complicado y, por lo tanto, se recomienda encarecidamente hacerlo acompañado por alguien con algo de experiencia.

.. Note::
    Ensamblar todos los componentes :term:`THT` puede llevar algo de tiempo (1-2 horas) ya que hay más de 500 puntos de soldadura.

Herramientas
-----
.. Tip:: 
    Invertir en herramientas de calidad asegurará una experiencia de soldadura electrónica más suave y precisa, y a largo plazo merece la pena.

1. Soldador / Estación de soldadura:
    :Rango de precios: 15€ a 50€ por un soldador, 50€ a 150€ por una estación
    Esencial para unir componentes electrónicos. Un soldador en el rango de 25-60 vatios y 
    con un rango de temperatura de alrededor de 300°C a 400°C debería cubrir la mayoría de las tareas de soldadura electrónica. 
    
    En cuanto a la punta, generalmente se recomienda una punta cónica fina o plana para el trabajo electrónico, ya que proporciona precisión y control.    
    El tamaño de la punta puede variar, pero una punta con un ancho de alrededor de 1 mm suele ser un buen punto de partida para la mayoría de los proyectos. 
    Algunas estaciones de soldadura ofrecen puntas intercambiables, lo que te permite seleccionar la más adecuada para tu tarea.

    .. imagen:: images/assembly/VTSSC40N.png
        :width: 60%
        :align: center
        :alt: VTSSC40N

2. Hilo de soldadura:
    :Rango de precios: 5€ a 15€ (bobina de 100g)
    Material utilizado para crear conexiones eléctricas. 
    Los diámetros comunes para trabajos electrónicos incluyen 0.8 mm (0.031"), 1.0 mm (0.039") y 1.2 mm (0.047"). 
    La soldadura más delgada (por ejemplo, 0.8 mm) es adecuada para trabajos finos y delicados, como la soldadura de la **ElectroLab**, 
    mientras que la soldadura más gruesa (por ejemplo, 1.2 mm) se puede usar para componentes y cables más grandes.

    .. imagen:: images/assembly/solder-wire.png
        :width: 60%
        :align: center

    Hay dos tipos principales de soldadura: con plomo y sin plomo. Cada uno tiene sus propias consideraciones:

    - Soldadura con plomo (por ejemplo, 60/40 o 63/37):

        - La soldadura con plomo contiene un pequeño porcentaje de plomo, que puede proporcionar uniones de soldadura más suaves y un flujo más fácil.
        - Tiene un punto de fusión más bajo (normalmente alrededor de 183°C o 361°F), lo que facilita su manipulación.
        - **Asegúrate de tener ventilación adecuada** o usa un extractor de humos al usar soldadura con plomo para evitar inhalar los humos.
        - **Lávate las manos** a fondo después de manipular soldadura con plomo y componentes.

    - Soldadura sin plomo:

        - La soldadura sin plomo es respetuosa con el medio ambiente y cumple con las regulaciones :term:`RoHS`.
        - Tiene un punto de fusión más alto (normalmente alrededor de 217°C o 422°F) en comparación con la soldadura con plomo, por lo que es posible que debas ajustar la temperatura de tu soldador en consecuencia.
        - La soldadura sin plomo puede requerir técnicas ligeramente diferentes, como mantener la punta del soldador en la unión durante un tiempo ligeramente más largo.
        - Generalmente se considera más segura en términos de impacto en la salud y el medio ambiente, pero puede ser menos indulgente para principiantes debido a su punto de fusión más alto.


3. Alicates de corte:
    :Rango de precios: 5€ a 20€
    Utilizados para recortar los excesos de pines y cables después de la soldadura. 
    Busca filos afilados y puntas de precisión, mangos ergonómicos y materiales resistentes a la corrosión.

    .. imagen:: images/assembly/Pliers.png
        :width: 60%
        :align: center

4. Soporte PCBs:
    :Rango de precios: 10€ a 30€
    Aunque esto es más una elección personal y no una herramienta requerida, un buen soporte de PCBs asegurará tu placa durante la soldadura y te ayudará en el ensamblaje. 
    Elige uno con presión de sujeción ajustable, una superficie que no deje marcas y un mecanismo de sujeción estable.

    .. imagen:: images/assembly/Clamp.png
        :width: 60%
        :align: center


.. admonition:: Y, por cierto...

    Para facilitar el ensamblaje de los componentes :term:`THT`, la |Product| viene con una placa *Stencil* que 
    te ayudará con la posición de los pines para soldar. 

    .. imagen:: images/assembly/Top_stencil.png
        :width: 49%

    .. imagen:: images/assembly/Bottom_stencil.png
        :width: 49%



Pasos
-----

1. Coloca 2 tornillos en la |Product| en diagonal, con la cabeza del tornillo viniendo desde la parte inferior (la que tiene los componentes :term:`SMD`) y agrega una tuerca en la parte superior de la placa (la que tiene el código QR).

    .. imagen:: images/assembly/1.PNG
        :width: 60%
        :align: center


2. Comienza con los pines. Coloca **todos** los pines en la cara superior de la |Product|. Asegúrate de introducir el lado corto de los pines en la :term:`PCB`.

    .. imagen:: images/assembly/2.PNG
        :width: 60%
        :align: center

3. Una vez que hayas colocado todos los pines, coloca suavemente la placa *Stencil* sobre estos. Ten paciencia, algunos (como el del generador de señales o el sensor de gas) pueden volverse rebeldes y difíciles. Una vez que todos estén en su lugar, atornilla otras 2 tuercas a los tornillos para asegurar las dos placas juntas.

    .. imagen:: images/assembly/3.PNG
        :width: 49%

    .. imagen:: images/assembly/4.PNG
        :width: 49%

4. Con los pines correctamente asegurados, procede a soldarlos individualmente en el **reverso de la ElectroLab**. Presta especial atención a esas soldaduras cerca de los componentes :term:`SMD` para evitar cualquier daño.

    .. imagen:: images/assembly/6.gif
        :width: 60%
        :align: center
        
5. Después de soldar todos los pines, quita los tornillos y separa las placas.

    .. imagen:: images/assembly/8.PNG
        :width: 60%
        :align: center
        
6. Continúa con cada componente :term:`THT` individual, comenzando por los más pequeños como los interruptores y sensores. En este caso, se recomienda:

    .. WARNING:: 
        Algunos componentes tienen **polaridad**, lo que significa que deben ensamblarse de una manera específica, presta atención a las marcas debajo del sensor.
        Esos componentes :term:`THT` son el altavoz, el micrófono, el :term:`LED` :term:`RGB` y el display de 7 segmentos.

    1. Coloca el componente en la cara superior de la placa.

        .. imagen:: images/assembly/9.PNG
            :width: 60%
            :align: center

    2. Si tiene patitas largas que puedan doblarse (como el sensor :term:`LDR`), dóblalas para mantener el componente en su lugar. 
    Si no, presiónalo para mantenerlo en posición mientras sueldas (como el altavoz).

    3. Comienza soldando solo uno de las patitas. 
            
        .. imagen:: images/assembly/10.PNG
            :width: 60%
            :align: center

    4. Verifica si el sensor todavía está en la posición correcta y corrígelo si es necesario.
    5. Suelda el resto de las patitas de los componentes y corta la longitud sobrante de estos.
            
        .. imagen:: images/assembly/13.gif
            :width: 60%
            :align: center

    .. Attention:: 
        Por favor, ten cuidado al recortar el metal sobrante de las patas de los componentes.  
        Se recomienda usar gafas de seguridad mientras realizas esta tarea para evitar posibles lesiones oculares.
