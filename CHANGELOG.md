# Changelog

This document records all notable changes to n8n-sdk-python.

## [0.1.2] - 2025-05-17

### Fixed
- Removed `callerPolicy` field from `WorkflowSettings` model. This field is not supported by the n8n API for workflow creation/update and was causing a `400 - request/body/settings must NOT have additional properties` error.

## [0.1.1] - 2025-05-16

### Added
- Added detailed descriptions and default values to all model fields.

### Changed
- Replaced `loguru` with standard Python `logging` module.

### Styling
- Minor code adjustments for PEP8 compliance.

## [0.1.0] - 2025-05-14

### Added
- Initial release
- Full support for n8n API v1.1.1
- Implemented asynchronous client architecture
- Support for all major n8n resources: workflows, executions, credentials, tags, users, projects, variables, etc.
- Comprehensive error handling mechanism
- Detailed documentation and examples

### Features
- Complete API Coverage
  - User Management
  - Workflow Management
  - Execution Management
  - Credential Management
  - Tag Management
  - Project Management
  - Variable Management
  - Source Control Integration
  - Security Audit Features
- Asynchronous Operations Support
- Strong Typing System
- Detailed Logging
- Custom Error Handling
- Environment Variable Configuration Support

### Planned Features
- Implement bulk operations
- Increase unit test coverage
- Add caching mechanism
- Workflow execution result monitoring
- Implement event subscription mechanism 