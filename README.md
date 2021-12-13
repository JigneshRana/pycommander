# pycommander
executes monitoring command on linux/ubuntu

#sample 
1. Apache requests monitoring
python3 sample.py -x2=10
python3 sample.py -x3=10
python3 sample.py -x4=10
python3 sample.py -x5=10

# Apache Time consuming request count(taking more than 100s) from last 10
python3 commander.py -timeC=10

2. Critical Service running or not?
# apache service 0 or 1 
service apache2 status | grep Active: | grep running | wc -l

# 1 = running 0 = not running
service ds_agent status | grep Active: | grep running | wc -1

# 1 = running 0 = not running
service td-agent status | grep Active: | grep running | wc -1

3. Number of service process running
# count php processes
ps -auxw | grep "\.php " | grep -v grep  | wc -l

# count shell script processes
ps -auxw | grep "\.sh" | grep -v grep | wc -l

# apache status 

# Total accesses: [eg:123817744]
pachectl status | grep 'Total accesses:' | awk -F" " '{print $3}'

# Total Traffic: in gb [eg: 765.4 GB]
apachectl status | grep 'Total Traffic:' | awk -F" " '{print $7,$8}'

# [N1] requests currently being processed, [N2] idle workers
apachectl status | grep 'requests currently being processed' | awk -F" " '{print $1,$6}'

# [N1] requests/sec - [N2] kB/second - [N3] kB/request - [N4] ms/request
apachectl status | grep 'requests/sec' | awk -F" " '{print $1,$4,$7,$10}'


# last 10 top Ips in list
grep "24/Nov/2021:06:27" /home/logdrive/apache2/access.log | awk -F" " '{if($2!="-") print $2}' | sed 's/"GET\|"POST\|,//g' | sort -n | uniq -c | sort -nr | head -10 

# last 10 top Ips in json
grep "24/Nov/2021:06:27" /home/logdrive/apache2/access.log | awk -F" " '{if($2!="-") print $2}' | sed 's/"GET\|"POST\|,//g' | sort -n | uniq -c | sort -nr | head -10 | awk -F" " '{a= "\""$2"\":\""$1"\","a }END { print "{"substr (a,1,length(a)-1)"}" }'

# last [N] minutes top 10 Ips
python3 commander.py -ip=10