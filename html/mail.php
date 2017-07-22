<?php
    shell_exec("sudo python /var/www/html/mail.py");
?>


<!DOCTYPE html>

<html>
	<head>
		<title>FFAK</title>
	</head>
        <link rel="stylesheet" type="text/css" href="ffak.css">
		<meta name="keywords" content="foot, diabetic, checker">
		<meta name="description" content="FFAK web page.">

	<body>
		<h1>Foot for a king</h1>
		<h2>Device</h2>
		<h3>v.0.0.0.0.2</h3>	
		<br>
		<br>
		<br>
		<table>
  			<tr>
				<h2>Mail sent</h2>
  			</tr>
		</table>
		<br>
		<br>
        <form action="/menu.php">
                 <input type="submit" value="HOME">
        </form>
	</body>
</html>
