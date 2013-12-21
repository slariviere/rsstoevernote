#/bin/bash
export rsstoevernotedb=rsstoevernote/test-rsstoevernote.db
bash sql/createdb.sh
python -m unittest discover
rm $rsstoevernotedb
