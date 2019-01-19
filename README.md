# local_file_share
# 描述
1 实现局域网内文件分享下载。pc端运行程序，手机端通过扫描二维码得到下载地址，浏览器打开
2 可以实现单文件下载，文件夹查看
3 一个用户分享文件，其他用户可以通过链接下载
# 安装
点击main.exe 运行

下载[local_file_share.zip](https://github.com/woshimanong1990/local_file_share/releases/download/v0.0.1/local_transfer_file.zip "download link"). 

# 原理
1 pc端开启一个服务(simplehttpserver)，用户设定下载的文件，pc端收到请求时验证
2 将间接生成二维码，同一个局域网内下载

# 依赖
Pyqt5
qrcode

# 注意事项
1 需要同处一个局域网内， wifi同处一个网段
2 注意个人隐私

# 声明
图片没有找到作者，如果侵权，请联系我删除。


# 协议
MIT