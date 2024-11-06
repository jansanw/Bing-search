# 必应搜索 API 文档

## 概述
本 API 允许用户通过发送搜索请求抓取必应搜索引擎的相关内容及智能回答结果。用户可以按关键词进行搜索，并获得一个结构化的响应。

## 接口信息

- **请求类型**: POST
- **请求 URL**: `http://127.0.0.1:10000/search`

## 请求参数
### Body 参数 (application/json)

| 参数名 | 类型   | 必需   | 描述               |
|--------|--------|--------|--------------------|
| query  | string | 是     | 搜索关键词         |

### 示例
```json
{
  "query": "小米15详细信息"
}
```

## 响应

### 成功响应

- **HTTP 状态码**: 200
- **内容格式**: JSON (application/json)

#### 数据结构

| 属性名         | 类型      | 必需   | 描述                                   |
|----------------|-----------|--------|----------------------------------------|
| data           | object    | 是     | 结果数据                               |
| ├─ Interlocution | string   | 是     | 智能回答内容                           |
| └─ Search Results | array[object] | 是 | 搜索结果列表，包含多个结果           |

### 示例响应
```json
{
  "data": {
    "Interlocution": "Encrypted Client Hello (ECH) 是 Firefox 和一些主流浏览器的一个安全功能。",
    "Search Results": [
      {
        "description": "环氧氯丙烷（ech）是一个有机氯化合物，也是一个环氧化物。",
        "link": "https://zh.wikipedia.org/wiki/%E7%8E%AF%E6%B0%A7%E6%B0%AF%E4%B8%99%E7%83%B7",
        "title": "环氧氯丙烷 - 维基百科，自由的百科全书"
      },
      {
        "description": "该化合物用于制造甘油、塑料和人造橡胶。",
        "link": "https://www.chembk.com/cn/chem/ECH",
        "title": "ECH_化工百科 - ChemBK"
      }
    ]
  }
}
```

## 错误处理
在请求过程中，如果出现错误，将返回相应的 HTTP 状态码及错误信息。确保根据状态码进行适当处理。

--- 

希望本 API 文档能够帮助您有效地使用必应搜索引擎的抓取功能。
