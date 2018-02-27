# bigdata-otus-hw13

* pairs count = 121659
* top 200 pairs 
```
more pairs
```

* log of hadoop work 
```
run.log
```

* hdfs commands
```
hdfs dfs -mkdir /user/alice_data/text_split
hdfs dfs -mkdir /user/alice_data/text_reduce
hdfs dfs -copyFromLocal text_split/alice_a*  /user/alice_data/text_split/
hdfs dfs -copyToLocal /user/alice_data/text_reduce/* ./text_reduce/
```

