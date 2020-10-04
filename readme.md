# Preparar ambiente (probado en Windows)
<code>pip install virtualenv</code>

<code>virtualenv venv</code>

* activamos el ambiente virtual

    <code>.\venv\Scripts\activate</code>

* desactivamos el ambiente virtual

    <code>deactivate</code>

* lista de librerias instaladas

    <code>pip freeze</code>


# Instalamos librerias (en el ambiente virtual)
<code>pip install pygame numpy</code>

# Ejecutamos (en el ambiente virtual)
<code>pip game.py</code>

Al presionar una tecla el juego se pone en pausa o se activa nuevamente.
Cuando el juego esta en pausa, podemos hacer click en las celdas para revivir o matar celulas.