<?php
// Initialize the session
session_start();

// Check if the user is logged in, if not then redirect him to login page
if (!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true) {
  header("location: login.php");
  exit;
}

require_once "db.php";
?>


<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
  <link rel="icon" href="favicon.ico">

  <title><?php echo $SITE_NAME ?> - Index</title>

  <!-- Bootstrap core CSS -->
  <link href="css/bootstrap.min.css" rel="stylesheet">

  <link href="css/custom.css" rel="stylesheet">

</head>

<body>

  <div class="jumbotron">
    <div class="container custom-container">
      <h1>Greetings</h1>
      <p>Welcome to Greetings. This website allows you to send digital greeting cards to fellow staff members. Feel free to use it as you see fit, but please keep things professional.</p>
    </div>
  </div>
  <div class="container">
    <main role="main">
      <div class="container">
        <!-- Example row of columns -->
        
        <div class="row">
          <form action="send_greetings.php" method="post">
            <div class="form-group">
              <label for="receiver">Receiver: </label>
              <br>
              <input type="text" name="receiver" id="receiver">
            </div>
            <div class="form-group">
              <label for="greeting">Greeting: </label>
              <br>
              <input type="text" name="greeting" id="greeting">
            </div>

            <br>
            <button type="submit" class="btn btn-primary">Send Greetings</button>
          </form>
        </div>
        <div class="container">
        <!-- Example row of columns -->
        
        <div class="row">
          <a href="/view_greetings.php">View greetings</a>
        </div>
        <div class="row">
          <a href="/logout.php">Log out</a>
        </div>
    </main>

  </div>
  <br><br>

  <footer class="container">
    <p>&copy; <?php echo $SITE_NAME ?> 2023</p>
  </footer>

  <!-- Bootstrap core JavaScript
    ================================================== -->
  <!-- Placed at the end of the document so the pages load faster -->
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
  <script>
    window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')
  </script>
  <script src="js/vendor/popper.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
</body>

</html>
