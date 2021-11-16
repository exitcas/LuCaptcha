<?php
session_start();
if (isset($_POST["cachelol"])) {
  $jsonlol = json_decode(file_get_contents("cache/".$_SESSION["cachename"].".json"), true);
  if ($jsonlol["text"]==$_POST["cachelol"]) {
    echo "Yes";
  } else {
    echo "No";
  }
} else {
  $_SESSION["cachename"] = strval(rand(10,9999999999));
  file_put_contents("cache/".$_SESSION["cachename"].".json", file_get_contents("[SERVER DOMAIN (AND PORT?)]/api"));
  $jsonlol = json_decode(file_get_contents("cache/".$_SESSION["cachename"].".json"), true);
  echo '<style>@import url("https://cdn.jsdelivr.net/npm/fork-awesome@1.1.7/css/fork-awesome.min.css");</style><img src="'.$jsonlol["url"].'" alt="'.$jsonlol["url"].'"><br><div style="display:flex"><form method="POST"><input type="text" name="cachelol" placeholder="Result"></form><a href="/"><button><i class="fa fa-refresh"></i></button></a></div>';
}
?>
