#!/bin/sh

nodi=$1;

#set the BRITE directory
NEW_DIR="/Users/Agnes/Documents/SLU_/ML/cartellaProvaCodici/RLSimFlow_v4.0/brite-patch-master"
#move the seed_file generated to have a different topology every time. Comment it to have the same topology
mv seed_file $NEW_DIR/bin
mkdir -p $NEW_DIR'/risultati'
mkdir -p $NEW_DIR'/file_topo'
mkdir -p $NEW_DIR'/configur'
sed 's/N = 100/N = '${nodi}'/' $NEW_DIR/conf/RTBarabasi.conf > $NEW_DIR/configur/RTBarabasi${nodi}.conf


for nodi in $nodi; do
java -classpath $NEW_DIR/Java Main.Brite $NEW_DIR/configur/RTBarabasi${nodi}.conf $NEW_DIR/risultati/topo_${nodi} $NEW_DIR/bin/seed_file
#2 = node id of source; 3 = node id of destination; 5 = propagation delay; 6 = bandwidth (assigned by AssignBW method)
awk 'x==1 {print $2, $3, $5, $6}{if($1=="Edges:")x=1}' $NEW_DIR/risultati/topo_${nodi}.brite > $NEW_DIR/file_topo/edges_${nodi}.txt

#1 = node id; 2 = x-axis coordinate in the plane; 3 = y-axis coordinate in the plane
myvar2=$((nodi-1))
awk -v myvar=$myvar2 'x==1 {print $1, $2, $3}{if($1=="Nodes:")x=1};($1 == myvar){exit}' $NEW_DIR/risultati/topo_${nodi}.brite > $NEW_DIR/file_topo/coordinate_${nodi}.txt


done


