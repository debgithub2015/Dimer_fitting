
for i in 4 
do
  cd System$i/
  bash prepare.sh $i
  bash transform
  cd ..
done


