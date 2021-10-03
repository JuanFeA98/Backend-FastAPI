# Deploy

**Paso 1.** Ubicar en una carpeta el script y un archivo requirements.txt que contenga la libreria *fastapi*

**Paso 2.** Vamos a https://www.deta.sh/?ref=fastapi y creamos un usuario en deta.

**Paso 3.** Vamos a Window PowerShell y desde allí ejecutamos el siguiente comando:

    iwr https://get.deta.dev/cli.ps1 -useb | iex

**Paso 4.** Verificamos que el cli de deta halla quedado correctemanete instalado y se encuentre dentro de nuestras variables de entorno

    deta --help

**Paso 5.** Nos logeamos desde la cli

    deta login

**Paso 6.** Vamos a la carpeta donde esta contenido nuestro proyecto y ejecutamos:

    deta new

Esto realizara el deploy y nos entregara el respectivo endpoint del proyecto.

**Paso 7.** Si hacemos alguna modificación de nuestro código utilizamos el comando
    
    deta deploy

Esto actualizara los cambios.