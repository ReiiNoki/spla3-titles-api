# Splatoon3 随机称号生成 API

## 简介

本项目灵感来源于任天堂著名射击游戏 [斯普拉顿3 (Splatoon3)](https://www.nintendo.com/hk/switch/av5ja/index.html)，游戏中有抽取随机扭蛋获取称号的机制，我将在github找到的称号数据进行提取整合为这个API，欢迎各位使用并提出建议。本项目主要由Fastapi开发并部署在koyeb上，数据库部分则部署在MongoDB Altas上。

## 测试前端

[Splatoon3 Title Generator](https://reiinoki.pythonanywhere.com/)

## API接口

```http
BASE URL = https://ethnic-giulietta-reiinoki-0b7ecf44.koyeb.app/
```
### 1. 获取 **所有语言** 的随机称号

```http
GET /title/
```

**返回示例：**

```json
{
  "title": {
    "adjective": {
      "_id": 863,
      "CNzh": "神清气爽的",
      "EUde": "Luftig-frisch",
      "EUen": "Brisk",
      "EUes": "brios",
      "EUfr": "frisquet",
      "EUit": "brusc",
      "EUnl": "Kras",
      "EUru": "бойк",
      "JPja": "すがすがしい",
      "KRko": "후련한",
      "TWzh": "神清氣爽的",
      "USen": "Brisk",
      "USes": "brusc",
      "USfr": "frisquet"
    },
    "subject": {
      "_id": 230,
      "CNzh": "刺刺头",
      "EUde": "Stachelhaarträger / Stachelhaarträgerin",
      "EUen": "Spiked Hair",
      "EUes": "Chico con cresta / Chica con cresta",
      "EUfr": "Hérisson",
      "EUit": "Spazzolatore / Spazzolatrice",
      "EUnl": "stekelhaardrager",
      "EUru": "еж / ежиха",
      "JPja": "ツンツン",
      "KRko": "삐죽 머리",
      "TWzh": "刺刺頭",
      "USen": "Spiked Hair",
      "USes": "Chico con peinado picudo / Chica con peinado picudo",
      "USfr": "Hérisson"
    }
  }
}
```

### 2. 获取 **指定语言** 的随机称号

```http
GET /title/{lang}
```

例如：

```http
GET /title/zh-CN
```

**返回示例：**

```json
{
    "title": "温泉花大峡谷的 广域标记枪操作者"
}
```

## 鸣谢

- 数据来源 [Splat3](https://github.com/Leanny/splat3)
- ChatGPT

## 未来可能的更新

- 添加其他游戏的称号，比如动物森友会
- 添加单独前缀/后缀抽取（应该没必要吧？）

---

**欢迎 Star ⭐ 和 Fork，本人是新手开发者，感谢issue和指导！** 🎉
