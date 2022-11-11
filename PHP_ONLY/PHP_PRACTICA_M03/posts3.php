<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<script type="text/javascript" src="dist/purify.min.js"></script>
<!-- <script type="text/javascript" src="posts3.js"> -->
<script>
let clean = DOMPurify.sanitize('<b>hello there</b>');
// const cadena = '<strong>Texto en javascript</strong>';
// const div = document.querySelector('#comentario');
// div.innerText = cadena;
</script>

</head>

<body>
<?php
if ($_SERVER['REQUEST_METHOD'] == 'GET'){
?>
<p>Nuevo Post</p>
<form action='posts3.php' method='post'>
    <textarea name="textarea" rows="10" cols="50"> Escribe algo aqui </textarea>
    <input type ='submit' value='enviar'>
</form>
 

<?php
}else
echo ($_POST["textarea"]) ?? "";
?>
</body>
</html>