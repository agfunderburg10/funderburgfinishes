REM create or update cloudformation stack
aws cloudformation deploy --template-file s3.website.cfn.yaml --stack-name funderburgfinishes-site-stack --profile personal^
 --capabilities CAPABILITY_NAMED_IAM^
 --tags resource_for=funderburgfinishes
