<?php

session_start();

if(isset($_SESSION['user'])){
	header("Location: menu.php");
	die();
}


$email = md5($_POST['user_email']);
$pass = md5($_POST['user_pass']);

$email_def = md5("ffak@ffak");
$pass_def = md5("toetoetoe");

if($email != $email_def || $pass != $pass_def){

	echo "<script>alert(\"Error\");</script>";
	header("Location: index.php");

}else{
	$_SESSION['user'] = $email;
	header("Location: menu.php");
}



?>
