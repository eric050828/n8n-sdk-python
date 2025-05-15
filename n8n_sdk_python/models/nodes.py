"""
n8n 節點資料模型。
定義節點相關的資料結構。
"""

from pydantic import Field, validator
from typing import Any, Optional, Union
from .base import N8nBaseModel
from enum import Enum

class NodeType(N8nBaseModel):
    """節點類型基本信息"""
    name: str = Field(..., description="節點類型名稱")
    displayName: str = Field(..., description="顯示名稱")
    icon: Optional[str] = Field(None, description="圖標")
    description: Optional[str] = Field(None, description="描述")
    version: int = Field(1, description="版本")
    group: list[str] = Field(default_factory=list, description="分組")
    codex: Optional[dict[str, Any]] = Field(None, description="Codex 信息")
    defaults: Optional[dict[str, Any]] = Field(None, description="默認值")
    sourcePath: Optional[str] = Field(None, description="源碼路徑")
    supportsCommunityNodes: Optional[bool] = Field(None, description="是否支援社群節點")

class NodePropertyType(str, Enum):
    """節點屬性類型枚舉"""
    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    COLLECTION = "collection"
    FIXED_COLLECTION = "fixedCollection"
    OPTIONS = "options"
    MULTI_OPTIONS = "multiOptions"
    JSON = "json"
    NOTICE = "notice"
    DATE_TIME = "dateTime"
    COLOR = "color"
    CREDENTIAL = "credential"
    RESOURCE_LOCATOR = "resourceLocator"
    RESOURCE_MAPPER = "resourceMapper"

class NodePropertyOptions(N8nBaseModel):
    """節點屬性選項"""
    name: str = Field(..., description="選項名稱")
    displayName: str = Field(..., description="顯示名稱")
    description: Optional[str] = Field(None, description="描述")
    type: NodePropertyType = Field(..., description="屬性類型")
    default: Optional[Any] = Field(None, description="默認值")
    required: Optional[bool] = Field(False, description="是否必填")
    displayOptions: Optional[dict[str, Any]] = Field(None, description="顯示選項")
    options: Optional[list[dict[str, Any]]] = Field(None, description="選項列表")
    placeholder: Optional[str] = Field(None, description="佔位符")
    typeOptions: Optional[dict[str, Any]] = Field(None, description="類型選項")

class NodeTypeDescription(N8nBaseModel):
    """節點類型詳細描述"""
    displayName: str = Field(..., description="顯示名稱")
    name: str = Field(..., description="節點類型名稱")
    group: list[str] = Field(default_factory=list, description="節點分組")
    description: Optional[str] = Field(None, description="節點描述")
    version: int = Field(1, description="節點版本")
    defaults: Optional[dict[str, Any]] = Field(None, description="默認值")
    inputs: Optional[list[str]] = Field(None, description="輸入")
    outputs: Optional[list[str]] = Field(None, description="輸出")
    properties: list[NodePropertyOptions] = Field(default_factory=list, description="節點屬性")
    credentials: Optional[list[dict[str, Any]]] = Field(None, description="節點憑證")
    icon: Optional[str] = Field(None, description="圖標")
    subtitle: Optional[str] = Field(None, description="子標題")
    maxNodes: Optional[int] = Field(None, description="最大節點數量")
    documentationUrl: Optional[str] = Field(None, description="文檔URL")
    codex: Optional[dict[str, Any]] = Field(None, description="Codex 信息")
    sourcePath: Optional[str] = Field(None, description="源碼路徑")
    supportsCommunityNodes: Optional[bool] = Field(None, description="是否支援社群節點")

class NodeParameterOption(N8nBaseModel):
    """節點參數選項"""
    name: str = Field(..., description="選項名稱")
    value: Any = Field(..., description="選項值")
    description: Optional[str] = Field(None, description="選項描述")
    action: Optional[str] = Field(None, description="選項動作")
    routing: Optional[dict[str, Any]] = Field(None, description="路由設定")

class NodeParameterOptions(N8nBaseModel):
    """節點參數可選值"""
    resourceName: Optional[str] = Field(None, description="資源名稱")
    resourceVersion: Optional[str] = Field(None, description="資源版本")
    operation: Optional[str] = Field(None, description="操作名稱")
    properties: dict[str, Any] = Field(default_factory=dict, description="屬性")
    options: list[NodeParameterOption] = Field(default_factory=list, description="選項列表")

class NodeParameterValue(N8nBaseModel):
    """節點參數值"""
    value: Any = Field(..., description="參數值")
    routing: Optional[dict[str, Any]] = Field(None, description="路由設定")

class NodeConnection(N8nBaseModel):
    """節點連接設定"""
    main: Optional[list[list[dict[str, Any]]]] = Field(None, description="主要連接")
    other: Optional[dict[str, list[dict[str, Any]]]] = Field(None, description="其他連接")

class NodeCreateResult(N8nBaseModel):
    """建立節點結果"""
    id: str = Field(..., description="節點 ID")
    name: str = Field(..., description="節點名稱")
    type: str = Field(..., description="節點類型")
    parameters: dict[str, Any] = Field(default_factory=dict, description="節點參數")
    position: dict[str, float] = Field(..., description="節點位置")
    typeVersion: int = Field(1, description="類型版本")

class NodeCreateError(N8nBaseModel):
    """建立節點錯誤"""
    message: str = Field(..., description="錯誤訊息")
    code: str = Field(..., description="錯誤代碼")

class NodeTypeList(N8nBaseModel):
    """節點類型列表"""
    creatorNodes: Optional[list[str]] = Field(None, description="創建者節點")
    nodes: dict[str, NodeTypeDescription] = Field(..., description="節點類型字典")
    count: Optional[int] = Field(None, description="總數")
    nextCursor: Optional[str] = Field(None, description="下一頁游標")

class NodeCreateOptions(N8nBaseModel):
    """節點選項查詢結果"""
    options: dict[str, Any] = Field(..., description="節點選項")

class NodeConnectionOptions(N8nBaseModel):
    """節點連接選項"""
    sourceNode: str = Field(..., description="源節點 ID")
    sourceNodeOutput: Optional[str] = Field(None, description="源節點輸出")
    targetNode: str = Field(..., description="目標節點 ID")
    targetNodeInput: Optional[str] = Field(None, description="目標節點輸入") 