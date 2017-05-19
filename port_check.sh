#! /bin/bash
input="./result_closedports.txt"
while IFS= read -r var
do
{	
	nc -v -w2 $var
}

done < "$input"