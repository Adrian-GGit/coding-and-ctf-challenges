
<?php   
$file = $_GET['page'];
   if(isset($file))
   {
       include("$file");
   }
   else
   {
       include("teamshare.php");
   }
?>

