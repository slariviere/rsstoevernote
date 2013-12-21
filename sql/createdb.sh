#!/bin/bash
echo $rsstoevernotedb
sqlite3 ${rsstoevernotedb} < sql/rsstoevernoteDB.sql
