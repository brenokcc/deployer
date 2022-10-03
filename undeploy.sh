set -axe
URL=$1
APP_NAME=$(echo $URL | sed 's|.*/||' | sed 's|.git||')
docker stop $APP_NAME
rm /etc/nginx/conf.d/$APP_NAME.conf
nginx -s reload
