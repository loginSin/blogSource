---
title: markdown-添加图片和超链接
date: 2016-06-16 01:19:48
tags:
---
我使用的hexo来搭建的博客，详情可以在简书上进行查找
之前没有用过，所以使用Mou对md文件进行编译都只有纯问文字，今天看到一位大神的项目写了一个md文件，可以显示图片，所以就对其稍微研究了一下，顺手研究了一下超链接，再次分享一下
1、图片展示
在后面的()中写入图片的链接，建议写网络图片路径，我在github上创建了一个仓库，专门用来存放博客中需要用到的脚本和图片等相关资源
![url demo](https://raw.githubusercontent.com/loginSin/blogSource/master/images/markdown/markdown.png)

2、超链接
超链接可以直接使用html的a标签来实现
![url demo](https://raw.githubusercontent.com/loginSin/blogSource/master/images/markdown/markdown2.png)

比如：
<a href="https://raw.githubusercontent.com/loginSin/blogSource/master/images/test.jpg">女神</a>

原始的md文件：
<a href="markdown-添加图片和超链接.md">点我啊</a>