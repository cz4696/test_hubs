#!/bin/bash
# Time:2022/8/23 15:24
# User:CAOZHENG
# File:using_log.sh

#source /mnt/cfg/data/config.sh

# 声明所有的日志文件
all_log_type=(log)
dir_pwd=$1
log_type=${all_log_type[*]}
log_dir=/mnt/cfg/data/log
if [ -z "$dir_pwd" ]; then
  dir_path=$(pwd)
elif [[ "${log_type[@]}" =~ "${dir_pwd}" ]]; then
  dir_path=${log_dir}/${dir_pwd}
else
  dir_path=${dir_pwd}
fi

flag=0
for log_file in $(ls $dir_path); do
  process_id=$(fuser $dir_path/$log_file)
  if [ -n "$process_id" ]; then
    echo -e "${dir_path}/$log_file"
    flag=1
  fi
done
if [ ${flag} != 1 ]; then
  echo -e "No logs in use found"
fi
exit 0
