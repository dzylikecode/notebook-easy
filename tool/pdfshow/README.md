# pdf-in-github

## target

为了能够在 github 上显示 pdf

## dependencies

[pdf2svg](https://www.pdftron.com/documentation/cli/download/)

> extension : [PDFTRON](https://www.pdftron.com/documentation/python/get-started/)


## havest

因为python中一切皆为对象，你所看到的一切变量，本质上都是对象的一个指针。当一个对象不再调用的时候，也就是当这个对象的引用计数(指针数)为 0 的时候，说明这个对象永不可达，自然它也就成为了垃圾，需要被回收。

那么，即使函数返回后，列表的引用依然存在，于是对象就不会被垃圾回收 