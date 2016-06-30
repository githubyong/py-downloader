# py-downloader

![Lisense: GPL v3][1]
[1]: http://img.shields.io/badge/license-GPL_v3-red.svg?style=flat-square

说明;下载小工具，可下载固定长度的文件(即headers包含Content-Length属性的连接)，暂不支持‘Transfer-Encoding: chunked’类型连接.
用途:在某些时候，比如p2p下载被禁止或限速，而直接通过浏览器下载的速度又比较慢时，可以尝试下这个 O(∩_∩)O

**How to use it?**

      -h,--help: 帮助.
      -v,--version: 版本信息.
      -x,--debug:开启debug模式
      -u=,--url=下载文件的url.
      -c=,--connection=n:开启n个连接(线程)去下载文件.(默认:1，站点出口速度不好的话开多个可以加快下载速度).
      -d=,--dir=d:/file/xxx:保存文件的路径 (默认为当前文件夹).
      -f=,-fName=xx: 要保存的文件名(默认截取url的最后一个 '/'之后的字符串).
      eg:cat -u http://dlsw.baidu.com/sw-search-sp/soft/3d/20621/XMusicSetup_2_0_2_1618.1394071033.exe -c 3
      表示用开3个线程去下载这个链接的文件.

usage(Eng):

      -h,--help: help info.'
      -v,--version: version info'
      -x,--debug:run as debug mode.
      -u=,--url=url to be work'
      -c=,--connection=n: num of connections (threads) to be opend to get the file .(default :1)'
      -d=,--dir=d:/file/xxx: the dir that download file will be saved in . (default:current dir)'
      -f=,-fName=xx: file name to be saved .(default:str after last ' / ')
