from pydantic import BaseModel, Field, validator
from typing import Any, Optional, Union
from datetime import datetime
import json

class N8nBaseModel(BaseModel):
    """n8n API 基礎模型類，所有其他模型繼承自此類"""
    
    class Config:
        """Pydantic 配置"""
        validate_assignment = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat()
        }
    
    def to_json(self) -> str:
        """將模型轉換為 JSON 字符串"""
        return json.dumps(self.model_dump(), default=str)
    
    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        """從字典創建模型實例"""
        return cls(**data)
    
    def update_from_dict(self, data: dict[str, Any]) -> None:
        """從字典更新模型字段"""
        for field_name, field_value in data.items():
            if hasattr(self, field_name):
                setattr(self, field_name, field_value) 