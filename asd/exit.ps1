write-output $args[0]
write-output $args.split('\')[-1]
$query = $args.split('\')[-1]
#$url = 'https://www.google.com/search?q=' + $query
#start $url
Read-Host