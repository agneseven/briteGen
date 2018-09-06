# briteGen
### 1. Prerequisites
* python
* [BRITE](https://www.cs.bu.edu/brite/)

### 2. Before running

1. move javagen.sh and seed file in your BRITE/bin directory

2. in javagen.sh, 
  
  * write in NEW_DIR your BRITE directory, e.g. NEW_DIR="~/BRITE "
  
  * substitute RTBarabasi.conf with the desired configuration. The following line create a new configuration file with a different number of nodes. 

> sed 's/N = 100/N = '${nodi}'/' $NEW_DIR/conf/RTBarabasi.conf > $NEW_DIR/configur/RTBarabasi${nodi}.conf

3. in briteGen.py write in path your BRITE directory, e.g. path="~/BRITE "

### 3. Run 
```
python sim.py <NODE_NUM>
```
where:

**\<NODE_NUM\>** : number of nodes in the topology

> *Example*
> 
> ./test 10 ./coordinates_10_1.txt ./edges_10_1.txt ./bandwidth_10_1.txt ./delay_10_1.txt 1000 5 uniform uniform 3 3 uniform 3 100 0 1 50 0 exponential
