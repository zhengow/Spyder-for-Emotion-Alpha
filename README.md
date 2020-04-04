### Requirements
python3.5+
  
requests==2.19.1  

### Use
单账号抓取：请你打开百度的首页，登录后，找到www.baidu.com此条GET请求，并复制此条请求的request headers里的cookie，将此cookie粘贴到config.py中的COOKIES对象中  
  

### Tip
- 搜索指数最早的数据日期为2011-01-01
- 开始时间超过最早的数据日期会导致数据不准确  
- 初始化类时传入area可以查询指定区域的百度指数, 默认为全国
- 有些代码不是特别严谨, 有需要请自己DIY
- 媒体指数不支持细分地域查询


