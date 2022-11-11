<?php
session_start();
if(!$_SESSION['ya_registrado']){
    header('Location: login.php');
}
$from = $_SESSION['usuario'];
$to = $_GET['to'];
$quantity = $_GET['quantity'];
$BD = "Transferencia realizada de $from a $to; cantidad: $quantity";
$fichero = 'transfers.txt';
$actual = file_get_contents($fichero);
file_put_contents($fichero, $VD, FILE_APPEND);

<img src='http://dominiodeguro.local/transfer.php?quantity=1000&to=juan'>
