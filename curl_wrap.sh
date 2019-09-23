#!/usr/bin/env bash

#d='{"query": {"filtered": {"query": {"match_all": {}}, "filter": {"range": {"timestamp": {"gt": "now-15m"}}}}}}'

response=$(curl --silent http://talend:9200/logstash-*/_search -d '{"query": {"filtered": {"query": {"match_all": {}}, "filter": {"range": {"@timestamp": {"gt": "now-15m"}}}}}}')

echo ${response}
