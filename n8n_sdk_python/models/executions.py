from pydantic import Field, validator, RootModel
from typing import Any, Optional, Union
from datetime import datetime
from .base import N8nBaseModel
from enum import Enum

class ExecutionStatus(str, Enum):
    """執行狀態枚舉"""
    ERROR = "error"
    SUCCESS = "success"
    WAITING = "waiting"
    # API 文件中未列出 RUNNING，但通常會有此狀態，暫不添加，按文件為主

class ExecutionData(N8nBaseModel):
    """執行數據"""
    resultData: Optional[dict[str, Any]] = Field(None, description="執行結果數據")
    executionData: Optional[dict[str, Any]] = Field(None, description="執行上下文數據")
    lastNodeExecuted: Optional[str] = Field(None, description="最後執行的節點")
    error: Optional[dict[str, Any]] = Field(None, description="錯誤信息")
    metadata: Optional[dict[str, Any]] = Field(None, description="元數據")

class DataItem(N8nBaseModel, RootModel[dict[str, Any]]):
    """執行數據中的項目"""
    # 根據 GET /executions 和 GET /executions/{id} 的 data 欄位，它是一個物件 {}。
    # 實際結構取決於工作流程，因此使用 dict[str, Any]
    pass

class BinaryDataItem(N8nBaseModel):
    """二進制數據項目"""
    # API 文件未明確定義二進制數據結構，暫時保留
    fileId: str = Field(..., description="文件 ID")
    data: str = Field(..., description="Base64 編碼的數據")
    mimeType: str = Field(..., description="MIME 類型")

class Execution(N8nBaseModel):
    """工作流程執行記錄"""
    id: Union[int, str] # API 文件中 execution id 有時是 int (1000), 有時是 string ("2"), 統一為 Union
    data: Optional[DataItem] = Field(None, description="執行數據，僅在 includeData=true 時包含")
    finished: bool = Field(..., description="是否已完成")
    mode: str = Field(..., description="執行模式 (例如: cli, webhook, manual)")
    retryOf: Optional[Union[int, str]] = Field(None, description="重試自哪個執行 ID") # 同 id
    retrySuccessId: Optional[Union[int, str]] = Field(None, description="重試成功後的執行 ID") # 同 id
    startedAt: datetime = Field(..., description="開始時間")
    stoppedAt: Optional[datetime] = Field(None, description="結束時間")
    workflowId: str = Field(..., description="工作流程 ID")
    # workflowData: Optional[dict[str, Any]] = Field(None, description="工作流程數據，API 文件未明確顯示此欄位在 /executions 回應中")
    waitTill: Optional[datetime] = Field(None, description="等待直到特定時間") # 新增 based on API doc
    customData: Optional[dict[str, Any]] = Field(None, description="自訂數據") # 新增 based on API doc

class ExecutionShort(N8nBaseModel):
    """精簡版執行記錄"""
    id: Union[int, str]
    finished: bool
    mode: str
    retryOf: Optional[Union[int, str]] = None
    retrySuccessId: Optional[Union[int, str]] = None
    startedAt: datetime
    stoppedAt: Optional[datetime] = None
    workflowId: str
    waitTill: Optional[datetime] = None # 新增
    customData: Optional[dict[str, Any]] = None # 新增

class ExecutionList(N8nBaseModel):
    """執行記錄列表"""
    data: list[ExecutionShort] # 或者 Execution，取決於 includeData 參數
    nextCursor: Optional[str] = Field(None, description="下一頁游標")
    # count: Optional[int] = Field(None, description="總數，API 文件未提及")

class ExecutionCreate(N8nBaseModel):
    """觸發工作流程執行請求 (通常是 POST /workflows/{id}/execute 或類似，但 N8N-API.md 沒有此端點，此模型可能用於內部)
       文件中有 POST /executions，但沒有請求體定義，也沒有明確說明用途，暫時不處理此模型。
    """
    # workflow_id: str = Field(..., description="工作流程 ID")
    # run_data: Optional[dict[str, Any]] = Field(None, description="執行數據")
    pass # 根據 API 文件，POST /executions 未定義請求體

# API 文件 GET /executions/{id} (delete) 的回應也是 Execution object
# class ExecutionDeleteResponse(Execution): # 不需要單獨定義，直接用 Execution
#     pass

class ExecutionStopResult(N8nBaseModel):
    """停止執行的結果"""
    success: bool = Field(..., description="是否成功")
    message: Optional[str] = Field(None, description="訊息")

class ExecutionRetryResult(N8nBaseModel):
    """重試執行的結果"""
    executionId: str = Field(..., description="新執行 ID")
    success: bool = Field(..., description="是否成功") 