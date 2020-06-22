#!/bin/bash
orgRepo=$1
newRepo=$2
corpCode=$3
if [ -z "$orgRepo" ]
 then
 echo "ERR: Origin Repository Name is empty"
 exit 1
fi

if [ -z $newRepo ]
 then
 echo "ERR: New Repository Name is Empty"
 exit 1
fi

if [ -z $corpCode ]
 then
 echo "ERR: Company Code is Empty"
 exit 1
fi

echo "git clone admin@github.com/virnect-corp/$orgRepo"
echo "cd $orgRepo"
echo "git remote set-url origin admin@github.com/virnect-corp/$newRepo"
echo "git push origin master"

python jenkinsRestApiTest.py $corpCode-$newRepo 
