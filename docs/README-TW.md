# n8n-sdk-python

這是 n8n 工作流自動化平台的非官方 Python SDK。此 SDK 提供了與 n8n API 進行交互的方便包裝器，使您能夠從 Python 應用程序中管理工作流、執行、憑證和其他 n8n 資源。

## 目錄
- [系統需求](#系統需求)
- [安裝方法](#安裝方法)
- [初始設置](#初始設置)
- [快速開始](#快速開始)
- [問題排解](#問題排解)
- [貢獻](#貢獻)
- [授權](#授權)

## 系統需求

在安裝 n8n-sdk-python 之前，請確保您的系統滿足以下要求：

- Python 3.8 或更高版本
- 正在運行的 n8n 實例（本地或遠程）
- n8n API 金鑰（用於認證）

## 安裝方法

### 使用虛擬環境

使用虛擬環境可以避免依賴衝突：

```bash
# 創建虛擬環境
python -m venv venv

# 啟動虛擬環境
# 在 Windows 上
venv\Scripts\activate
# 在 macOS/Linux 上
source venv/bin/activate
```

### 方法 1：使用 pip（推薦）

最簡單的安裝方式是使用 pip 包管理器：

```bash
pip install n8n-sdk-python
```

### 方法 2：從源碼安裝

如果您需要最新的開發版本或者想要修改代碼，可以從源碼安裝：

```bash
# 克隆存儲庫
git clone https://github.com/eric050828/n8n-sdk-python.git
cd n8n-sdk-python

# 安裝開發模式
pip install -e .
```

## 初始設置

安裝完成後，您需要進行一些初始設置才能使用 SDK。

### 獲取 n8n API 金鑰

1. 登錄到您的 n8n 實例。
2. 點擊右上角的用戶圖標，選擇「設置」。
3. 點擊「API」選項卡。
4. 點擊「創建」按鈕生成一個新的 API 金鑰。
5. 複製生成的 API 金鑰（請注意保存，因為它只會顯示一次）。

### 設置環境變數

您可以通過環境變數來配置 SDK，這樣就不需要在代碼中硬編碼敏感信息：

#### 在 Linux/macOS 上

```bash
export N8N_BASE_URL="http://localhost:5678"
export N8N_API_KEY="your-api-key-here"
```

#### 在 Windows 上

```bash
set N8N_BASE_URL=http://localhost:5678
set N8N_API_KEY=your-api-key-here
```

#### 使用 .env 文件

對於項目開發，建議使用 `.env` 文件來管理環境變數：

1. 創建一個名為 `.env` 的文件在您的項目根目錄中。
2. 添加以下內容：

```
N8N_BASE_URL=http://localhost:5678
N8N_API_KEY=your-api-key-here
```

3. 在您的程式中載入這些設置：

```python
from dotenv import load_dotenv
import os

# 載入 .env 文件中的環境變數
load_dotenv()

# 現在可以使用 os.getenv 獲取環境變數
base_url = os.getenv("N8N_BASE_URL")
api_key = os.getenv("N8N_API_KEY")
```

請注意，您需要安裝 `python-dotenv` 庫才能使用此功能：`pip install python-dotenv`

## 快速開始

安裝完成後，您可以運行以下代碼來驗證 SDK 是否正常工作：

```python
import asyncio
from n8n_sdk_python import N8nClient
from n8n_sdk_python.models.workflows import WorkflowList

async def test_connection():
    # 初始化客戶端
    client = N8nClient(
        base_url="http://localhost:5678",  # 替換為您的 n8n 實例 URL
        api_key="your-api-key-here"  # 替換為您的 API 金鑰
    )
    
    try:
        # 嘗試獲取工作流列表
        workflows: WorkflowList = await client.list_workflows(limit=1)
        print("✅ 連接成功！找到工作流數量:", len(workflows.data))
        return True
    except Exception as e:
        print("❌ 連接失敗:", str(e))
        return False

if __name__ == "__main__":
    result = asyncio.run(test_connection())
    print("測試結果:", "成功" if result else "失敗")
```

## 問題排解

如果您遇到問題，以下是一些常見問題及其解決方案：

### 安裝問題

**問題：** 安裝時出現 "ERROR: Could not find a version that satisfies the requirement n8n-sdk-python"

**解決方案：** 檢查 Python 版本是否滿足要求（3.8+），並確保 pip 已更新到最新版本：

```bash
python --version
pip install --upgrade pip
```

### 連接問題

**問題：** 連接到 n8n 實例時出現 "Connection refused" 錯誤

**解決方案：** 
- 確認 n8n 實例是否正在運行
- 檢查 URL 是否正確，包括協議（http/https）和端口
- 確認沒有防火牆阻止連接

**問題：** 收到 401 Unauthorized 錯誤

**解決方案：** 
- 確認 API 金鑰是否正確
- 檢查 API 金鑰是否已過期或被撤銷
- 驗證用戶是否有足夠的權限

### 導入問題

**問題：** 出現 "ModuleNotFoundError: No module named 'n8n_sdk_python'"

**解決方案：** 
- 確認庫已正確安裝：`pip list | grep n8n-sdk-python`
- 如果使用虛擬環境，確認已激活：`which python`
- 嘗試重新安裝：`pip install --force-reinstall --no-cache-dir n8n-sdk-python`

### 其他問題

如果您遇到其他問題，可以：

1. 檢查日誌輸出以獲取詳細錯誤信息
2. 啟用調試模式獲取更多日誌：

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

3. 在 GitHub 存儲庫上提交 issue，附上錯誤詳情和重現步驟 