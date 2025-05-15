"""
n8n 專案資料模型。
定義專案相關的資料結構。
"""

from typing import Optional, Any, Dict
from pydantic import Field
from datetime import datetime # 雖然 API 文件範例未顯示時間戳，但通常會有
from .base import N8nBaseModel

class Project(N8nBaseModel):
    """專案資料模型"""
    id: str
    name: str
    type: Optional[str] = Field(None, description="專案類型，API 文件範例中有此欄位，但未詳述") # GET /projects 回應範例中有 type
    createdAt: Optional[datetime] = Field(None, description="創建時間 (推測)")
    updatedAt: Optional[datetime] = Field(None, description="更新時間 (推測)")

class ProjectCreate(N8nBaseModel):
    """建立專案請求模型 (POST /projects)"""
    name: str

class ProjectUpdate(N8nBaseModel):
    """更新專案請求模型 (PUT /projects/{projectId})"""
    name: str

class ProjectList(N8nBaseModel):
    """專案列表響應模型 (GET /projects)"""
    data: list[Project]
    nextCursor: Optional[str] = None