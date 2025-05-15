"""
n8n API 客戶端模組。
這個模組包含與 n8n API 通信的客戶端類。
"""

from .base import BaseClient
from .users import UserClient
from .audit import AuditClient
from .executions import ExecutionClient
from .workflows import WorkflowClient
from .credentials import CredentialClient
from .tags import TagClient
from .source_control import SourceControlClient
from .variables import VariableClient
from .projects import ProjectClient

from .nodes import NodesClient
from .connections import ConnectionsClient

from typing import Optional

class N8nClient:
    """
    n8n API 完整客戶端類，整合所有API功能。
    """
    
    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None):
        """
        初始化 n8n API 客戶端
        
        Args:
            base_url: n8n API 的基礎 URL
            api_key: n8n API 金鑰
        """
        self.users = UserClient(base_url=base_url, api_key=api_key)
        self.audit = AuditClient(base_url=base_url, api_key=api_key)
        self.executions = ExecutionClient(base_url=base_url, api_key=api_key)
        self.workflows = WorkflowClient(base_url=base_url, api_key=api_key)
        self.credentials = CredentialClient(base_url=base_url, api_key=api_key)
        self.tags = TagClient(base_url=base_url, api_key=api_key)
        self.source_control = SourceControlClient(base_url=base_url, api_key=api_key)
        self.variables = VariableClient(base_url=base_url, api_key=api_key)
        self.projects = ProjectClient(base_url=base_url, api_key=api_key)

        self.nodes = NodesClient(base_url=base_url, api_key=api_key)
        self.connections = ConnectionsClient(base_url=base_url, api_key=api_key)

        self.create_workflow = self.workflows.create_workflow
        self.list_workflows = self.workflows.list_workflows
        self.get_workflow = self.workflows.get_workflow
        self.delete_workflow = self.workflows.delete_workflow
        self.update_workflow = self.workflows.update_workflow
        self.activate_workflow = self.workflows.activate_workflow
        self.deactivate_workflow = self.workflows.deactivate_workflow
        self.transfer_workflow_to_project = self.workflows.transfer_workflow_to_project
        self.get_workflow_tags = self.workflows.get_workflow_tags
        self.update_workflow_tags = self.workflows.update_workflow_tags
        
    
    async def list_users(self, **kwargs): return await self.users.list_users(**kwargs)
    async def create_users(self, **kwargs): return await self.users.create_users(**kwargs)
    async def get_user(self, **kwargs): return await self.users.get_user(**kwargs)
    async def delete_user(self, **kwargs): return await self.users.delete_user(**kwargs)
    async def update_user_role(self, **kwargs): return await self.users.update_user_role(**kwargs)

    async def generate_audit_report(self, **kwargs): return await self.audit.generate_audit_report(**kwargs)

    async def list_executions(self, **kwargs): return await self.executions.list_executions(**kwargs)
    async def get_execution(self, **kwargs): return await self.executions.get_execution(**kwargs)
    async def delete_execution(self, **kwargs): return await self.executions.delete_execution(**kwargs)

    async def create_credential(self, **kwargs): return await self.credentials.create_credential(**kwargs)
    async def delete_credential(self, **kwargs): return await self.credentials.delete_credential(**kwargs)
    async def get_credential_schema(self, **kwargs): return await self.credentials.get_credential_schema(**kwargs)
    async def transfer_credential_to_project(self, **kwargs): return await self.credentials.transfer_credential_to_project(**kwargs)

    async def create_tag(self, **kwargs): return await self.tags.create_tag(**kwargs)
    async def list_tags(self, **kwargs): return await self.tags.list_tags(**kwargs)
    async def get_tag(self, **kwargs): return await self.tags.get_tag(**kwargs)
    async def delete_tag(self, **kwargs): return await self.tags.delete_tag(**kwargs)
    async def update_tag(self, **kwargs): return await self.tags.update_tag(**kwargs)

    async def pull_from_source_control(self, **kwargs): return await self.source_control.pull_from_source_control(**kwargs)

    async def create_variable(self, **kwargs): return await self.variables.create_variable(**kwargs)
    async def list_variables(self, **kwargs): return await self.variables.list_variables(**kwargs)
    async def delete_variable(self, **kwargs): return await self.variables.delete_variable(**kwargs)

    async def create_project(self, **kwargs): return await self.projects.create_project(**kwargs)
    async def list_projects(self, **kwargs): return await self.projects.list_projects(**kwargs)
    async def delete_project(self, **kwargs): return await self.projects.delete_project(**kwargs)
    async def update_project(self, **kwargs): return await self.projects.update_project(**kwargs)
    
    async def get_node_types(self, **kwargs): return await self.nodes.get_node_types(**kwargs)
    async def get_node_type(self, **kwargs): return await self.nodes.get_node_type(**kwargs)

__all__ = [
    'BaseClient',
    'UserClient',
    'AuditClient',
    'ExecutionClient',
    'WorkflowClient',
    'CredentialClient',
    'TagClient',
    'SourceControlClient',
    'VariableClient',
    'ProjectClient',
    'NodesClient',
    'ConnectionsClient',
    'N8nClient'
] 