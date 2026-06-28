# CTLoom

> 终端原生 AI 编程助手 — ReAct + Plan Mode 双引擎驱动，支持多 Agent 协作、MCP 工具扩展、跨会话记忆

Terminal-native AI coding assistant with ReAct + Plan Mode dual-engine, multi-agent collaboration, MCP tool extension, and cross-session memory.

## 特性 / Features

- **双模式引擎 / Dual-Mode Engine** — ReAct 推理循环 + Plan Mode 结构化规划
- **多 LLM 协议 / Multi-LLM** — Anthropic 与 OpenAI 双协议统一为内部流式事件接口，新增后端仅需一个适配器
- **MCP 工具延迟加载 / MCP Tool Lazy Loading** — 按需实例化，百级工具场景下工具定义 Token 占用降低约 85%
- **两层渐进压缩 / Two-Layer Context Compression** — Layer1 超限结果落盘 + Layer2 LLM 摘要 + 熔断保护，支撑数小时连续会话
- **纵深权限管控 / Five-Layer Permission Model** — 工具类别 × 权限模式矩阵 + 多级拦截链，任一层拒绝即终止
- **自动记忆提取 / Auto Memory Extraction** — LLM 分析对话自动沉淀结构化记忆，跨会话自动继承
- **多 Agent 协作 / Multi-Agent Collaboration** — Coordinator-Worker 模式 + Git Worktree 文件隔离

## 快速开始 / Quick Start

### 环境要求 / Prerequisites

- Python >= 3.11
- [uv](https://docs.astral.sh/uv/)（推荐）或 pip

### 安装 / Installation

```bash
git clone https://github.com/Nature-Porter/CTLoom.git
cd CTLoom

uv pip install -e .
```

### 配置 / Configuration

复制示例配置文件并编辑：

```bash
cp config.yaml.example config.yaml
```

设置 API 密钥：

```bash
export ANTHROPIC_API_KEY=sk-ant-...
# 或
export OPENAI_API_KEY=sk-...
```

### 运行 / Run

```bash
mewcode
```

## 项目结构 / Project Structure

```
mewcode/
├── agent.py            # 核心 Agent 循环（ReAct + Plan Mode）
├── app.py              # 终端 UI（Textual）
├── driver.py           # 引擎驱动，编排 Agent ↔ 工具 ↔ LLM
├── conversation.py     # 消息历史 & Token 估算
├── context/            # 两层上下文压缩
├── tools/              # 内置工具实现
├── mcp/                # MCP 协议客户端 & 延迟加载包装器
├── teams/              # 多 Agent 协作
├── hooks/              # 生命周期钩子引擎
├── memory/             # 跨会话自动记忆
├── permissions/        # 权限检查器 & 规则
├── skills/             # Skill 技能加载器 & 执行器
├── commands/           # 斜杠命令处理器
├── sandbox/            # 沙箱执行
└── worktree/           # Git Worktree 隔离
```

## 许可证 / License

MIT
