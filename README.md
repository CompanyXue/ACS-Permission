# ACS-Permission
用户管理--权限管理--资源管理


### 一、角色访问控制（RBAC，Role-Based Access Control）
   概念最初是在1992年由美国国家标准局（NIST）所提出，目前国外RBAC研究机构主要是美国NIST和George Mansion Univ。LIST实验室（Prof。Ravi。Sandhu）。

      RBAC引入了Role的概念，目的是为了隔离User（即动作主体，Subject）与Privilege（权限，表示对Resource的一个操作，即Operation+Resource）。

　　Role作为一个用户（User）与权限（Privilege）的代理层，解耦了权限和用户的关系，所有的授权应该给予Role而不是
直接给User或Group。Privilege是权限颗粒，由Operation和Resource组成，表示对Resource的一个Operation。例如，
对于信息栏目的删除操作。Role-Privilege是many-to-many的关系，这就是权限的核心。

基于角色的访问控制方法（RBAC）的显著的两大特征是：
1。由于角色/权限之间的变化比角色/用户关系之间的变化相对要慢得多，减小了授权管理的复杂性，降低管理开销。
2。灵活地支持企业的安全策略，并对企业的变化有很大的伸缩性。


RBAC认为权限授权实际上是Who、What、How的问题。在RBAC模型中，who、what、how构成了访问权限三元组，也就是“Who对What(Which)进行How的操作”。

* Who：权限的拥用者或主体（如Principal、User、Group、Role、Actor等等）

* What：权限针对的对象或资源（Resource、Class）。

* How：具体的权限（Privilege，正向授权与负向授权）。


Group要实现继承。即在创建时必须要指定该Group的Parent是什么Group。在粗粒度控制上，可以认为，只要某用户直接或者间接的属于某个Group那么它就具备这个Group的所有操作许可。细粒度控制上，在业务逻辑的判断中，User仅应关注其直接属于的Group，用来判断是否“同组” 。Group是可继承的，对于一个分级的权限实现，某个Group通过“继承”就已经直接获得了其父Group所拥有的所有“权限集合”，对这个Group而言，需要与权限建立直接关联的，仅是它比起其父Group需要“扩展”的那部分权限。子组继承父组的所有权限，规则来得更简单，同时意味着管理更容易。为了更进一步实现权限的继承，最直接的就是在Group上引入“父子关系”。

Permission, 是Resource Related的权限。 而权限，包括系统定义权限和用户自定义权限用户自定义权限之间可以指定排斥和包含关系(如：读取，修改，管理三个权限，管理 权限 包含 前两种权限)。Privilege 如"删除" 是一个抽象的名词，当它不与任何具体的 Object 或 Resource 绑定在一起时是没有任何意义的。拿新闻发布来说，发布是一种权限，但是只说发布它是毫无意义的。因为不知道发布可以操作的对象是什么。只有当发布与新闻结合在一起时，才会产生真正的 Privilege。这就是 Privilege Instance。权限系统根据需求的不同可以延伸很多不同的版本。


关系：

* Privilege   n : 1   Resource

* Role   n : n   Privilege

* Group   n : n   User

* Group   n : n   Role

* User  n : n   Role

### 核心实现

权限系统的核心由以下三部分构成：创造权限、分配权限、使用权限。

1、 Creator 创造 Privilege， Creator 在设计和实现系统时会划分，一个子系统或称为模块，应该有哪些权限。这里完成的是 Privilege 与 Resource 的对象声明，并没有真正将 Privilege 与具体Resource 实例联系在一起，形成Operator。

2、 Administrator 指定 Privilege 与 Resource Instance 的关联。在这一步， 权限真正与资源实例联系到了一起， 产生了Operator（Privilege Instance）。Administrator利用Operator这个基本元素，来创造他理想中的权限模型。如，创建角色，创建用户组，给用户组分配用户，将用户组与角色关联等等。这些操作都是由 Administrator 来完成的。

   ![tuple](http://pic002.cnblogs.com/images/2011/10016/2011070808443232.jpg)


3、 User 使用 Administrator 分配给的权限去使用各个子系统。Administrator 是用户，在他的心目中有一个比较适合他管理和维护的权限模型。于是，程序员只要回答一个问题，就是什么权限可以访问什么资源，也就是前面说的 Operator。程序员提供 Operator 就意味着给系统穿上了盔甲。Administrator 就可以按照他的意愿来建立他所希望的权限框架自行增加，删除，管理Resource和Privilege之间关系。可以自行设定用户User和角色Role的对应关系。(如果将 Creator看作是 Basic 的发明者， Administrator 就是 Basic 的使用者，他可以做一些脚本式的编程) Operator是这个系统中最关键的部分，它是一个纽带，一个系在Programmer，Administrator，User之间的纽带。

***
### 二、SQLAlchemy支撑

      它是Python编程语言下的一款ORM框架，该框架建立在数据库API之上，使用关系对象映射进行数据库操作，
简言之便是：将对象转换成SQL，然后使用数据API执行SQL并获取执行结果。

ORM方法论 基于三个核心原则：

* 【简单：以最基本的形式建模数据。】

* 【传达性：数据库结构被任何人都能理解的语言文档化。】

* 【精确性：基于数据模型创建正确标准化了的结构。】

ORM 框架的作用:将数据库表中的一行记录与一个对象互相作自动转换。

***

### 三、User Story -用户故事


通常按照如下的格式来表达：

英文：

* As a <Role>, I want to <Activity>, so that <Business Value>.

中文：

* 作为一个<角色>, 我想要<活动>, 以便于<商业价值>。


关于用户故事，Ron Jeffries用3个C来描述它：

- 卡片（Card） - 用户故事一般写在小的记事卡片上。卡片上可能会写上故事的简短描述，工作量估算等。

- 交谈（Conversation）- 用户故事背后的细节来源于和客户或者产品负责人的交流沟通。

- 确认（Confirmation）- 通过验收测试确认用户故事被正确完成。

### 四、Token 认证

对Token认证机制有5点直接注意的地方：

- 一个Token就是一些信息的集合；

- 在Token中包含足够多的信息，以便在后续请求中减少查询数据库的几率；

- 服务端需要对cookie和HTTP Authrorization Header进行Token信息的检查；

- 基于上一点，你可以用一套token认证代码来面对浏览器类客户端和非浏览器类客户端；

- 因为token是被签名的，所以我们可以认为一个可以解码认证通过的token是由我们系统发放的，其中带的信息是合法有效的；