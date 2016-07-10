#!/usr/bin/env python
# coding=utf8

header = '''
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?de33185aab4349864a83eda0e0dbff8f";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
'''


with open('index.html', 'r') as f:
    data = f.read()
    idx = data.find('</head>')
    newdata = data[:idx-1] + header + data[idx:]

with open('index.html', 'w') as f:
    f.write(newdata)

