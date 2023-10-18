<?php
  // Initialize the session
  session_start();

  // Check if the user is logged in, if not then redirect him to login page
  if (!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true) {
    header("location: /login.php");
    exit;
  }
?>




<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
  <link rel="icon" href="/favicon.ico">

  <title><?php echo $SITE_NAME ?> - Index</title>

  <!-- Bootstrap core CSS -->
  <link href="/css/bootstrap.min.css" rel="stylesheet">

  <link href="/css/custom.css" rel="stylesheet">

</head>

<body>

  <div class="jumbotron">
    <div class="container custom-container">
      <h1>Greetings</h1>
      <p>Welcome to Greetings. This displays all greetings send to your account by fellow staff members.</p>
    </div>
  </div>
  <div class="container">
    <main role="main">
      <div class="container">
        <!-- Example row of columns -->
        
        <div class="row">
          <!-- TODO list the greetings here -->
<?php
  require_once "db.php";

  // Retrieve all greetings for current user
  $username = $_SESSION["username"];
  $sql_query = "SELECT greeting, sender FROM greetings WHERE receiver = ? ;";
  if ($sql_statement = mysqli_prepare($database_connection, $sql_query)) {
    mysqli_stmt_bind_param($sql_statement, "s", $username);
    mysqli_stmt_execute($sql_statement);
    $result = "";
    $sender = "";
    $greeting = "";
    mysqli_stmt_bind_result($sql_statement, $greeting, $sender);
    echo "<table><tr><th>Sender</th><th>Greeting</th></tr>";
    while (mysqli_stmt_fetch($sql_statement)) {
      echo "<tr><td>Sender: $sender</td><td> Message: $greeting </td></tr>";
    }
    echo "</table>";
    mysqli_close($database_connection);
  }
?>
        </div>
        <div class="row">
          <a href="/index.php">Send greetings</a>
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
  <script src="/js/vendor/popper.min.js"></script>
  <script src="/js/bootstrap.min.js"></script>
</body>

</html>
