# 项目文档说明
## 基于知识图谱的出版物检索和推荐系统

### 项目要求：

1. 出版物包括：电影、图书、游戏三类
2. 采用的知识图谱包括DBpedia开放数据
3. 实现出版物的检索功能，能够直接检索到相关出版物的基本信息
4. 实现出版物的语义推荐功能，基于知识图谱给出的语义，推荐用户可能感兴趣的其他出版物，注意课上提到的推荐中需要注意的问题
5. 实现对出版物相关数据的可视化分析与展示，包括检索结果中部分数据的可视化展示以及对于出版物的统计分析等。

### 小组成员：
    姓名   学号             主要负责的东西                             得分系数
1. 白 玲  ZF1721101   主要负责推荐查询模块的编写，统筹整体的安排            25%
2. 牛晨雪 ZF1721250   主要负责网页的编写                                 25%
3. 蔡晨毅 ZF1721104   主要负责说明文档的编写                              25%
4. 吴 迪  ZF1721331   主要负责使用文档的编写                              25%

### 使用技术

1. 基于python使用Flask框架
2. 基于python使用sparql查询语言去查询dbpedia

### 特色功能
在网站上实时查询需要的数据是我们这个项目最有特色的功能，保证用户获得最新的数据信息。

### 课程总结
通过这门课程，我们学到了知识工程相关知识，通过理论和实践的结合，我们掌握了sparql查询语言，掌握了一些关于知识工程的工具。 
对于网页的编写有了一定的了解。 

感谢老师！


## 项目思路
1. 在网站中选择类别，输入关键字，进行搜索。 
	书籍和电影是基于作者的匹配，一旦输入该作者的名字，选择相应的类别，就会推荐出来相应的作品。对于游戏的推荐，是基于类型的推荐，
	输入相应的类型，就会出来相应的游戏。
2. 搜索的内容会使用sparql查询语言从[DBPedia](http://wiki.dbpedia.org/)获取数据，其中电影和书籍在查询的过程中会按照作者进行推荐，游戏在查询的过程中会根据类型进行推荐，sparql查询语句见im_spider.py
3. 对获取的数据进行json解析
4. 返回解析后的数据传送给网站，在网站上展示检索结果 

