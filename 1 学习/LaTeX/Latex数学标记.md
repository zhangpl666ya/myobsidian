我在obsidian里面下载了一个Latex插件
用两个$产生Latex环境
# 希腊字母表
要打希腊字母，用反斜杠后面接英文拼写，大写的话就给英文拼写首字母大写就好了
有的有变体，需要在前面加var（varible）显示
如： \sigma \Sigma \lambda \Lambda \varLambda演示如下

$$
\sigma \ \Sigma \ \lambda \ \Lambda \ \varLambda 
$$

表查阅：

![[Latex希腊字母表.png]]

# 上下标
上标用^ 后面接上标内容，下标用_后面加下标内容，如果复杂需要用{}括起来
在数学中，只用变量用斜体
对于直立体 用\rm(roman 罗马体) 和 \text体现文本
\text支持空格显示，\rm不支持
\text后面若内容复杂，要用{}括起来，\rm不用（但括起来最好吧）
a^2 \ a_{ij} \ AB \ \text{AB} \ \text{e}^x演示如下:
$$
a^2 \ a_{ij} \ AB \ \text{AB} \ \text{e}^x
$$
# 分式与根式
\frac(fraction)表示分数 ，后面接分子分母。若复杂，用{}括起来
\sqrt(square root)表示根式，n次方在后面用【】括起来
要表现那个分数就写\dfrac
\frac 1 2 \ \frac 1 {(x+y)} \ \frac {\frac 1 x +1}{y+1} \ \frac {\dfrac 1 x +1}{y+1}\\
\sqrt{ x+y }\ \ \sqrt[n]{3+x+x^2  } 效果如下

$$
\frac 1 2 \ \frac 1 {(x+y)} \ \frac {\frac 1 x +1}{y+1} \ \frac {\dfrac 1 x +1}{y+1}\\
\sqrt{ x+y }\ \ \sqrt[n]{3+x+x^2  }
$$

# 运算符
加减正常写
乘\times 
点乘\cdot(centre)
除\div
正负号 \pm(plus-minus) 
负正号\mp
大于等于\ge(greater than or equal)   
小于等于\le(less than or equal)
远大于 \gg   
远小于\ll
不等于\ne(not equal) 
约等于\approx(approximate) 
恒等于\equiv(equivalent)
交集\cap(帽子)
并集\cup(帽子) 
属于\in 
不属于\notin
子集\subseteq 
非子集\subsetneqq 
空集\varnothing
任意\forall 
存在\exists 
不存在\nexists
因为\because   
所以\therefore
\mathbb(blackboard bold) 数集\（字母）
\mathcal(calligraphy)   \mathscr(script)
 $$
+ -\\
\times \\ \cdot \\ 
\pm \\ \mp
\ge \ \le
\ne \ \equiv\\
\cap \ \cup \ \in \ \not\in \\
\subseteq \ \subsetneqq \ \varnothing
\forall \ 
\because \ \therefore
\mathbb R \ \mathcal R \ \mathscr R
$$

省略号：
\cdots \vdots \ddots
$$
\cdots \vdots \ddots
$$
无穷：
\infty(infinity)  \  \partial \  \propto(proportion to)
$$
\infty(infinity)  \  \partial \  \propto(proportion to)
$$

三角：
\sin x \ \sec x \ \cosh s\\
\log_2 x, \ln x \ \lgx
\lim(这里加limits可以将趋近于放到下面)_(x\to 0) \frac{x}{\sin x }
$$
\sin x \ \sec x \ \cosh s\\
\log_2 x, \ln x \ \lg x
\lim_{(x\to 0)} \frac{x}{\sin x }
$$大型运算符：
\sum
\prod
\sum_i,
\sum_(i=0)^ N
\int(integral)
\iint
\iiint
\oint
\int_{-\infty}^ {+\infty} f(x) {\text d}x

$$
\sum
\prod
\sum_i,
\sum_(i=0)^ N
\int
\iint
\iiint
\oint
\int_{-\infty}^ {+\infty} f(s)\, {\text d}x

$$
PS:
间隔怎么表示：
*  a\\,a
* a\\ a
* a\\quad a
* a\\qquad a
* $$
 a\,a
 a\ a
 a\quad a
 a\qquad a
$$

# 标注符号

![[Pasted image 20251113195242.png]]

$$
\vec{ x} ,\ \overrightarrow {AB}\ \
\bar{x}\ \overline{AB} 

$$


箭头
![[Pasted image 20251113195540.png]]

# 括号与定界符
中小括号直接输入 ，大括号已经被占用，要加\转义
\lceil  \rcell \lfloor \rfloor
如果需要括号自适应高度，加\left和\right
没有配对的就用.代替

$$
() \ [] \ \{\}  \ \lceil  \rceil \ \lfloor  \rfloor \ 
(0,\frac{1}{x} ] \quad \left( 0 , \frac{1}{x}\right]
\quad \frac{\partial f}{\partial x}|_{x=0}
\quad \left.\frac{\partial f}{\partial x}\right|_{x=0}
$$

多行公式
用\begin{}构建多行环境，可见多行是右对齐
用&符号对需要的地方对齐
$$
\begin{align}
a=b+c+d \\
=e+f \\
a&= b+c+d \\
&=e+f
\end{align}
$$
大括号
用cases环境
$$
f(x)=
\begin{cases}
\sin x &x<0\\
x^2 ,&x\ge0
\end{cases}
$$
矩阵
matrix环境
bmatrix(bracket 方括号)
pmatrix(parenthesis 圆括号)
vmatrix（vertical 垂直）
一般矩阵都是用加粗黑体表示 \bf(bold face 粗体)
$$
\begin{matrix}
a & b & \cdots & c\\
\vdots & \vdots &\ddots & \vdots\\
e & f & \cdots & g
\end{matrix}
\quad
\begin{bmatrix}  
a & b & \cdots & c\\
\vdots & \vdots &\ddots & \vdots\\
e & f & \cdots & g
\end{bmatrix}
\quad
\begin{pmatrix}
a & b & \cdots & c\\
\vdots & \vdots &\ddots & \vdots\\
e & f & \cdots & g
\end{pmatrix}
\quad
\begin{vmatrix}
a & b & \cdots & c\\
\vdots & \vdots &\ddots & \vdots\\
e & f & \cdots & g
\end{vmatrix}
\ \ 
\bf A^{\mathrm{T}}
$$