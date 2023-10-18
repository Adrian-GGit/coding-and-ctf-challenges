<?php
// Initialize the session
session_start();

// Check if the user is already logged in, if yes then redirect him to welcome page
if (!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true) {
    header("location: login.php");
    exit;
}

// Include config file
require_once "db.php";

// Define variables and initialize with empty values
$greeting = $sender = $receiver = "";
$greeting_err = $sender_err = "";

// Processing form data when form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Check if greeting is empty
    if (empty(trim($_POST["greeting"]))) {
        $greeting_err = "Please provide a greeting.";
    } else {
        $greeting = trim($_POST["greeting"]);
    }

    // Check if receiver is empty
    if (empty(trim($_POST["receiver"]))) {
        $receiver_err = "Please provide a receiver.";
    } else {
        $receiver = trim($_POST["receiver"]);
    }

    // Get sender
    $sender = $_SESSION["username"];

    // Validate credentials
    if (empty($greeting_err) && empty($receiver_err)) {
        // Prepare a select statement
        $sql = "INSERT INTO greetings (greeting, receiver, sender) VALUES (?, ?, ?)";
        if ($stmt = mysqli_prepare($database_connection, $sql)) {
            // Bind variables to the prepared statement as parameters
            mysqli_stmt_bind_param($stmt, "sss", $param_greeting, $param_receiver, $param_sender);

            // Set parameters
            $param_sender = $sender;
            $param_receiver = $receiver;
            $param_greeting = $greeting;

            // Attempt to execute the prepared statement
            if (mysqli_stmt_execute($stmt)) {
                $message = "Worked";
            } else {
                $message = "Oops! Something went wrong. Please try again later.";
            }

            // Close statement
            mysqli_stmt_close($stmt);
        }
    }

    // Close connection
    mysqli_close($database_connection);
}
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
      <h1>Send greeting result</h1>
    </div>
  </div>
  <div class="container">
    <main role="main">
      <div class="container">
        <div class="alert alert-success" role="alert">
            <?php echo $message ?>
        </div>
          
      </div>
      <div class="row">
          <a href="/index.php">Go back</a>
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