<h1 align="center">Colort</h1>

<p align="center">
    <a href="https://pepy.tech/project/colort"><img alt="Downloads" src="https://static.pepy.tech/badge/colort"></a>    
    <a href="https://pepy.tech/project/colort"><img alt="Downloads" src="https://static.pepy.tech/badge/colort/month"></a>
    <a href="https://pepy.tech/project/colort"><img alt="Downloads" src="https://static.pepy.tech/badge/colort/week"></a>
</p>

终端中的彩色显示

## 使用

### 安装

```shell
pip install colort
```

### 使用

```python
from colort import display_style as ds

src = "这是要显示的文本"
dist = ds.format_with_one_style(src, ds.foreground_color.red)
print("更改文字颜色：", dist)
dist = ds.format_with_one_style(src, ds.backgorud_color.green)
print("更改文字背景色：", dist)
dist = ds.format_with_multiple_styles(src, ds.foreground_color.red, ds.mode.underline, ds.mode.bold)
print("多种样式：", dist)
```

效果：

![sample](https://cdn.jsdelivr.net/gh/thep0y/image-bed/md/1622076879923.png)
