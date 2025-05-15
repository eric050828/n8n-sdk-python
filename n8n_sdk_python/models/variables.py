"""
n8n 變數資料模型。
定義工作流程變數相關的資料結構。
"""

from typing import Optional, Any, Union
from enum import Enum
from datetime import datetime
from pydantic import Field

from .base import N8nBaseModel


class VariableType(str, Enum):
    """變數類型枚舉"""
    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    JSON = "json"


class Variable(N8nBaseModel):
    """變數資料模型"""
    id: str
    key: str
    value: Any
    type: Optional[VariableType] = Field(default=VariableType.STRING, description="變數類型")
    description: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class VariableCreate(N8nBaseModel):
    """建立變數請求模型"""
    key: str = Field(..., description="變數的鍵")
    value: str = Field(..., description="變數的值 (API 文件指定為 string)")


class VariableUpdate(N8nBaseModel):
    """更新變數請求模型"""
    key: Optional[str] = None
    value: Optional[Any] = None
    type: Optional[VariableType] = None
    description: Optional[str] = None


class VariablesList(N8nBaseModel):
    """變數列表響應模型"""
    data: list[Variable]
    nextCursor: Optional[str] = None
    count: Optional[int] = None 