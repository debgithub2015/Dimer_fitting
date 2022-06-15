
for i in 4 
do
  cd System$i/
  echo $i
  bash bash_submit.sh $i
  cd ..
done


