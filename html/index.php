<?php

session_start();
if(isset($_SESSION['user'])){
	header("Location: menu.php");
	die();
}

?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <title>FFAK - Login</title>
    <link href="ffak.css" rel="stylesheet">

  </head>
  <body>

    <h1 align="center">Login</h1>
    <br>

    <div class="row">
      <div class="col-md-4"></div>

      <div class="col-md-4">
	<form action="logar.php" method="POST">

	  <div class="form-group">
	    <div align="center">
	    <label>Mail</label>
	    </div>
	    <input type="email" class="form-control" name="user_email" placeholder="Ex .: ffak@ffak.ffak">
	  </div>

	  <div class="form-group">
	    <div align="center">
	    <label>Password</label>
	    </div>
	    <input type="password" class="form-control" name="user_pass" placeholder="">
	  </div>


	  <br>
      <form action="/settings.php">
        <input type="submit" value="SIGN IN" name="submit">
      </form>
      </div>
    </div>

  </body>
</html>
