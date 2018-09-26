<?php
  
require __DIR__ . '/vendor/autoload.php';

$log = new Monolog\Logger('name');
$log->pushHandler(new Monolog\Handler\StreamHandler('/tmp/app.log', Monolog\Logger::WARNING));
$log->addWarning('Foo');

echo "Wrote a log entry to /tmp/app.log!";
