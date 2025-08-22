// Bugbot JavaScript测试文件
// 故意包含各种代码问题

// 1. 未使用的变量
let unusedVariable = "test";

// 2. 缺少参数验证的函数
function calculateSum(a, b) {
    return a + b; // 可能导致类型错误
}

// 3. 硬编码的魔法数字
const result = calculateSum(10, 20);

// 4. 潜在的内存泄漏
class EventHandler {
    constructor() {
        this.events = [];
    }
    
    addEvent(event) {
        this.events.push(event);
        // 缺少事件清理机制
    }
    
    // 没有清理方法
}

// 5. 异步处理问题
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.log(error); // 应该使用更详细的错误处理
    }
}

// 6. 性能问题：不必要的重复计算
function processArray(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            // O(n²) 复杂度，可能性能问题
            console.log(arr[i] + arr[j]);
        }
    }
}

// 7. 代码风格问题
function badFunctionName() { // 应该使用camelCase
    let x=1+2; // 缺少空格
    if(x==3) { // 缺少空格
        console.log("x is 3");
    }
    return x;
}

// 8. 潜在的安全问题
function getUserData(userId) {
    const query = `SELECT * FROM users WHERE id = ${userId}`; // SQL注入风险
    return executeQuery(query);
}

// 9. 缺少类型注解（如果使用TypeScript）
function processUser(user) {
    return user.name + user.age; // 可能类型错误
}

// 10. 死代码
if (false) {
    console.log("This will never execute");
}

// 导出函数供测试
module.exports = {
    calculateSum,
    EventHandler,
    fetchData,
    processArray,
    badFunctionName,
    getUserData,
    processUser
};
