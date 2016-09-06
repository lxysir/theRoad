##这是我的第一份Python学习笔记

从下定决心学习python以来，经历了多次**游移不定**，终于还是决定先学完再说，引用前辈的一句话：

>管那么多干嘛，学了再说吧

ok，所以了，下面就是一些心得：

###Project1: 一个简单的爬虫-爬取网页中的链接

###Project2: PageRank算法的python实现-构建自己的搜索引擎

    def union(p, q):
    	for e in q:
    		if e not in q:
    			p.append(e)
    p = ['a', 'b', 'c']
    q = ['c', 'd', 'e']
    print(union(p, q))
