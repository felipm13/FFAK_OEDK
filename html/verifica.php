<?php

        session_start();

        if(!isset($_SESSION['user'])){
            die(header("Location: index.php"));
        }


?>
