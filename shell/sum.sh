read n
sum=0
for (( i=1 ; i<=$n ; i++ ))
do
  read a
  let "sum+=$a"

done
printf "Output: %.3f" $(echo $sum/$n | bc -l)


##!/bin/bash
#read n
#
#for ((i=1;i<=$n;i++))
#do
#read input${i}
#done

#SUM=0
#for ((i=1;i<=5;i++))
#do
#SUM=`echo $SUM+$"input"${i}""|bc`
#echo $SUM
#done
#AVG=`echo "scale=3; ${SUM}/5"|bc`
#echo $AVG