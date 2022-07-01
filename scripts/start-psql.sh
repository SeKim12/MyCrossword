#!/bin/bash


# remove existing database, recreate role and database
restart() {
  rm -rf /usr/local/var/postgres/
  sleep 1
  initdb /usr/local/var/postgres/
  sleep 2
  pg_ctl -D /usr/local/var/postgres start
  sleep 1
  psql postgres -c "CREATE ROLE crossword WITH LOGIN ENCRYPTED PASSWORD 'crossword'"
  sleep 1
  psql postgres -c "CREATE DATABASE crossword"
  sleep 1
}

if pg_isready ; then
  printf "psql is already running! stop psql first with\n\npg_ctl -D /usr/local/var/postgres stop\n\n and try again!\n"
  exit 1
fi

# drop databases locally and recreate on -r flag
while getopts 'r' flag; do
  echo Initiating clean restart, removing existing database...
  case $flag in
    r) restart
       pg_ctl -D /usr/local/var/postgres stop ;;
    *) echo invalid flag, supply -r for clean restart
       exit 1
  esac
done

pg_ctl -D /usr/local/var/postgres start

