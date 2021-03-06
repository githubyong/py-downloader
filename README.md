# py-downloader

![Lisense: GPL v3][1]
[1]: http://img.shields.io/badge/license-GPL_v3-red.svg?style=flat-square
##基本信息
* 说明:下载小工具，主要使用requests+threading写成，可下载固定长度的文件(即headers包含Content-Length属性的连接)，暂不支持‘Transfer-Encoding: chunked’类型连接
* 用途:在某些时候，比如p2p下载被禁止或限速，而直接通过浏览器下载的速度又比较慢时，可以尝试下这个 O(∩_∩)O

如下是我在下载一个virtualbox时分别使用迅雷龟速和使用本程序下载的时候一个还可以接受的速度对比:<br>
![2]<br>
![3]
[2]:https://github.com/githubyong/py-downloader/blob/master/img/thunder.png
[3]:https://github.com/githubyong/py-downloader/blob/master/img/mycat.png

###如何使用?

      -h,--help: 帮助.
      -v,--version: 版本信息.
      -x,--debug:开启debug模式
      -u=,--url=下载文件的url.
      -c=,--connection=n:开启n个连接(线程)去下载文件.(默认:1，站点出口速度不好的话开多个可以加快下载速度).
      -d=,--dir=d:/file/xxx:保存文件的路径 (默认为当前文件夹).
      -f=,-fName=xx: 要保存的文件名(默认截取url的最后一个 '/'之后的字符串).
      eg:cat -u http://dlsw.baidu.com/sw-search-sp/soft/3d/20621/XMusicSetup_2_0_2_1618.1394071033.exe -c 3
      表示用开3个线程去下载这个链接的文件.

###How to use it?

      -h,--help: help info.
      -v,--version: version info
      -x,--debug:run as debug mode.
      -u=,--url=url to be work
      -c=,--connection=n: num of connections (threads) to be opend to get the file .(default :1)
      -d=,--dir=d:/file/xxx: the dir that download file will be saved in . (default:current dir)
      -f=,-fName=xx: file name to be saved .(default:str after last ' / ')

### Work Details
      1.Tracker 请求url,获取Content-Length,本地建立文件,然后等分为n个片段.
      2.开启n个Worker(线程)取file对应片段,向本地文件指定位置循环写入.
      3.Tracker每秒检查自己线程数组中各个worker的状态，更新下载速度，完成百分比和预估剩余时间，更新进度条.
