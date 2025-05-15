"""
n8n 源碼控制資料模型。
定義源碼控制相關的資料結構。
"""

from typing import Optional, Any, Union
from enum import Enum
from datetime import datetime
from pydantic import Field

from .base import N8nBaseModel


class ScmPullRequest(N8nBaseModel):
    """源碼控制拉取請求模型 (POST /source-control/pull 的請求體)"""
    force: Optional[bool] = Field(None, description="是否強制拉取")
    variables: Optional[dict[str, Any]] = Field(None, description="在拉取期間應用的變量")


class ScmPullResponseVariables(N8nBaseModel):
    """源碼控制拉取響應中的變量變更"""
    added: Optional[list[str]] = Field(default_factory=list)
    changed: Optional[list[str]] = Field(default_factory=list)


class ScmPullResponseCredential(N8nBaseModel):
    """源碼控制拉取響應中的憑證簡要信息"""
    id: str
    name: str
    type: str


class ScmPullResponseWorkflow(N8nBaseModel):
    """源碼控制拉取響應中的工作流程簡要信息"""
    id: str
    name: str


class ScmPullResponseTagItem(N8nBaseModel):
    """源碼控制拉取響應中的標籤項"""
    id: str
    name: str


class ScmPullResponseTagMapping(N8nBaseModel):
    """源碼控制拉取響應中的標籤映射"""
    workflowId: str
    tagId: str


class ScmPullResponseTags(N8nBaseModel):
    """源碼控制拉取響應中的標籤變更"""
    tags: Optional[list[ScmPullResponseTagItem]] = Field(default_factory=list)
    mappings: Optional[list[ScmPullResponseTagMapping]] = Field(default_factory=list)


class ScmPullResponse(N8nBaseModel):
    """源碼控制拉取響應模型 (POST /source-control/pull 的響應體)"""
    variables: Optional[ScmPullResponseVariables] = None
    credentials: Optional[list[ScmPullResponseCredential]] = Field(default_factory=list)
    workflows: Optional[list[ScmPullResponseWorkflow]] = Field(default_factory=list)
    tags: Optional[ScmPullResponseTags] = None

# ScmConnection, ScmConnectionCreate, ScmConnectionUpdate 等模型
# 在 N8N-API.md 中沒有找到對應的 /source-control/connections (或類似) 端點來管理連接本身。
# 只有 /source-control/pull 端點。因此，這些連接管理相關的模型可能來自舊版或企業版特定功能。
# 暫時註解，以嚴格對應提供的 API 文件。

class ScmProvider(str, Enum):
    """源碼控制提供者枚舉"""
    GITHUB = "github"
    GITLAB = "gitlab"
    BITBUCKET = "bitbucket"
    GITEA = "gitea"
    CUSTOM = "custom"


class ScmConnectionType(str, Enum):
    """源碼控制連接類型枚舉"""
    OAUTH2 = "oauth2"
    PERSONAL_ACCESS_TOKEN = "personalAccessToken"
    BASIC_AUTH = "basicAuth"
    SSH_KEY = "sshKey"


class PullRequestState(str, Enum):
    """拉取請求狀態枚舉"""
    OPEN = "open"
    CLOSED = "closed"
    MERGED = "merged"


class ScmConnection(N8nBaseModel):
    """源碼控制連接資料模型"""
    id: str
    name: str
    provider: ScmProvider
    repositoryUrl: str
    branchName: str
    connectionType: ScmConnectionType
    connected: bool
    settings: Optional[dict[str, Any]] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class ScmConnectionCreate(N8nBaseModel):
    """建立源碼控制連接請求模型"""
    name: str
    provider: ScmProvider
    repositoryUrl: str
    branchName: Optional[str] = "main"
    connectionType: ScmConnectionType
    settings: Optional[dict[str, Any]] = None


class ScmConnectionUpdate(N8nBaseModel):
    """更新源碼控制連接請求模型"""
    name: Optional[str] = None
    provider: Optional[ScmProvider] = None
    repositoryUrl: Optional[str] = None
    branchName: Optional[str] = None
    connectionType: Optional[ScmConnectionType] = None
    settings: Optional[dict[str, Any]] = None


class PullRequestStatus(N8nBaseModel):
    """拉取請求狀態資料模型"""
    pullRequestId: str
    state: PullRequestState
    title: str
    url: str
    createdAt: datetime
    updatedAt: Optional[datetime] = None
    mergedAt: Optional[datetime] = None
    closedAt: Optional[datetime] = None


class CommitInfo(N8nBaseModel):
    """提交資訊資料模型"""
    id: str
    message: str
    date: datetime
    author: str
    url: Optional[str] = None


class ScmStatus(N8nBaseModel):
    """源碼控制狀態資料模型"""
    connected: bool
    currentBranch: Optional[str] = None
    latestCommit: Optional[CommitInfo] = None
    pendingChanges: bool = False
    activePullRequest: Optional[PullRequestStatus] = None


class StatusItemType(str, Enum):
    """狀態項目類型枚舉"""
    WORKFLOW = "workflow"
    CREDENTIAL = "credential"
    VARIABLE = "variable"
    TAG = "tag"
    OWNER = "owner"
    OTHER = "other"


class StatusItemStatus(str, Enum):
    """狀態項目狀態枚舉"""
    CREATED = "created"
    MODIFIED = "modified"
    DELETED = "deleted"
    RENAMED = "renamed"
    CONFLICT = "conflict"


class StatusItem(N8nBaseModel):
    """狀態項目資料模型"""
    id: str
    name: str
    type: StatusItemType
    status: StatusItemStatus
    oldName: Optional[str] = None  # 用於重命名操作


class StatusList(N8nBaseModel):
    """狀態列表響應模型"""
    data: list[StatusItem]
    count: int


class PullRequestCreate(N8nBaseModel):
    """建立拉取請求請求模型"""
    title: str
    description: Optional[str] = None
    targetBranch: Optional[str] = None


class BranchCreate(N8nBaseModel):
    """建立分支請求模型"""
    name: str
    fromBranch: Optional[str] = None