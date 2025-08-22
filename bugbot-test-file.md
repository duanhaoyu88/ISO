# Bugbot功能测试文件

## 测试目的
验证Bugbot的代码审查功能是否正常工作

## 测试内容

### 1. 代码质量测试
```javascript
// 这是一个故意包含问题的JavaScript代码示例
function calculateSum(a, b) {
    // 缺少参数验证
    return a + b;  // 可能导致类型错误
}

// 未使用的变量
let unusedVariable = "test";

// 硬编码的魔法数字
const result = calculateSum(10, 20);
```

### 2. 文档质量测试
这个文档包含了一些可能的改进点：
- 缺少详细的函数说明
- 代码示例可以更完整
- 可以添加更多测试用例

### 3. 安全性测试
```python
# 潜在的SQL注入风险
def get_user_data(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    # 应该使用参数化查询
    return execute_query(query)
```

## 预期Bugbot检测的问题
1. 未使用的变量
2. 缺少参数验证
3. 硬编码的魔法数字
4. 潜在的SQL注入风险
5. 缺少文档注释

## 测试结论
此文件用于验证Bugbot是否能正确识别代码质量问题并提供改进建议。
