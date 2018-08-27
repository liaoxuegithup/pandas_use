. 导入MongoDB公共GPG密钥sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
2. 创建/etc/apt/sources.list.d/mongodb3.4-org 名单列表文件echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
3. 重新加载本地包数据库sudo apt-get update
4. 安装MongoDB包 sudo apt-get install -y mongodb-org
5. 我们需要简单配置下,编辑/etc/mongod.conf

ideal@ideal-PowerEdge-R730xd:~$ sudo vim /etc/mongod.conf
mongod.conf 文件如下:

# mongod.conf# for documentation of all options, see:# http://docs.mongodb.org/manual/reference/configuration-options/# Where and how to store data.storage: dbPath: /var/lib/mongodb # mongodb的数据存放目录 journal: enabled: true# engine:# mmapv1:# wiredTiger:# where to write logging data.systemLog: destination: file logAppend: true path: /var/log/mongodb/mongod.log # 日志存放目录# network interfacesnet: port: 27017 # 设置访问端口,默认27017 bindIp: 192.168.255.1 # 绑定ip,默认127.0.0.1#processManagement:#security:#operationProfiling:#replication:#sharding:## Enterprise-Only Options:#auditLog:#snmp:
编辑完之后source 一下

ideal@ideal-PowerEdge-R730xd:~$ source /etc/mongod.conf
现在我们的集群已经安装成功了, 我们来启动下

ideal@ideal-PowerEdge-R730xd:~$ sudo service mongod start
接着我们看看是否可以打开mongodb shell 客户端:

