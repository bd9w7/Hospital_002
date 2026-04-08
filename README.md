# 医院智能挂号与叫号系统

## 项目信息
- 课程：COMP2090SEF
- 小组成员：LI Xuanyi (13640692), FAN Lingwen (13651866), HE Zhixun (13568063)
- 提交日期：2026年4月12日

## 项目结构
- `Task1_OOP/`：OOP 医院管理系统，包含 GUI 及核心业务逻辑
- `Task2_SelfStudy/`：自学数据结构和算法（最小堆、鸡尾酒排序）及测试

## 运行指南
1. 确保 Python 3.x 环境
2. 进入 `Task1_OOP/` 目录，执行 `python main.py`
3. GUI 启动后可进行注册、叫号、撤销、搜索、排序等操作
4. 测试自学部分：进入 `Task2_SelfStudy/` 执行 `python test.py`

## 核心功能
- 患者注册（支持紧急/普通，优先级 1~5）
- 智能叫号：紧急患者基于最小堆优先，普通患者队列
- 操作撤销：支持撤销注册和叫号（栈 + BST 删除 + 堆/队列恢复）
- 患者搜索：基于 BST 的 PID 快速查找
- 多维度排序：按年龄（冒泡）、PID（选择）、姓名（归并）、优先级（鸡尾酒排序）
- 就诊历史记录（链表）
- 友好的 Tkinter GUI

## OOP 概念体现
- 封装：所有属性私有，提供 getter/setter
- 继承：`Patient` 继承 `Person` 抽象基类
- 多态：`Sorter` 抽象类，不同排序算法实现统一 `sort()` 接口
- 抽象：`Person` 类含抽象方法 `get_info()`

## 自学部分
- 最小堆（MinHeap）：用于紧急患者优先队列，时间复杂度 O(log n)
- 鸡尾酒排序（Cocktail Sort）：双向冒泡排序，用于按优先级排序患者

## 演示视频
[点击观看 5 分钟演示视频](https://your-video-link.com)

## 引用声明
本项目为原创，未使用外部代码。GUI 使用 Python 标准库 tkinter。