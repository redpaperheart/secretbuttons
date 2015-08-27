<--!Launcher website --!>

<!DOCTYPE html>
<head>
<html lang="en">
<meta charset="UTF-8">
<title>PIPO Launcher Monitoring</title>

<link rel="stylesheet" type="text/css" href="style/style.css">
</head>

<body>
<h1>Keeping track of how many PIPO launches have been made. </h1>

<?php
$str = file_get_contents("/home/pi/pipo/data/info.json");
$json = json_decode($str, true);

$numHits = $json["NumberOfHits"];
$LastHit = $json["TimeOfLastHit"];
$startDate = $json["StartDate"];
$recentHit = strtotime($LastHit);
$t = date('m/d/y H:i:s', $recentHit);

$first = strtotime($startDate);
$s = date('m/d/y H:i:s', $first);

$now = date_create();
$n = date_timestamp_get($now);

//Echo "<script> function colorS(){document.getElementById('colorP').style.color='green';}</script>";
Echo "<p id='colorP'>There have been <strong>$numHits</strong>  made total.";
Echo " The last hit took place on <strong>$t</strong>.</p>";

$diffInMinutes = ($n - $first)/60;

$averageHit = floor(($diffInMinutes / $numHits) * 100) / 100;

Echo "<p>Since we started counting at $s, that makes one hit every <strong>$averageHit</strong> minutes or so</p>";

//Echo "<p id='js'>Test text please ignore</p>";

//Echo "<script>document.getElementById('js').innerHTML = $averageHit;</script>";
?>
</script>
</body>
</html>
