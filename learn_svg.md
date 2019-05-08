# 概念
SVG全称是可缩放矢量图（Scalable Vector Graphics），是一种基于XML语法，用于描述二维矢量图形的图形格式。jpg，png等其他图像格式都是基于像素处理的，而SVG是用文本格式的描述性语言来描述图像内容，因此是一种和图像分辨率无关的矢量图形格式，可以无损进行缩放。
## SVG格式的优点：
1. 图像文件可读，易于修改和编辑
2. 与现有技术可以互动融合。例如，SVG技术本身的动态部分（包括时序控制和动画）就是基于SMIL标准。SVG文件还可嵌入JavaScript脚本来控制SVG对象
3. SVG图形格式可以方便的创建文字索引，从而实现基于内容的图像搜索
4. SVG图形格式支持多种滤镜和特殊效果，在不改变图像内容的前提下可以实现位图格式中类似文字阴影的效果
5. SVG图形格式可以用来动态生成图形。例如，可用SVG动态生成具有交互功能的地图

## SVG格式的缺点：
1. 较老的IE浏览器不支持（需要IE9+）
3. 由于原始的SVG档是遵从XML语法，导致数据采用未压缩的方式存放，因此相较于其他的矢量图形格式，同样的文件内容会比其他的文件格式稍大
4. SVG标准不兼容，旧版的SVG Viewer无法正确显示出使用新版SVG格式的矢量图形

# SVG使用方式
## SVG的基础知识
SVG必须使用`<svg>`元素进行声明，表示一个SVG文档片段。可以直接嵌入HTML，也可以在直接存为一个svg文件。

使用图形元素来绘制图形，常用的图形元素有：矩形`<rect>`、圆`<cicrle>`、椭圆`<ellipse>`、多边形`<polygon>`、直线`<line>`、折线`<polyline>`、任意曲线`<path>`等。

可以使用`<g>`元素来做组合对象的容器，其子元素可以继承其属性。此外，`<g>`元素也可以用来定义复杂的对象，之后可以通过<use>元素来引用它们。

可以使用`<defs>`元素来预定义图形，并且在其他元素中引用。

可以直接在元素上定义属性来设置图形的线宽，颜色，填充色等；也可以使用css来定义，但是属性和普通css不相同。

svg的坐标体系。如下图，取svg元素左上角为坐标原点，X轴向右递增，Y轴向下递增。进行图形绘制时，以此坐标来定位。但是需要注意的是`text`元素的x,y属性定位时是该元素的左下角。
<div>
<svg width="120" height="120">
	<g stroke="#425766" stroke-width="2">
		<line x1="6" y1="6" x2="6" y2="120" />
		<line x1="6" y1="120" x2="0" y2="114" />
		<line x1="6" y1="120" x2="12" y2="114" />
		<line x1="6" y1="6" x2="120" y2="6" />
		<line x1="120" y1="6" x2="114" y2="0" />
		<line x1="120" y1="6" x2="114" y2="12" />
	</g>
	<g style="color:#425766;font-size:12px;" stroke-width="1">
		<text x="10" y="22">原点(0,0)</text>
		<text x="100" y="22">X轴(100,0)</text>
		<text x="12" y="110">Y轴(0,100)</text>
	</g>
</svg>
</div>
## 如何在HTML中使用SVG
SVG在网页中使用有很多种方式，即可像其他图片文件一样直接引用，也可以做像其他DOM元素一样嵌入其中。示例如下：
```html
  // SVG 文件可以直接插入网页，成为 DOM 的一部分，然后用 JavaScript 和 CSS 进行操作。
  <!DOCTYPE html>
  <html>
  <head></head>
  <body>
    <svg id="mysvg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
      <circle id="mycircle" cx="400" cy="300" r="50" />
    <svg>
   </body>
  </html>
  
  // SVG代码也可以写在一个独立文件中，然后用<img>、<object>、<embed>、<iframe>等标签插入网页。
  <img src="circle.svg">
  <object id="object" data="circle.svg" type="image/svg+xml"></object>
  <embed id="embed" src="icon.svg" type="image/svg+xml">
  <iframe id="iframe" src="icon.svg"></iframe>

  //SVG文件还可以转为 BASE64 编码，然后作为 Data URI 写入网页。
    <img src="data:image/svg+xml;base64,[data]">

  // CSS 也可以使用 SVG 文件。
  .logo {
    background: url(icon.svg);
  }
```
# SVG常用元素介绍
SVG标准中的元素，主要分为：容器元素，基本图形元素，描述性元素，动画元素，滤镜元素，字体元素等等。本文只介绍前三类元素中最基本元素的使用，后续再描述其他元素的使用方法。
## 容器元素
### svg
`<svg>`元素是SVG图片的根元素/容器，表示一个SVG文档片段。其主要属性如下。

属性  | 描述 | 默认值
--- | --- | ---
width  | SVG片段的宽度，可以是像素也可以是百分比  | 100% 
height  | SVG片段的高度，可以是像素也可以是百分比 | 100% 
viewBox  | 用来控制实际显示的内容，即只显示`svg`元素内部分区域，并缩放。该属性是一个包含4个参数的列表start-x,start-y,width和height，以空格或者逗号分隔开。用以设置实现显示区域的初始坐标和宽高。如果x+width>svg width,则会向右移，以保证最终显示区域的width不变。height规则相同。不允许宽度和高度为负值,0则禁用元素的呈现。  | 0，0，svg width，svg height，全部显示 
preserveAspectRatio | 表示对viewBox选中的区域是否强制进行统一缩放.规则过于复杂，这里不再转述，详见[preserveAspectRatio](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/preserveAspectRatio) | none，根据显示区域决定是否缩放 

### defs
`<defs>`元素来自定义图形，它内部的图形不会显示，仅供在其他元素中引用。例如定义一个箭头图形，供其他连线使用。
```html
<defs>
  <marker id="markerArrow" markerWidth="4" markerHeight="4" refX="0" refY="2" orient="auto">
    <path d="M0,0 L4,2 L0,4 z" class="axis-arrow"></path>
  </marker>
</defs>

<path d="M100,10 L150,10 L150,60" style="stroke: #6666ff; stroke-width: 1px; fill: none;
      marker-end: url(#markerArrow) "></path>
```
<svg width="100" height="100">
<defs>
  <marker id="markerArrow" markerWidth="4" markerHeight="4" refX="0" refY="2" orient="auto">
    <path d="M0,0 L4,2 L0,4 z" class="axis-arrow"></path>
  </marker>
</defs>
<path d="M10,10 L50,10 L50,60" style="stroke: #6666ff; stroke-width: 1px; fill: none;
      marker-end: url(#markerArrow) "></path>
</svg>

### g
`<g>`元素来做组合对象的容器，其子元素可以继承其属性。此外，`<g>`元素也可以用来定义复杂的对象，之后可以通过`<use>`元素来引用它们。
```html
<defs>
  <g id="ShapeGroup">
    <rect x="0" y="0" width="100" height="100" fill="#69C" stroke="red" stroke-width="2"/>
    <circle cx="50" cy="50" r="40" stroke="#00f" fill="none" stroke-width="5"/>
  </g>
</defs>
<use xlink:href="#ShapeGroup" x="0" y="0" transform="scale(0.5)"/>
<use xlink:href="#ShapeGroup" x="10" y="10" transform="scale(1)"/>
<use xlink:href="#ShapeGroup" x="30" y="30" transform="scale(1.5)"/>
```

<svg width="300" height="240">
  <defs>
    <g id="ShapeGroup">
      <rect x="0" y="0" width="100" height="100" fill="#69C" stroke="red" stroke-width="2"/>
      <circle cx="50" cy="50" r="40" stroke="#00f" fill="none" stroke-width="5"/>
    </g>
  </defs>
  <use xlink:href="#ShapeGroup" x="0" y="0" transform="scale(0.5)"/>
  <use xlink:href="#ShapeGroup" x="10" y="10" transform="scale(1)"/>
  <use xlink:href="#ShapeGroup" x="30" y="30" transform="scale(1.5)"/>
</svg>

## 常用属性介绍
在绘制图形时，经常使用如下一些属性，用来定义图形的样式，可以直接在元素上直接设置属性，也可以类似CSS一样使用。

属性  | 描述 | 默认值 
--- | --- | ---
| fill | 图形内填充颜色，与css颜色定义相同，可以预定义，长/短十六进制和rgb方式定义 | none，无填充色 |
| stroke | 图形外轮廓线条的颜色，与css颜色定义相同 | none，无颜色 |
| stroke-width | 图形外轮廓线条的宽度像素值，如果使用了一个百分比，这个值代表当前视图的百分比 | 1 |

SVG的相关属性，同样也可以采用css样式来定义
```css
.myrect{
  fill: red;
  stroke: #0FF;
  stroke-width: 1;
}
```

## 基本图形元素
### rect矩形
`<rect>`元素用来绘制矩形，属性x，y指定矩形左上角的坐标，属性width设置宽度，属性height设置高度。
```html
<rect x="2" y="2" width="90" height="90" fill="#69C" stroke="red" stroke-width="2"/>
```
<svg width="100" height="100">
<rect x="2" y="2" width="90" height="90" fill="#69C" stroke="red" stroke-width="2"/>
</svg>

### cicrle圆
`<cicrle>`元素用来绘制圆形，属性cx，cy指定圆形的圆心坐标，属性r设置圆的半径。
```html
<circle cx="50" cy="50" r="40" stroke="#00f" fill="none" stroke-width="2"/>
```
<svg width="100" height="100">
<circle cx="50" cy="50" r="40" stroke="#00f" fill="none" stroke-width="2"/>
</svg>

### ellipse椭圆
`<ellipse>`元素用来绘制椭圆，属性cx，cy指定椭圆的中心坐标，属性rx设置椭圆的横轴半径，属性ry设置椭圆的纵轴半径。
```html
<ellipse cx="50" cy="50" rx="40" ry="30" stroke="#00f" fill="none" stroke-width="2"/>
```
<svg width="100" height="100">
<ellipse cx="50" cy="50" rx="40" ry="30" stroke="#00f" fill="none" stroke-width="2"/>
</svg>

### polygon多边形
`<polygon>`元素用来绘制多边形，属性point用来设置多边形的各端点。points默认会自动闭合,无需最后添加起始点。
```html
<polygon points="2,2 98,2 80,50 98,98 2,98 " stroke="#00f" fill="none" stroke-width="2"/>
```
<svg width="100" height="100">
<polygon points="2,2 98,2 80,50 98,98 2,98 " stroke="#00f" fill="none" stroke-width="2"/>
</svg>

### line直线
`<line>`元素用来绘制直线，x1属性和y1属性，表示线段起点的横坐标和纵坐标；x2属性和y2属性，表示线段终点的横坐标和纵坐标。
```html
<line x1="10" y1="10" x2="100" y2="100" stroke="#00f" fill="none" stroke-width="2"/>
```
<svg width="100" height="100">
<line x1="10" y1="10" x2="100" y2="100" stroke="#00f" fill="none" stroke-width="2"/>
</svg>

### polyline折线
`<polyline>`元素用来绘制折线，属性point用来设置折形的各端点。。
```html
<polyline points="2,2 98,2 80,50 98,98 2,98" stroke="#00f" fill="none" stroke-width="2"/>
```
<svg width="100" height="100">
<polyline points="2,2 98,2 80,50 98,98 2,98" stroke="#00f" fill="none" stroke-width="2"/>
</svg>

### path任意曲线
`<path>`元素用来绘制任意曲线，属性d设置曲线的定义。
```html
<path fill="none" stroke="red"
    d="M 10,30
       A 20,20 0,0,1 50,30
       A 20,20 0,0,1 90,30
       Q 90,60 50,90
       Q 10,60 10,30 z" />
```
<svg width="100" height="100">
<path fill="none" stroke="red"
    d="M 10,30
       A 20,20 0,0,1 50,30
       A 20,20 0,0,1 90,30
       Q 90,60 50,90
       Q 10,60 10,30 z" />
</svg>

d属性中路径的设置有以下几种类型，可以任意组合，空格分隔，最后生成实际的曲线。简单的曲线直接定义，复杂的曲线一般是使用那个其他工具自动生成。

类型  |  参数形式  | 说明 | 实例 
--- | --- | ---  | ---
M | x,y| moveTo，移动到[x,y]| M10,10
|L|x,y|lineTo，绘制一条到[x,y]的直线|L100,10|
|H|x|horizontal，绘制一条到 [x,currentY] 的横线|H100|
|V|y|vertical，绘制一条到 [currentX,y] 的竖线|V100|
|A|rx,ry rotation arc sweep x,y|arc，绘制椭圆弧，参数分别为半径、旋转角度，是否超过180，是否逆时针，终点坐标|A30,50 0 0 1 162.55,162.45|
|Q|x1,y1 x2,x2|quadratic，绘制一条控制点为 [x1,y1]，目标点为 [x2,y2]的二次贝塞尔曲线|L100,10|
|T|x,y|绘制一条目标点为 [x,y]的二次贝塞尔曲线，控制点是当前到目标的中心对称点。|L100,10|
|C|x1,y1 x2,y2 x3,y3|绘制一条目标点为 [x3,y3]，开始控制点为[x1,y1],结束控制点为[x2,y2] 的三次贝塞尔曲线|L100,10|
|S|x1,y1 x2,y2|绘制一条目标点为[x2,y2]，以[x1,y1]和当前点与结束点的中心对称点为控制点的三次贝塞尔曲线|L100,10|
|Z|-|闭合路径|Z|

关于贝塞尔曲线，这里是示意图：
![1](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/B%C3%A9zier_2_big.gif/240px-B%C3%A9zier_2_big.gif)![2](https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/B%C3%A9zier_3_big.gif/240px-B%C3%A9zier_3_big.gif)
如需进一步了解path相关特性，建议参考
[《深度掌握SVG路径path的贝塞尔曲线指令》](https://www.zhangxinxu.com/wordpress/2014/06/deep-understand-svg-path-bezier-curves-command/)
[《MDN-Path—d》](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/d)

## 文本和其他元素
### text文本
`<text>`元素用来绘制文本图形，而且可以将渐变、图案、剪切路径、遮罩或者滤镜应用到text上。属性x，y指定文本图形`左下角`的坐标。注意此时的strok是指文字的线条而不是图形的边框。css中关于文字的相关属性，此处同样有效。
```html
<text x="40" y="40" stroke="#0ff" fill="none" stroke-width="1">text文本</text>
```
<svg width="100" height="50">
<text x="40" y="40" stroke="#0ff" fill="none" stroke-width="1">text文本</text>
</svg>

### foreignObject容器
`<foreignObject>`元素也是一个容器元素，用来在SVG中引入其他XML定义，常用来引入HTML元素。
```html
<foreignObject>
  <p>foreignObject容器</p>
  <ul>
    <li>嵌入HTML</li>
    <li><a>插入超链接</a></li>
  </ul>
</foreignObject>
```
<svg width="300" height="100">
<foreignObject width="300" height="100">
  <p>foreignObject容器</p>
  <ul>
    <li>嵌入HTML</li>
    <li><a>插入超链接</a></li>
  </ul>
</foreignObject>
</svg>


# 实例
由于SVG可以看作是HTML元素，所以可以使用JS和CSS精确控制，同样可以使用在Vue等前端框架中。这里演示一个里程碑的实例。
<div class="landmark-container">
      <svg width="800px" height="320px" style="stroke:#E9EDF0;stroke-linecap: square;stroke-width: 1;fill: none;fill-rule:evenodd;font-size: 14px;word-wrap:break-word;">
      <defs>
      <marker id="arrowEnd" markerWidth="4" markerHeight="4" refX="0" refY="2" orient="auto">
      <path d="M0,0 L4,2 L0,4 z" stroke="#EC4C47" fill="#EC4C47"   stroke-width="2"/>
      </marker>
      <marker id="axisArrow" markerWidth="4" markerHeight="4" refX="0" refY="2" orient="auto" fill="#E9EDF0" stroke-width="0">
      <path d="M0,0 L4,2 L0,4 z" class="axis-arrow"/>
      </marker>
      <marker id="releaseEnd" markerWidth="10" markerHeight="6" refX="0" refY="3" orient="auto">
      <path d="M0,1 L4,3 L0,5 z" fill="#E9EDF0" />
      <path d="M6,0 L6,6" stroke-width="1"/>
      <path d="M8,0 L8,6" stroke-width="1"/>
      </marker>
      </defs>
      <g>
      <path d="M0,150 L780,150" stroke-width="1" class="lane-border"></path>
      <path d="M0,300 L780,300" stroke-width="1" class="lane-border"></path>
      <path d="M0,49 L780,49" stroke-width="4" marker-end="url(#axisArrow)" class="lane-axis"></path>
      <path d="M0,199 L780,199" stroke-width="4" marker-end="url(#axisArrow)" class="lane-axis"></path>
      <path d="M350,199 L350,159 L550,159" stroke-width="4" marker-end="url(#releaseEnd)" class="sublane-axis"/>
      <svg  width="100" height="100" x="400" y="69" class="landmark-item">
        <foreignObject  width="100" height="80">
          <div style="height:80px;position: relative;">
            <div style="position:absolute;bottom:0;">补丁版本P01</div>
          </div>
        </foreignObject>
        <svg y="80">
          <polygon  points="40,10 50,0 60,10 50,20" fill="#fff"></polygon>
          <polygon  points="40,10 50,0 60,10 50,20" style="fill: rgba(71, 184, 129, .3);stroke: #47B881;"></polygon>
        </svg>
      </svg>
      <path d="M100,0 L100,600" id="monthLine-0" stroke-dasharray="1,4"></path>
      <path d="M200,0 L200,600" id="monthLine-1" stroke-dasharray="1,4"></path>
      <path d="M300,0 L300,600" id="monthLine-2" stroke-dasharray="1,4"></path>
      <path d="M400,0 L400,600" id="monthLine-3" stroke-dasharray="1,4"></path>
      <path d="M500,0 L500,600" id="monthLine-4" stroke-dasharray="1,4"></path>
      <path d="M600,0 L600,600" id="monthLine-5" stroke-dasharray="1,4"></path>
      <path d="M700,0 L700,600" id="monthLine-6" stroke-dasharray="1,4"></path>
      <path d="M800,0 L800,600" id="monthLine-7" stroke-dasharray="1,4"></path>
      <g>
      <svg width="100" x="100" y="39" class="landmark-item">
      <svg>
      <polygon points="40,10 50,0 60,10 50,20" fill="#fff"></polygon>
      <polygon points="40,10 50,0 60,10 50,20" style="fill: rgba(71, 184, 129, .3);stroke: #47B881;"></polygon>
      </svg>
      <foreignObject width="100" height="98" x="0" y="20">
      <p class="item-title">前端工程化实践</p>
      </foreignObject>
      </svg>
      <svg width="100" x="300" y="39" class="landmark-item">
      <svg>
      <polygon points="40,10 50,0 60,10 50,20" fill="#fff"></polygon>
      <polygon points="40,10 50,0 60,10 50,20" style="fill: rgba(71, 184, 129, .3);stroke: #47B881;"></polygon>
      </svg>
      <foreignObject width="100" height="98" x="0" y="20">
      <p class="item-title">技术方案验证001</p>
      </foreignObject>
      </svg>
      <svg width="100" x="500" y="39" class="landmark-item">
      <svg>
      <polygon points="40,10 50,0 60,10 50,20" fill="#fff"></polygon>
      <polygon points="40,10 50,0 60,10 50,20" style="fill: rgba(71, 184, 129, .3);stroke: #47B881;"></polygon>
      </svg>
      <foreignObject width="100" height="98" x="0" y="20">
      <p class="item-title">里程碑信息展示</p>
      </foreignObject>
      </svg>
      <svg width="100" x="700" y="39" class="landmark-item">
      <svg>
      <polygon points="40,10 50,0 60,10 50,20" fill="#fff"></polygon>
      <polygon points="40,10 50,0 60,10 50,20" style="fill: rgba(37, 102, 242, .3);stroke: #0067FB;"></polygon>
      </svg>
      <foreignObject width="100" height="98" x="0" y="20">
      <p class="item-title">版本发布计划</p>
      </foreignObject>
      </svg>
      </g>
      <g>
        <svg  width="100" x="200" y="189" class="landmark-item">
          <svg >
            <polygon  points="40,10 50,0 60,10 50,20" fill="#fff"></polygon>
            <polygon  points="40,10 50,0 60,10 50,20" style="fill:rgba(236, 76, 71, .3);stroke:#EC4C47;"></polygon>
          </svg>
          <foreignObject  width="100" height="98" x="0" y="20">
            <p class="item-title">Demo演示环境搭建</p>
          </foreignObject>
        </svg>
        <svg  width="100" x="700" y="189" class="landmark-item">
          <svg ><polygon  points="40,10 50,0 60,10 50,20" fill="#fff"></polygon>
            <polygon  points="40,10 50,0 60,10 50,20" style="fill: rgba(71, 184, 129, .3);stroke: #47B881;"></polygon>
          </svg>
          <foreignObject  width="100" height="98" x="0" y="20">
            <p  class="item-title">测试垂直关联</p>
          </foreignObject>
        </svg>
        <path d="M250,184 C272,122 295,91 340,60" marker-end="url(#arrowEnd)"  stroke="#EC4C47" stroke-width="2"></path>
        <path d="M250,184 C322,122 395,91 540,60" marker-end="url(#arrowEnd)" stroke="#EC4C47" stroke-width="2"></path>
    </svg>
  </div>

# 参考资料
[维基百科——可縮放向量圖形](https://zh.wikipedia.org/wiki/%E5%8F%AF%E7%B8%AE%E6%94%BE%E5%90%91%E9%87%8F%E5%9C%96%E5%BD%A2)
[MDN-SVG](https://developer.mozilla.org/zh-CN/docs/Web/SVG)
[《SVG图像入门教程》——阮一峰](http://www.ruanyifeng.com/blog/2018/08/svg.html)

