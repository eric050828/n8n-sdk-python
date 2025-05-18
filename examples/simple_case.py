import asyncio
from n8n_sdk_python import N8nClient
from n8n_sdk_python.models import Workflow

async def create_http_workflow():
    client = N8nClient(
        base_url="http://localhost:5678",
        api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzYjEzMzk5Yi1iYjI2LTQyOWItOThlNS03ZTM4YTFkMzQ5OTMiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzQ4MTMxOTI4LCJleHAiOjE3NTA2NTEyMDB9.Zq6K82Uh9E0K1k92sgmy2mj_X9wC-9U5BPIuaxgCris"  # 添加缺失的憑證
    )
    
    # 建立工作流
    workflow_data_payload = {
        "name": "HTTP Request Demo SDK",
        "nodes": [
            {
            "id": "schedule",
            "parameters": {
                "interval": [
                {
                    "field": "minutes",
                    "value": 5
                }
                ]
            },
            "name": "Schedule Trigger",
            "type": "n8n-nodes-base.scheduleTrigger",
            "typeVersion": 1,
            "position": [240, 300]
            },
            {
            "id": "set",
            "parameters": {
                "values": {
                "string": [
                    {
                    "name": "message",
                    "value": "Hello from n8n!"
                    }
                ]
                }
            },
            "name": "Set",
            "type": "n8n-nodes-base.set",
            "typeVersion": 1,
            "position": [440, 300]
            },
            {
            "id": "code",
            "parameters": {
                "mode": "runOnceForAllItems",
                "jsCode": "// 取得輸入數據\nconst items = $input.all();\n\n// 加工處理數據\nconst outputData = items.map(item => ({\n  json: {\n    message: item.json.message,\n    timestamp: new Date().toISOString(),\n    processed: true\n  }\n}));\n\n// 返回處理後的數據\nreturn outputData;"
            },
            "name": "Code",
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [640, 300]
            },
            {
            "id": "http",
            "parameters": {
                "url": "https://httpbin.org/post",
                "method": "POST",
                "options": {},
                "sendBody": True,
                "bodyParameters": {
                "parameters": [
                    {
                    "name": "data",
                    "value": "={{ $json }}"
                    }
                ]
                }
            },
            "name": "HTTP Request",
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.2,
            "position": [840, 300]
            }
        ],
        "connections": {
            "Schedule Trigger": {
            "main": [
                [
                {
                    "node": "Set",
                    "type": "main",
                    "index": 0
                }
                ]
            ]
            },
            "Set": {
            "main": [
                [
                {
                    "node": "Code",
                    "type": "main",
                    "index": 0
                }
                ]
            ]
            },
            "Code": {
            "main": [
                [
                {
                    "node": "HTTP Request",
                    "type": "main",
                    "index": 0
                }
                ]
            ]
            }
        },
        "settings": {
            "saveExecutionProgress": True,
            "saveManualExecutions": True
            # "executionTimeout": 3600 # 根據需要添加
        }
    }
    
    # 創建工作流
    created_workflow: Workflow = await client.create_workflow(**workflow_data_payload)
    print(f"建立工作流成功，ID: {created_workflow.id}, 名稱: {created_workflow.name}")
    
    # 啟用工作流
    activated_workflow: Workflow = await client.activate_workflow(workflow_id=created_workflow.id)
    print(f"工作流 '{activated_workflow.name}' 已 {'激活' if activated_workflow.active else '未激活'}")
    
    return created_workflow.id

if __name__ == "__main__":
    workflow_id = asyncio.run(create_http_workflow())
    print(f"完成操作，工作流 ID: {workflow_id}")