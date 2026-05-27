[github](https://github.com/)
这篇专门记录github设置和使用技巧
## 团队内协作
需要加入团队，才有权限push到同一个远程库中
在github远程库中设置manage access发送邀请函（一个链接地址）
对方打开链接接受邀请

## 跨团队协作
团队外的需要用fork加到自己的库中
团队外的人要发送pull request，库主人同意后merge到自己的库中

## SSH免密登录
`ssh-keygen -t 加密方式 -C 账号`
* `ssh-keygen`：启动生成密钥的工具
* `-t 加密方式`:-t是类型的意思，后面加加密方式（ed25519或rsa）
* `-C 邮箱`：-C是备注的意思，只是给密钥加个标签