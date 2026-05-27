const对变量的修饰，C++中和C中的没什么区别
[[指针 函数 常量 易混淆名词#常量 & 指针||看这篇就行了]]

# const修饰class中的函数
在class中函数小括号后面加const，约定该函数不能修改class内非mutable的变量（外部传入的非class变量无const修饰也可以修改）

mutable：跟const一样是个标签，承诺该变量可以修改
```cpp
class Entity
{
	int X, Y;
	mutable int Z;//承诺Z可以修改
public:
	void putX() const
	{
		//X = 2; //错误，不能修改
		Z = 2; //可以修改
		std::cout<< X <<std::endl;
	}
	void SetX()
	{
		X = 2;
		std::cout<< X <<std::endl;
	}
}
void printX(const Entity& e){ //这里传入的是const引用，约定不能修改e，所以SetX不能调用
	e.putX();
	//e.SetX(); //错误，不能修改
}
	

```

再单开一则笔记讲[[引用]]
