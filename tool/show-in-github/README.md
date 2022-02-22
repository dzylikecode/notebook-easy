- [show-in-github](#show-in-github)
  - [思路](#思路)
    - [扩展](#扩展)
  - [code](#code)
    - [模块](#模块)
      - [pdf](#pdf)
      - [ppt](#ppt)
      - [word](#word)
      - [delog](#delog)
  - [python](#python)
    - [grammar](#grammar)
  - [havest](#havest)

# show-in-github

## 思路

1. 递归地寻找文件夹中的所有文件
2. 当前文件夹内是否有符合工作对象的文件
3. 工作对象文件
   > 1. 根据后缀名判断处理方式
   > 2. 创建一个同名文件夹
   > 3. 将文件赋值到同名文件夹中
   > 4. 进入同名文件夹中工作
   > 5. 创建类型转化的文件夹
   >    > eg. `.pict_pdf2svg`, `.pict_pptx2svg`
   > 6. 完成类型转化
   > 7. 创建 REAMDME.md, 帮助显示
   > 8. 返回到上一级文件夹, 进一步创建 REAMDME.md, 用来链接到显示的 README.md

### 扩展

可以回退:

在文件里面错放之前相对位置的信息 如 `hui_notebook_easy.txt`

## code

### 模块

#### pdf

- dependencies
  > [pdf2svg](https://www.pdftron.com/documentation/cli/download/)
  >
  > extension : [PDFTRON](https://www.pdftron.com/documentation/python/get-started/)

#### ppt

- dependencies
  > [pptx python](https://blog.aspose.com/2022/02/01/convert-powerpoint-ppt-slides-to-svg-in-python/)

#### word

- dependencies
  > [word2html](https://blog.aspose.com/2021/11/01/convert-word-to-html-in-python/)

#### delog

```shell
$ pip install loguru
```

## python

### grammar

## havest

因为 python 中一切皆为对象，你所看到的一切变量，本质上都是对象的一个指针。当一个对象不再调用的时候，也就是当这个对象的引用计数(指针数)为 0 的时候，说明这个对象永不可达，自然它也就成为了垃圾，需要被回收。

那么，即使函数返回后，列表的引用依然存在，于是对象就不会被垃圾回收
