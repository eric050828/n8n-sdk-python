"""
n8n 用戶資料模型。
定義用戶相關的資料結構。
"""

from typing import Optional, Any, Union
from enum import Enum
from datetime import datetime, timezone
from pydantic import Field

from .base import N8nBaseModel


class UserRole(str, Enum):
    """用戶角色枚舉"""
    GLOBAL_OWNER = "global:owner"
    GLOBAL_ADMIN = "global:admin"
    GLOBAL_MEMBER = "global:member"
    OWNER = "owner"
    ADMIN = "admin"
    EDITOR = "editor"
    DEFAULT = "default"


class AuthenticatedUser(N8nBaseModel):
    """已認證用戶資料模型"""
    id: str
    email: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    fullName: Optional[str] = None
    password: Optional[str] = None
    isOwner: bool = False
    isPending: bool = False
    signInType: Optional[str] = None
    role: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    settings: Optional[dict[str, Any]] = None
    globalRole: UserRole = UserRole.GLOBAL_MEMBER
    authenticationMethod: Optional[str] = None


class User(N8nBaseModel):
    """用戶資料模型"""
    id: str
    email: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    isOwner: bool = False
    isPending: bool = False
    signInType: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    role: Optional[UserRole] = None
    inviteAcceptUrl: Optional[str] = None
    emailSent: Optional[bool] = None


class UserShort(N8nBaseModel):
    """精簡版用戶資料模型"""
    id: str
    email: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None


class UserCreate(N8nBaseModel):
    """建立用戶請求模型"""
    email: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    role: Optional[UserRole] = None
    password: Optional[str] = None


class UserCreateItem(N8nBaseModel):
    """建立用戶請求中的單個用戶項目"""
    email: str
    role: Optional[UserRole] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None


class UserCreateResponseItem(N8nBaseModel):
    """建立用戶響應中的單個用戶項目"""
    user: Optional[User] = None
    error: Optional[str] = None


class UserUpdateRequest(N8nBaseModel):
    """更新用戶角色請求模型"""
    newRoleName: UserRole


class UsersList(N8nBaseModel):
    """用戶列表響應模型"""
    data: list[User]
    nextCursor: Optional[str] = None
    count: Optional[int] = None
