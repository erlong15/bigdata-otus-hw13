/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -input /data/word_count/test_tet/ \
    -output /data/word_count/test_text_result \
    -mapper 'python mapper.py' \
    -reducer 'python reducer.py' \
    -file mapper.py \
    -file reducer.py
