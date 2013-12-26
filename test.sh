#/bin/bash
export rsstoevernotedb=rsstoevernote/test-rsstoevernote.db
bash sql/createdb.sh
python -m unittest discover
exitcode=$?
echo $exitcode
rm $rsstoevernotedb
exit $exitcode
