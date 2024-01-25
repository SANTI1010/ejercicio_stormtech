Se crea proyecto solicitado para la segunda etapa de entrevista en Stormtech.

Se creo un entorno virtual en el cual correr django y se hicieron las instalaciones necesarias para crear el entorno.

Luego se creo un proyecto llamado "exercise" y luego una aplicacion llamada "logistics".

Dentro de la aplicacion se crearon los modelos correspondientes con sus atributos y relaciones.

Para poder manejar estos modelos se utilizo el "admid" brindado por Django. Para poder ingresar a este admin se creo un superUsuario con los siguientes datos:
user: admin 
password: superuser123

En la clase admin.py se realizaron las configuraciones para poder realizar el punto 
● crear una acción que permita elegir una planilla y pasar todos los paquetes “en depósito” a “en distribución". 

Dentro del "admin" se pueden agregar y modificar Clientes, Paquetes, Plantillas e Items Plantillas. Dentro de la pantalla Plantillas se ven y se pueden agregar los diferentes items de plantillas.

Para realizar el punto EXTRA se utilizo el decorador @api_view que brinda Django REST Framework.
@api_view se utiliza para convertir una función en una vista de API. Este decorador permite especificar los verbos HTTP permitidos para esa vista y proporciona una forma sencilla de manejar las solicitudes y respuestas de la API. Sin embargo, no ofrece la misma estructura y funcionalidades adicionales que se obtienen al utilizar las clases proporcionadas por Django REST Framework. 
Si bien para este caso en especifico se utilizo @api_view, para realizar una API con todas sus funcionalidad es preferible utilizar las clases ed Django REST Framework.

Cuando se especifica la url 'api/paquetes/<str:tracking>/', esta devuelve en formato json los datos del paquete que tiene asociado el tracking dado (identificador unico) y ademas informa en que planilla se encuentra dicho paquete.
