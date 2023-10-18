<?php

class Account
{
	public function __construct($con)
	{
		$this->con = $con;
	}
	public function login($un,$pw)
	{
		$pw = hash("md5",$pw);
		$query = $this->con->prepare("SELECT * FROM users WHERE username='$un' AND password='$pw'");
		$query->execute();
		if($query->rowCount() >= 1)
		{
			return true;
		}?>
		<h1 style="color:red";>Invalid username or password</h1>
	<?php }
}

?>
