# 开发初衷

自诩为一位极简主义者的我发现我的东西还是太多了，想对自己的所有物品以及未来想拥有的物品进行良好的管理，就开发了“格物”物品管理系统。

# 应用技术

后端使用python的Django框架，前端使用了Bootstrap5样式，HTML，CSS，JS以及具体的ajax异步请求，连接了MySQL数据库。

# 实现功能

- 用户登录&注册&退出
  - 登录![image-20241122095809522](https://s2.loli.net/2025/03/29/CFyPmiAaTh58WHM.png)
  - 注册![image-20241122095911895](https://s2.loli.net/2025/03/29/PMGKmCyidcuL6D5.png)![image-20241122095136221](https://s2.loli.net/2025/03/29/i8Er1CFVD4ROyWb.png)
  - 退出![image-20241122095921389](https://s2.loli.net/2025/03/29/QybM5it67fhzcuk.png)
- 添加物品![image-20241122095945912](https://s2.loli.net/2025/03/29/aRwA9uog3K2G1lE.png)
- 修改和删除物品
  - ![image-20241122100008129](https://s2.loli.net/2025/03/29/e8psGKqB5Lo3t9P.png)
  - ![image-20241122100020113](https://s2.loli.net/2025/03/29/yGka4DjWHtBo7gl.png)
  - ![image-20241122100049203](https://s2.loli.net/2025/03/29/gjNTthXvSy9IWmn.png)
  - ![image-20241122100100877](https://s2.loli.net/2025/03/29/IeuA6JbmyPQ58Mv.png)
- 查看所有物品![image-20241122100120796](https://s2.loli.net/2025/03/29/RuVtgdlIMpYahyL.png)
- 查看不同种类下或不同状态下的所有物品
  - ![image-20241122100330978](https://s2.loli.net/2025/03/29/mGbNdislge3zD2t.png)
  - ![image-20241122100146644](https://s2.loli.net/2025/03/29/3ikZj2ge4E16MGN.png)
  - ![image-20241122100346884](https://s2.loli.net/2025/03/29/ziLKQJNZl5fPR8T.png)
  - ![image-20241122100201968](https://s2.loli.net/2025/03/29/bkZ5T3XiO1dlcoP.png)
- 查看物品的具体信息![image-20241122100246332](https://s2.loli.net/2025/03/29/e8psGKqB5Lo3t9P.png)
- 物品的统计数据![image-20241122100257832](https://s2.loli.net/2025/03/29/GCbKs9EwveoAVQc.png)
- 查看物品的过期时间线![image-20241122100305899](https://s2.loli.net/2025/03/29/tkfrX7wqQ8EWU5C.png)
- 对物品的名称或描述进行搜索![image-20241122100416001](https://s2.loli.net/2025/03/29/on6pqs9rVfgSv5W.png)

# 具体实现

GrantItems项目下有两个APP，用户登录APP和物品管理APP。

## 用户登录APP

![image-20241122102741890](https://s2.loli.net/2025/03/29/GJErfUVvqipWO3t.png)

- 两个页面：注册和登录
  - ![image-20241122101015743](https://s2.loli.net/2025/03/29/2nYIbAyXjLJpSEN.png)
  - ![image-20241122101029676](https://s2.loli.net/2025/03/29/jiWQKlmcr83SZkn.png)
- 四个函数：用户登录、退出、注册以及给邮箱发送验证码
  - ![image-20241122101050810](https://s2.loli.net/2025/03/29/o5KmtxThcDj3gpM.png)
  - ![image-20241122101100169](https://s2.loli.net/2025/03/29/m9VNs5bBGq3wXvZ.png)
  - ![image-20241122101110348](https://s2.loli.net/2025/03/29/qGdsarVPH1ozXli.png)
  - ![image-20241122101119380](https://s2.loli.net/2025/03/29/SuPGdw2XTANq8hF.png)
- 两个表单：登录表单和注册表单
  - ![image-20241122101141955](https://s2.loli.net/2025/03/29/HfxaDUdB9ZMJ8tn.png)
  - ![image-20241122101153503](https://s2.loli.net/2025/03/29/mziq7XujAQolPRk.png)
- 一个模型：验证码模型
  - ![image-20241122101203301](https://s2.loli.net/2025/03/29/fGK65pOvJk8RbjA.png)



## 物品管理APP

![image-20241122102726855](https://s2.loli.net/2025/03/29/7qKgOrX3AeowyW9.png)

### 物品模型

![image-20241122101955824](https://s2.loli.net/2025/03/29/crdu46L9Kel1zhD.png)

![image-20241122102005542](https://s2.loli.net/2025/03/29/vR6SolU9nyr7Ecj.png)

![image-20241122102022869](https://s2.loli.net/2025/03/29/hkG6cWnVivYND3L.png)

### 表单

![image-20241122102040935](https://s2.loli.net/2025/03/29/mZiBR6VeXcSw4pj.png)

### 未登录首页

![image-20241122101739372](https://s2.loli.net/2025/03/29/d1jpmCLBKeb54nJ.png)

![image-20241122101756530](https://s2.loli.net/2025/03/29/jtHxBPGm4NnQurf.png)

### 已登录首页

![image-20241122101827431](https://s2.loli.net/2025/03/29/pK9lJWOstkUxSd4.png)

![image-20241122101901961](https://s2.loli.net/2025/03/29/vCJgMyUwEmbzui8.png)

![image-20241122101917432](https://s2.loli.net/2025/03/29/TzhS4AvI98jlrsf.png)

### 添加物品

![image-20241122102143680](https://s2.loli.net/2025/03/29/AtJVUOMFcYKWTxs.png)

![image-20241122102201991](https://s2.loli.net/2025/03/29/xXsPdVgSKy7RJav.png)

### 修改物品

![image-20241122102252695](https://s2.loli.net/2025/03/29/KrbwnS956NiztTQ.png)

![image-20241122102310104](https://s2.loli.net/2025/03/29/laKXZuqxr95zkDN.png)

### 移除或删除物品

![image-20241122102335412](https://s2.loli.net/2025/03/29/n7zXhCKfMdOm825.png)

### 显示所有/特定种类/特定状态的物品

![image-20241122102444307](https://s2.loli.net/2025/03/29/TPp8WzsrIuKkqfO.png)

![image-20241122102457218](https://s2.loli.net/2025/03/29/q21EOnPgiVZkhaB.png)

### 查看物品信息

![image-20241122102519795](https://s2.loli.net/2025/03/29/DATUHct8qjdBCxO.png)

![image-20241122102535940](https://s2.loli.net/2025/03/29/wOgWmubLTG29Mz1.png)

### 过期时间线

![image-20241122102608838](https://s2.loli.net/2025/03/29/q86WzFtxSYMpCoL.png)

![image-20241122102620085](https://s2.loli.net/2025/03/29/CSKXFyab26vco1V.png)

### 搜索功能

![image-20241122102648474](https://s2.loli.net/2025/03/29/ZOL42gk9aEHbBKN.png)

# 后续改进

- 物品即将过期时发邮件提醒
- 移动端
