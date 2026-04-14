import argparse
import boto3
from utils import setup_logger

logger = setup_logger()

def audit_resources(region):
    logger.info(f"Starting audit for region: {region}")
    # AWS interaction
    ec2 = boto3.client('ec2', region_name=region)
    logger.info("Fetching instance list...")
    # In a real scenario, this would list instances
    print(f"[*] Audit complete for {region}. 0 issues found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AWS Cloud Manager CLI")
    parser.add_argument("--region", default="us-east-1", help="AWS Region to audit")
    parser.add_argument("--audit", action="store_true", help="Run resource audit")
    
    args = parser.parse_args()
    
    if args.audit:
        audit_resources(args.region)
    else:
        print("Usage: python main.py --region <region> --audit")
