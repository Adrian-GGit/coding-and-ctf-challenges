<?php
    require_once "../db.php";
    
    // Initialize the session
    session_start();

    // Check if the user is logged in, otherwise redirect to login page
    if (!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true) {
        header("location: /login.php");
        exit;
    }
    // Endpoint for adding and removing admins

    // Check if user has the staff role
    $username = $_SESSION["username"];
    $greetings = $result = "";
    
    $sql_query = "SELECT username FROM greetings_users WHERE username = ? AND staff = 0x1;";
    if ($sql_statement = mysqli_prepare($database_connection, $sql_query)) {
        mysqli_stmt_bind_param($sql_statement, "s", $username);
        mysqli_stmt_execute($sql_statement);
        $result = "";
        mysqli_stmt_bind_result($sql_statement, $result);
        mysqli_stmt_fetch($sql_statement);
        if ($result === '') {
            $message = "Only staff users can manage admins.";
            header("location: /login.php");
        }
        mysqli_stmt_close($sql_statement);
    } else {
        $message = "Not logged in";
        header("location: /login.php");
        exit;
    }
    
    $target_username = "";
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        if (empty(trim($_POST["mode"]))) {
            $message = "Please enter mode.";
        } else {
            // Check if username is empty
            if (empty(trim($_POST["target_username"]))) {
                $username_err = "Please enter username.";
                exit;
            } else {
                $target_username = trim($_POST["target_username"]);
            }
            $method = trim($_POST["mode"]);
            if ($method === "add"){
                $sql_query = "UPDATE greetings_users SET staff = 0x1 WHERE username = ?;";
                // Change the role of the specified user to staff
                if ($sql_statement = mysqli_prepare($database_connection, $sql_query)) {
                    mysqli_stmt_execute($sql_statement, array($target_username));
                    $message = "User should have been updated";
                } else {
                    $message = "Error updating user";
                }
            }
            elseif ($method === "delete") {
                $sql_query = "UPDATE greetings_users SET staff = 0x0 WHERE username = ?;";
                // Change the role of the specified user to staff
                if ($sql_statement = mysqli_prepare($database_connection, $sql_query)) {
                    mysqli_stmt_execute($sql_statement, array($target_username));
                    $message = "User should have been updated";
                } else {
                    $message = "Error updating user";
                }
            }
            else {
                exit;
            }
        }
    }
    mysqli_close($database_connection); 
?>

<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="/favicon.ico">

    <title><?php echo $SITE_NAME ?>- Manage Admins</title>

    <!-- Bootstrap core CSS -->
    <link href="/css/bootstrap.min.css" rel="stylesheet">

    <link href="/css/custom.css" rel="stylesheet">

</head>

<body>
    <div class="jumbotron">
        <div class="container custom-container">
            <h1>Manage Admins</h1>
        </div>
    </div>
    <div class="container">
        <main role="main">
            <div class="row">
                <p>Please choose whether you want to add an admin or delete an admin and provide the username of the account.</p>
            </div>

            <h2> Add admin </h2>
            <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
                <div class="form-group row">
                    <div class="col-xs-6">
                        <label>Username</label>
                        <input type="text" name="target_username" value="">
                    </div>
                </div>
                <div class="form-group row">
                    <div class="col-xs-6">
                        <input type="hidden" name="mode" value="add">
                    </div>
                </div>
                <div class="form-group row">
                    <div class="col-xs-6">
                        <input type="submit" class="btn btn-primary" value="Send">
                    </div>
                </div>
            </form>
            <h2>Delete admin</h2>
            <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
                <div class="form-group row">
                    <div class="col-xs-6">
                        <label>Username</label>
                        <input type="text" name="target_username" value="">
                    </div>
                </div>
                <div class="form-group row">
                    <div class="col-xs-6">
                        <input type="hidden" name="mode" value="add">
                    </div>
                </div>
                <div class="form-group row">
                    <div class="col-xs-6">
                        <input type="submit" class="btn btn-primary" value="Send">
                    </div>
                </div>
            </form>
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