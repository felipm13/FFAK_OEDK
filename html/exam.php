<?php
    shell_exec("sudo python /var/www/html/cam.py");
?>
<!DOCTYPE html>

<html>
	<head>
		<title>FFAK</title>
	</head>
        <link rel="stylesheet" type="text/css" href="ffak.css">
		<meta name="keywords" content="foot, diabetic, checker">
		<meta name="description" content="FFAK web page.">

	<body  onload="showPage()" style="margin:0;">
		<h1>Foot for a king</h1>
		<h2>Device</h2>
		<h3>v.Medium Fidelity</h3>	
		<br>
		<br>
		<br>
        <?php
        $row = 1;
        if (($handle = fopen("data/lastExam.csv", "r")) !== FALSE) {
          while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
            $num = count($data);
            echo "<p align='center'> <font color=blue  size='6pt'>$data[2]</font> </p>";  
            echo '<img src="'.$data[5].'" weight="720" width="480" <br /> <br />';
          }
          fclose($handle);
        }
        ?>
        <br>
        <form action="/confirm.php">
                 <input type="submit" value="START ANOTHER EXAM">
        </form>
        <br>
        <br>
        <form action="/menu.php">
                 <input type="submit" value="HOME">
        </form>
	</body>
</html>
