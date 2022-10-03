PID=$(cat server.pid)
kill $PID
rm -f server.pid