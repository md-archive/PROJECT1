<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
</head>
<body>
<?php
if ($_SERVER['REQUEST_METHOD'] == 'GET'){
?>

<p>Nuevo Post</p>
<form action='posts.php' method='post'>
    <textarea name="textarea" rows="10" cols="50"> Escribe algo aqui </textarea>
    <input type ='submit' value='enviar'>
</form>
<?php
}else
echo $_POST["textarea"] ?? "";
?>
</body>
</html>