# Simple directory traversal tool
This is very simple directory traversal detect tool in python, but also quite effective!!!
If you have any issues or website this tool cannot detect, Please let me know!
Thank you!

## How to run
*python path_traversal_detect.py -u 'http://demosite.com/index.php?file=123' - c 'security=low; PHPSESSID=eolqo4ngnu6dsmtoif31185dk'*

With parameter:
* -u or --url: Full link of path traversal vuln. Ex: Ex: -u 'http://demosite.com/index.php?file=123'
* -c or --cookie: Cookie for authenticated attack. Ex: -c 'security=low; PHPSESSID=eolqo4ngnu6dsmtoif31185dk'

And for help
*python path_traversal_detect.py -h*

