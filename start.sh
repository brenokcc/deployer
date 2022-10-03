sh -c 'echo $$ > server.pid; exec ./server.py'&
sleep 3
cat server.pid