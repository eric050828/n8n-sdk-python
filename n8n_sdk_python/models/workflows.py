"""
n8n 工作流程資料模型。
定義工作流程相關的資料結構。
"""

from pydantic import Field, validator, RootModel
from typing import Any, Optional
from datetime import datetime
from .base import N8nBaseModel

class NodeParameter(N8nBaseModel, RootModel[dict[str, Any]]):
    """節點參數，允許任意結構"""
    pass

class Connection(N8nBaseModel):
    """節點之間的連接"""
    node: str = Field(..., description="目標節點名稱")
    type: str = Field("main", description="連接類型")
    index: int = Field(0, description="輸入索引")

class NodeConnection(N8nBaseModel):
    """節點的連接集合"""
    main: Optional[list[list[Connection]]] = Field(None, description="主要連接")

class NodeCredential(N8nBaseModel):
    """節點憑證引用"""
    id: Optional[str] = Field(None, description="憑證 ID")
    name: str = Field(..., description="憑證名稱")

class Node(N8nBaseModel):
    """工作流程中的節點"""
    id: str = Field(..., description="節點唯一 ID")
    name: str = Field(..., description="節點名稱")
    type: str = Field(..., description="節點類型")
    typeVersion: int | float = Field(1, description="節點類型版本")
    position: list[float] = Field(..., description="節點位置坐標 [x, y]")
    parameters: dict[str, Any] = Field(default_factory=dict, description="節點參數")
    credentials: Optional[dict[str, NodeCredential]] = Field(
        None, description="節點使用的憑證"
    )
    disabled: Optional[bool] = Field(None, description="節點是否被禁用")
    notes: Optional[str] = Field(None, description="節點註釋")
    webhookId: Optional[str] = Field(None, description="Webhook ID")
    notesInFlow: Optional[bool] = Field(None, description="是否在流程中顯示註釋")
    executeOnce: Optional[bool] = Field(None, description="是否僅執行一次")
    onError: Optional[str] = Field(None, description="錯誤處理方式")
    continueOnFail: Optional[bool] = Field(None, description="失敗時是否繼續")
    alwaysOutputData: Optional[bool] = Field(None, description="始終輸出數據")
    retryOnFail: Optional[bool] = Field(None, description="失敗時是否重試")
    maxTries: Optional[int] = Field(None, description="最大重試次數")
    waitBetweenTries: Optional[int] = Field(None, description="重試間隔（毫秒）")
    createdAt: Optional[datetime] = Field(None, description="創建時間")
    updatedAt: Optional[datetime] = Field(None, description="更新時間")

class WorkflowSettings(N8nBaseModel):
    """工作流程設置"""
    saveExecutionProgress: Optional[bool] = Field(None, description="是否保存執行進度")
    saveDataErrorExecution: Optional[str] = Field(None, description="保存錯誤執行數據")
    saveDataSuccessExecution: Optional[str] = Field(None, description="保存成功執行數據")
    saveManualExecutions: Optional[bool] = Field(None, description="是否保存手動執行")
    executionTimeout: Optional[int] = Field(None, description="執行超時時間（秒）")
    callerPolicy: Optional[str] = Field(None, description="調用者策略")
    timezone: Optional[str] = Field(None, description="時區")
    errorWorkflow: Optional[str] = Field(None, description="錯誤工作流程 ID")
    executionOrder: Optional[str] = Field(None, description="執行順序 (v1)")

class Tag(N8nBaseModel):
    """標籤"""
    id: str = Field(..., description="標籤 ID")
    name: str = Field(..., description="標籤名稱")
    createdAt: Optional[datetime] = Field(None, description="創建時間")
    updatedAt: Optional[datetime] = Field(None, description="更新時間")

class TagList(N8nBaseModel):
    """標籤列表響應模型"""
    data: list[Tag] = Field(..., description="標籤列表")
    nextCursor: Optional[str] = Field(None, description="下一頁游標")
    count: Optional[int] = Field(None, description="總數")
    
class WorkflowStaticData(N8nBaseModel):
    lastId: Optional[int] = None
    # Add other fields if necessary based on actual staticData structure

class Workflow(N8nBaseModel):
    """工作流程完整模型"""
    id: str = Field(..., description="工作流程 ID")
    name: str = Field(..., description="工作流程名稱")
    active: bool = Field(False, description="工作流程是否啟用")
    connections: dict[str, dict[str, list[list[Connection]]]] = Field(
        default_factory=dict, description="節點之間的連接，鍵為來源節點名稱，值為輸出端口到目標連接列表的列表"
    )
    nodes: list[Node] = Field(default_factory=list, description="工作流程中的節點集合")
    settings: Optional[WorkflowSettings] = Field(None, description="工作流程設置")
    tags: Optional[list[Tag]] = Field(None, description="工作流程標籤")
    pinData: Optional[dict[str, Any]] = Field(None, description="固定數據")
    staticData: Optional[WorkflowStaticData | dict[str, Any]] = Field(None, description="靜態數據")
    versionId: Optional[str] = Field(None, description="版本 ID")
    meta: Optional[dict[str, Any]] = Field(None, description="元數據")
    updatedAt: Optional[datetime] = Field(None, description="更新時間")
    createdAt: Optional[datetime] = Field(None, description="創建時間")

class WorkflowShort(N8nBaseModel):
    """工作流程簡短信息（列表用）"""
    id: str = Field(..., description="工作流程 ID")
    name: str = Field(..., description="工作流程名稱")
    active: bool = Field(False, description="工作流程是否啟用")
    createdAt: Optional[datetime] = Field(None, description="創建時間")
    updatedAt: Optional[datetime] = Field(None, description="更新時間")
    tags: Optional[list[Tag]] = Field(None, description="工作流程標籤")

class WorkflowList(N8nBaseModel):
    """工作流程列表響應模型"""
    data: list[WorkflowShort] = Field(..., description="工作流程列表")
    nextCursor: Optional[str] = Field(None, description="下一頁游標")
    count: Optional[int] = Field(None, description="總數")

class WorkflowCreate(N8nBaseModel):
    """創建工作流程的請求模型"""
    name: str = Field(..., description="工作流程名稱")
    nodes: list[Node] = Field(default_factory=list, description="節點集合")
    connections: dict[str, dict[str, list[list[Connection]]]] = Field(
        default_factory=dict, description="節點連接，鍵為來源節點名稱"
    )
    settings: Optional[WorkflowSettings] = Field(None, description="工作流程設置")
    staticData: Optional[WorkflowStaticData | dict[str, Any]] = Field(None, description="靜態數據")

class WorkflowUpdate(N8nBaseModel):
    """更新工作流程的請求模型"""
    name: Optional[str] = Field(None, description="工作流程名稱")
    active: Optional[bool] = Field(None, description="工作流程是否啟用")
    nodes: Optional[list[Node]] = Field(None, description="節點集合")
    connections: Optional[dict[str, dict[str, list[list[Connection]]]]] = Field(None, description="節點連接，鍵為來源節點名稱")
    settings: Optional[WorkflowSettings] = Field(None, description="工作流程設置")
    staticData: Optional[WorkflowStaticData | dict[str, Any]] = Field(None, description="靜態數據")

class WorkflowTransferRequest(N8nBaseModel):
    """工作流程轉移請求模型"""
    destinationProjectId: str

class WorkflowTagUpdateRequestItem(N8nBaseModel):
    """更新工作流程標籤請求中的單個標籤項目"""
    id: str

# WorkflowRunResult 模型似乎與 API 文件中的任何特定端點回應都不直接對應，可能是自訂的或舊版
class WorkflowRunResult(N8nBaseModel):
    """工作流程執行結果"""
    executionId: str = Field(..., description="執行 ID")
    data: Optional[dict[str, Any]] = Field(None, description="執行數據")
