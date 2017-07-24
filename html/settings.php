
<!DOCTYPE html>

<?php
$row = 0;
if (($handle = fopen("settings.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        $num = count($data);
            $mu = "Name: ". $data[0];
            $nu = "Mail: ".$data[1];
            $au = "Age: ". $data[2];
            $md = "Mail: ".$data[3];
            $nd = "Name: ".$data[4];
    }
    fclose($handle);
}
$row = 0;
if (($handle = fopen("config.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        $num = count($data);
            $wi = "Wifi: ". $data[0];
            $ps = "Password: ". $data[1];
            $c1 = "Camera 1: ".$data[2];
            $c2 = "Camera 2: ". $data[3];
    }
    fclose($handle);
}

?>
<html>
	<head>
        <link rel="shortcut icon" href="img/f.jpg" type="image/x-icon">
		<title>FFAK</title>
	</head>
        <link rel="stylesheet" type="text/css" href="ffak.css">
		<meta name="keywords" content="foot, diabetic, checker">
		<meta name="description" content="FFAK web page.">

	<body>
		<h1>Foot for a king</h1>
		<h2>Device</h2>
		<h3>v. Almost High fidelity</h3>	
		<br>
		<br>
        <div class="form">
                <form name = "docForm" method="post">
                   <div>
                      <h2>Patient Details</h2>
                      <br>
                      <input type="text" placeholder="<?php echo $mu?>" name= "mailU" id = "mailU">
                      <br>
                      <input type="text" placeholder="<?php echo $nu?>" name = "nameU" id = "nameU">
                      <br>
                      <input type="text" placeholder="<?php echo $au?>" name= "ageU" id = "ageU">
                      <br>
                      <h2>Doctor Details</h2>
                      <input type="text" placeholder="<?php echo $nd?>" name = "nameD"  id = "nameD">
                      <br>
                      <input type="text" placeholder="<?php echo $md?>" name= "mailD" id = "mailD">
                      <br>

                        <input type='submit' value='Save Info' name="submit1"/>
                    </div>
                </form>
          </div>
        </div>
		<br>
        <div class="form">
                <form name = "configForm" method="post">
                   <div>
                      <h2>Device Config</h2>
                      <br>
                      <input type="text" placeholder="<?php echo $wi?>" name= "wifi" id = "wifi">
                      <br>
                      <input type="text" placeholder="<?php echo $ps?>" name= "password" id = "password">
                      <br>
                      <input type="text" placeholder="<?php echo $c1?>" name = "cam1" id = "cam1">
                      <br>
                      <input type="text" placeholder="<?php echo $c2?>" name= "cam2" id = "cam2">
                      <br>
                        <input type='submit' value='Save Config' name="submit2"/>
                    </div>
                </form>
          </div>
        </div>

        <?php
            if (isset($_POST['submit1']))
            {
                $userName = $_POST['nameU'];
                $userAge = $_POST['ageU'];
                $userMail = $_POST['mailU'];
                $docName = $_POST['nameD'];
                $docMail = $_POST['mailD'];

                $fd = fopen ("settings.csv", "w");
                fputs($fd,$userMail);
                fputs($fd,",");
                fputs($fd,$userName);
                fputs($fd,",");
                fputs($fd,$userAge);
                fputs($fd,",");
                fputs($fd,$docMail);
                fputs($fd,",");
                fputs($fd,$docName);
                fputs($fd,"\n");
                fclose($fd);
                header("Refresh:0");
            }
        ?>

        <?php
            if (isset($_POST['submit2']))
            {
                $wifi = $_POST['wifi'];
                $password = $_POST['password'];
                $cam1 = $_POST['cam1'];
                $cam2 = $_POST['cam2'];

                $fd = fopen ("config.csv", "w");
                fputs($fd,$wifi);
                fputs($fd,",");
                fputs($fd,$password);
                fputs($fd,",");
                fputs($fd,$cam1);
                fputs($fd,",");
                fputs($fd,$cam2);
                fputs($fd,"\n");
                fclose($fd);
                header("Refresh:0");
            }
        ?>
		<br>
		<br>
        <form action="/menu.php">
                 <input type="submit" value="HOME">
        </form>
	</body>
</html>
