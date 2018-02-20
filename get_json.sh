#!/bin/sh

# s: 検索を始めるURL番号
# m: 定数（m*並列数10）
# n: 定数（一つのpickleファイルが担当するURLの数）
readonly s=1000000
readonly m=100000
readonly n=10000

for i in `seq 0 9`
do
  python get_json.py `expr $s + $m \* $i + 0 \* $n` `expr $s + $m \* $i + 1 \* $n` & \
  python get_json.py `expr $s + $m \* $i + 1 \* $n` `expr $s + $m \* $i + 2 \* $n` & \
  python get_json.py `expr $s + $m \* $i + 2 \* $n` `expr $s + $m \* $i + 3 \* $n` & \
  python get_json.py `expr $s + $m \* $i + 3 \* $n` `expr $s + $m \* $i + 4 \* $n` & \
  python get_json.py `expr $s + $m \* $i + 4 \* $n` `expr $s + $m \* $i + 5 \* $n` & \
  python get_json.py `expr $s + $m \* $i + 5 \* $n` `expr $s + $m \* $i + 6 \* $n` & \
  python get_json.py `expr $s + $m \* $i + 6 \* $n` `expr $s + $m \* $i + 7 \* $n` & \
  python get_json.py `expr $s + $m \* $i + 7 \* $n` `expr $s + $m \* $i + 8 \* $n` & \
  python get_json.py `expr $s + $m \* $i + 8 \* $n` `expr $s + $m \* $i + 9 \* $n` & \
  python get_json.py `expr $s + $m \* $i + 9 \* $n` `expr $s + $m \* $i + 10 \* $n`
  wait
  echo done!
done
wait
echo done!!
