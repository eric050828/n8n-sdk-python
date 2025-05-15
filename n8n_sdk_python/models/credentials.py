from pydantic import Field, validator, RootModel
from typing import Any, Optional, Union
from datetime import datetime
from .base import N8nBaseModel



class CredentialType(N8nBaseModel):
    """憑證類型基本信息"""
    id: str = Field(..., description="憑證類型 ID (非標準API)")
    name: str = Field(..., description="憑證類型名稱 (非標準API)")
    displayName: Optional[str] = Field(None, description="顯示名稱 (非標準API)")

class CredentialDataSchemaResponse(N8nBaseModel):
    type: str
    properties: dict[str, Any] # Can be more specific if property structure is known
    required: Optional[list[str]] = None
    additionalProperties: Optional[Union[bool, dict[str, Any]]] = None # As per OpenAPI spec

class CredentialTransferRequest(N8nBaseModel):
    """憑證轉移請求模型 (對應 PUT /credentials/{id}/transfer)"""
    destinationProjectId: str

# CredentialTypeList, CredentialTypeDescription, NodeAccess, CredentialSharing, CredentialTypeProperty
# 這些模型在 N8N-API.md 中沒有找到直接對應的 API 端點，可能是舊版、內部使用或特定 UI 需求。

class NodeAccess(N8nBaseModel):
    """節點訪問配置"""
    nodeType: str = Field(..., description="節點類型")
    date: Optional[Union[str, datetime]] = Field(None, description="訪問日期")

class CredentialTypeProperty(N8nBaseModel):
    """憑證類型屬性"""
    name: str = Field(..., description="屬性名稱")
    displayName: str = Field(..., description="顯示名稱")
    type: str = Field(..., description="數據類型")
    default: Optional[Any] = Field(None, description="默認值")
    required: Optional[bool] = Field(False, description="是否必填")
    description: Optional[str] = Field(None, description="描述")
    placeholder: Optional[str] = Field(None, description="佔位符文本")
    options: Optional[list[dict[str, Any]]] = Field(None, description="選項")
    typeOptions: Optional[dict[str, Any]] = Field(None, description="類型選項")

class CredentialTypeDescription(N8nBaseModel):
    """憑證類型描述"""
    name: str = Field(..., description="類型名稱")
    displayName: str = Field(..., description="顯示名稱")
    description: Optional[str] = Field(None, description="類型描述")
    icon: Optional[str] = Field(None, description="圖標")
    documentationUrl: Optional[str] = Field(None, description="文檔URL")
    properties: list[CredentialTypeProperty] = Field(default_factory=list, description="憑證屬性")
    required: Optional[list[str]] = Field(None, description="必填屬性列表")
    authenticate: Optional[dict[str, Any]] = Field(None, description="認證設置")

class CredentialData(N8nBaseModel, RootModel[dict[str, Any]]):
    """憑證數據"""
    pass

class CredentialListItem(N8nBaseModel):
    """憑證列表項"""
    id: str = Field(..., description="憑證 ID")
    name: str = Field(..., description="憑證名稱")
    type: str = Field(..., description="憑證類型")
    nodesAccess: list[NodeAccess] = Field(default_factory=list, description="允許訪問的節點類型")
    createdAt: Union[str, datetime] = Field(..., description="創建時間")
    updatedAt: Union[str, datetime] = Field(..., description="更新時間")
    sharedWith: Optional[list[dict[str, Any]]] = Field(None, description="共享用戶")

class CredentialDetail(CredentialListItem):
    """憑證詳情"""
    data: Optional[CredentialData] = Field(None, description="憑證數據")

class CredentialTestResult(N8nBaseModel):
    """憑證測試結果"""
    status: str = Field(..., description="測試狀態")
    message: Optional[str] = Field(None, description="測試訊息")

class CredentialSharing(N8nBaseModel):
    """憑證共享設置"""
    user: Optional[dict[str, Any]] = Field(None, description="共享用戶信息")
    role: Optional[str] = Field(None, description="角色權限")
    date: Optional[Union[str, datetime]] = Field(None, description="共享日期")

class CredentialShort(N8nBaseModel):
    """憑證簡短信息（列表用）"""
    id: str = Field(..., description="憑證 ID")
    name: str = Field(..., description="憑證名稱")
    type: str = Field(..., description="憑證類型")
    nodesAccess: Optional[list[NodeAccess]] = Field(None, description="允許訪問的節點類型")
    createdAt: Union[str, datetime] = Field(..., description="創建時間")
    updatedAt: Union[str, datetime] = Field(..., description="更新時間")
    sharedWith: Optional[list[CredentialSharing]] = Field(None, description="共享用戶")

class Credential(CredentialShort):
    """憑證詳細信息"""
    data: dict[str, Any] = Field(default_factory=dict, description="憑證數據")
    ownedBy: Optional[dict[str, Any]] = Field(None, description="擁有者信息")

class CredentialCreate(N8nBaseModel):
    """創建憑證的請求模型"""
    name: str = Field(..., description="憑證名稱")
    type: str = Field(..., description="憑證類型")
    data: dict[str, Any] = Field(default_factory=dict, description="憑證數據")
    nodesAccess: Optional[list[NodeAccess]] = Field(None, description="允許訪問的節點")
    sharedWith: Optional[list[dict[str, Any]]] = Field(None, description="共享設置")

class CredentialUpdate(N8nBaseModel):
    """更新憑證的請求模型"""
    name: Optional[str] = Field(None, description="憑證名稱")
    data: Optional[dict[str, Any]] = Field(None, description="憑證數據")
    nodesAccess: Optional[list[NodeAccess]] = Field(None, description="允許訪問的節點")
    sharedWith: Optional[list[dict[str, Any]]] = Field(None, description="共享設置")

class CredentialTest(N8nBaseModel):
    """憑證測試結果"""
    credential_id: str = Field(..., description="憑證 ID")
    success: bool = Field(..., description="測試是否成功")
    message: Optional[str] = Field(None, description="測試結果消息")
    details: Optional[dict[str, Any]] = Field(None, description="詳細信息")

class CredentialTypeList(N8nBaseModel):
    """憑證類型列表"""
    count: int = Field(..., description="憑證類型數量")
    types: dict[str, CredentialTypeDescription] = Field(default_factory=dict, description="憑證類型字典")