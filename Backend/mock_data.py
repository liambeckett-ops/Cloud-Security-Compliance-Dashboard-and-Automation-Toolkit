MOCK_RESOURCES = [
    {"id": "r1", "type": "EC2", "name": "WebServer1", "compliance_status": "Compliant"},
    {"id": "r2", "type": "S3", "name": "DataBucket", "compliance_status": "Non-Compliant"},
]

MOCK_SCANS = [
    {"id": "s1", "resource_id": "r2", "tool": "Nessus", "severity": "Critical", "finding": "Public S3 bucket", "status": "Open"},
    {"id": "s2", "resource_id": "r1", "tool": "TrendMicro", "severity": "Low", "finding": "Outdated package", "status": "Resolved"},
]

MOCK_INCIDENTS = [
    {"id": "i1", "title": "Unauthorized Access", "status": "Open", "description": "Detected suspicious login to EC2."}
]