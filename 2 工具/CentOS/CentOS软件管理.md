# Linux系统的应用商店

操作系统安装软件有许多方式
* 下载安装包自行安装
	* win系统使用的exe文件
	* mac系统的dmg文件
* 系统的应用商店内安装

Linux同样支持

# 相关命令
## yum命令
yum：RPM包[^1]软件管理器，用于自动化安装Linux软件，并解决依赖问题
* 语法：`yum [-y] [install | remove |search] 软件名称
* 选项：-y，自动确认，无需手动确认安装或卸载过程
* install：安装
* remove：卸载
* search：搜索

安装包由软件仓库（Repositroy）提供，有官方仓库和第三方仓库
Yum通过`/etc/yum.repos.d/`目录下的`repo`文件获取仓库地址（网络地址或本地路径）
>[!注意]
>yum命令需要root权限且需要联网

[^1]: linux常见安装包文件名

## systemctl命令

Linux系统很多内置和第三方软件都支持使用systemctl命令控制启动、停止、开机自启动
能被systemctl管理的软件一般也称之为：服务
语法：`systemctl start | stop | status | enable |disable 服务名
* start 启动
* stop 关闭
* status 查看状态
* enable 开启开机自启动
* disable 关闭开机自启动

系统有很多内置的服务，如：
* NetworkManager 主网络服务
* network 副网络服务
* firewalld 防火墙服务 
* sshd，ssh服务

很多第三方软件通过yum下载后会自动注册服务，如果没有自动注册，可以手动注册

## ln命令与软连接
什么是软连接？——在系统中创建软链接，可以将文件、文件夹链接到其他位置。
类似obsidian的双链功能
语法：`ln -s 参数一 参数二`
* -s选项，创建软链接
* 参数一：被链接的文件或文件夹
* 参数二：要链接去的目的地
示例：`ln -s /etc/yum.conf ~/yum`
将`/etc/yum/conf`的文件链接到`~/yum`中