

<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "cars_outlet";

try {
  $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  //echo "Connected successfully";
} catch(PDOException $e) {
  echo "Connection failed: " . $e->getMessage();
  exit();
}
$brand = $_POST['brand'];
$type = $_POST['type'];
$licence = $_POST['licence'];
$stmt = $conn->prepare("INSERT INTO `cars` (`id`, `Brand`, `Type`, `licence`) VALUES (NULL, '$brand', '$type', '$licence');");
$stmt->execute();

header('Location: new.html');