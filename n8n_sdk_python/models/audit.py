"""
n8n 審計日誌資料模型。
定義審計日誌相關的資料結構。
"""

from typing import Optional, Any
from pydantic import Field
from .base import N8nBaseModel

class AuditAdditionalOptions(N8nBaseModel):
    """審計請求的額外選項"""
    daysAbandonedWorkflow: Optional[int] = Field(None, description="廢棄工作流程的天數")
    categories: Optional[list[str]] = Field(None, description="審計類別")

class AuditReportLocationItem(N8nBaseModel):
    """審計報告位置項目"""
    kind: str
    id: Optional[str] = None
    name: Optional[str] = None
    workflowId: Optional[str] = None
    workflowName: Optional[str] = None
    nodeId: Optional[str] = None
    nodeName: Optional[str] = None
    nodeType: Optional[str] = None
    packageUrl: Optional[str] = None # For community nodes

class AuditReportSection(N8nBaseModel):
    """審計報告區段"""
    title: str
    description: str
    recommendation: str
    # API 範例中有一個 "or validating the input of the expression in the "Query" field.": null 這樣的鍵，
    # 這不是合法的 Python 識別符，Pydantic 可能無法直接處理。
    # 我們可以將其視為 additional_details 或類似的通用 dict。
    additional_details: Optional[dict[str, Optional[str]]] = Field(None, alias="or validating the input of the expression in the \"Query\" field.")
    location: list[AuditReportLocationItem]

class AuditRiskReport(N8nBaseModel):
    """審計風險報告基類"""
    risk: str
    sections: list[AuditReportSection]

class AuditResponse(N8nBaseModel):
    """審計 API 響應模型"""
    CredentialsRiskReport: Optional[AuditRiskReport] = Field(None, alias="Credentials Risk Report")
    DatabaseRiskReport: Optional[AuditRiskReport] = Field(None, alias="Database Risk Report")
    FilesystemRiskReport: Optional[AuditRiskReport] = Field(None, alias="Filesystem Risk Report")
    NodesRiskReport: Optional[AuditRiskReport] = Field(None, alias="Nodes Risk Report")
    InstanceRiskReport: Optional[AuditRiskReport] = Field(None, alias="Instance Risk Report") 