
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
        <form action="/menu.php">
                 <input type="submit" value="HOME">
        </form>

		<br>
        <?php
        $row = 1;
        if (($handle = fopen("data/historyExam.csv", "r")) !== FALSE) {
          echo "<table align='center'>";
          while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
            $num = count($data);
            echo "<tr>";
            echo "<td><p align='center'> <font color=blue  size='5pt'>$data[2]</font> </p>";
            echo "<p align='center'> <font color=blue  size='4pt'>$data[4]</font> </p>";
            echo '<img src="'.$data[5].'" weight="480" width="320" <br /> <br /> </td>';
            $data = fgetcsv($handle, 1000, ",");
            echo "<td><p align='center'> <font color=blue  size='5pt'>$data[2]</font> </p>";
            echo "<p align='center'> <font color=blue  size='4pt'>$data[4]</font> </p>";
            echo '<img src="'.$data[5].'" weight="480" width="320" <br /> <br /> </td>';

            echo "</tr>"; 
          }
          echo "</table>";
          fclose($handle);
        }
        ?>

		<br>
	</body>
</html>
