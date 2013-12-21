#!/bin/bash
if [ -z "$rsstoevernotedb" ]; then
	export rsstoevernotedb=rsstoevernote/rsstoevernote.db
fi

if [ -f "$rsstoevernotedb" ]; then
	echo "[+] Deleting old database"
	rm "$rsstoevernotedb"
fi
echo "[+] Create $rsstoevernotedb database"
sqlite3 ${rsstoevernotedb} < sql/rsstoevernoteDB.sql
