/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -files mapper.py,reducer.py \
    -input /user/alice_data/text_split/* \
    -output /user/alice_data/text_reduce \
    -mapper 'python mapper.py' \
    -reducer 'python reducer.py' \
