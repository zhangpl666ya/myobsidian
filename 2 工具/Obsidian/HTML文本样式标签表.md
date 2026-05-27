
|分类|标签|核心功能|语法示例|效果展示|扩展用法（CSS 调整）|
|---|---|---|---|---|---|
|基础样式|`<b>`|文字加粗（无语义，仅样式）|`<b>加粗文本</b>`|<b>加粗文本</b>|`<b style="color: blue;">蓝色加粗</b>` → <b style="color: blue;">蓝色加粗</b>|
|基础样式|`<i>`|文字斜体（可表强调或特殊文本）|`<i>斜体文本</i>`|<i>斜体文本</i>|`<i style="font-size: 18px;">放大斜体</i>` → <i style="font-size: 18px;">放大斜体</i>|
|基础样式|`<u>`|文字下划线|`<u>下划线文本</u>`|下划线文本|`<u style="text-decoration: underline red dashed;">红色虚线下划线</u>` → 红色虚线下划线|
|强调与标记|`<s>`|文字删除线（表废弃内容）|`<s>已废弃的文本</s>`|<s>已废弃的文本</s>|`<s style="text-decoration-color: #999;">灰色删除线</s>` → <s style="text-decoration-color: #999;">灰色删除线</s>|
|强调与标记|`<mark>`|文字背景高亮（表重点）|`<mark>重点高亮文本</mark>`|<mark>重点高亮文本</mark>|`<mark style="background-color: #ffeb3b;">黄色高亮</mark>` → <mark style="background-color: #ffeb3b;">黄色高亮</mark>|
|特殊格式|`<sup>`|上标（如公式、引用标注）|`X<sup>2</sup>`（平方）、`参考<sup>[1]</sup>`|X<sup>2</sup>、参考<sup>[1]</sup>|无额外调整需求，多用于数学公式或文献引用|
|特殊格式|`<sub>`|下标（如化学公式）|`H<sub>2</sub>O`（水）|H<sub>2</sub>O|无额外调整需求，常见于化学符号或脚注标记|

### 注意事项

1. **兼容性**：以上标签在 99% 的 Markdown 编辑器（如 Typora、VS Code、GitHub）和浏览器中都能正常显示，仅极简编辑器可能限制 CSS 扩展用法。
2. **语义优先**：如果需要强调 “重要性” 而非单纯改样式，优先用 `<strong>`（替代 `<b>`）、`<em>`（替代 `<i>`），比如 `<strong>警告内容</strong>`，对阅读辅助工具更友好。



虽然 `<u>` 本身除标记下划线外没有其他功能，但可以通过搭配 **CSS 样式**，让它的下划线呈现不同效果（比如改颜色、变虚线），满足更多场景需求。以下是几个常见示例：

1. **修改下划线颜色**
    
    给 `<u>` 标签加 `style` 属性，指定下划线颜色：
    
    html
    
    Preview
    
    ```html
    <u style="text-decoration-color: red;">红色下划线文字</u>
    ```
    
    效果：<u style="text-decoration-color: red;">红色下划线文字</u>
    
2. **改成虚线 / 点线下划线**
    
    调整 `text-decoration-style` 属性，改变下划线样式：
    
    html
    
    Preview
    
    ```html
    <u style="text-decoration-style: dashed;">虚线下划线</u>
    <u style="text-decoration-style: dotted;">点线下划线</u>
    ```
    
    效果：<u style="text-decoration-style: dashed;">虚线下划线</u>/<u style="text-decoration-style: dotted;">点线下划线</u>
    
3. **加粗下划线**
    
    通过 `text-decoration-thickness` 调整下划线粗细：
    
    html
    
    Preview
    
    ```html
    <u style="text-decoration-thickness: 2px;">粗下划线文字</u>
    ```
    
    效果：<u style="text-decoration-thickness: 2px;">粗下划线文字</u>