# Working with Amazon Virtual Private Cloud<a name="services-vpc"></a>

Amazon Virtual Private Cloud \(Amazon VPC\) is a service for creating private networks, security rules, and related resources in AWS\. You create a virtual private cloud \(VPC\) to allow resources like EC2 instances and databases to communicate securely over a local network connection\.

When you use Amazon Relational Database Service \(Amazon RDS\) or Amazon Redshift as a datasource, Lookout for Metrics uses Amazon VPC to [connect to a database](#services-vpc-database) in your account\. The detector creates a network interface in your VPC subnet and uses it to connect to the database and run queries at the end of each interval\.

If you develop applications that run in a VPC without internet access, you can also create a [VPC endpoint](#services-vpc-interface)\. A VPC endpoint lets applications running in a private subnet connect to an AWS service without an internet connection\.

**Topics**
+ [Connecting to a database](#services-vpc-database)
+ [Creating a VPC endpoint](#services-vpc-interface)
+ [Sample AWS CloudFormation templates](#services-vpc-templates)

## Connecting to a database<a name="services-vpc-database"></a>

When you configure a detector to monitor a database, you choose a VPC subnet and security group\. The detector uses these to create a network interface that it can use to connect to the database\. The network interface is named `Amazon Lookout for Metrics Network Interface`\.

The detector gets permission to manage network interfaces in your VPC from the a [service role](permissions-service.md)\. When you configure a datasource in the Lookout for Metrics console, the console can create a role for you\. To consolidate datasource and alert roles for a detector, or connect to a database in another account, you can create a custom role\.

For more information, see the following topics:

****
+ [Using Amazon RDS with Lookout for Metrics](services-rds.md)
+ [Using Amazon Redshift with Lookout for Metrics](services-redshift.md)

## Creating a VPC endpoint<a name="services-vpc-interface"></a>

To establish a private connection between your VPC and Amazon Lookout for Metrics, create a *VPC endpoint*\. A VPC endpoint is not required to monitor a database for anomalies\. You only need to create a VPC endpoint if you run an application that uses the AWS SDK in a private subnet\. When the AWS SDK attempts to connect to Lookout for Metrics, the traffic is routed through the VPC endpoint\.

[Create a VPC endpoint](https://console.aws.amazon.com//vpc/home#CreateVpcEndpoint:) for Lookout for Metrics using the following settings:
+ **Service name** – **com\.amazonaws\.*us\-east\-2*\.lookoutmetrics**
+ **Type** – **Interface**

A VPC endpoint uses the service's DNS name to get traffic from AWS SDK clients without any additional configuration\. For more information about using VPC endpoints, see [Interface VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*\.

## Sample AWS CloudFormation templates<a name="services-vpc-templates"></a>

The GitHub repository for this guide provides AWS CloudFormation templates that you can use to create resources for use with Lookout for Metrics\. The `vpc-network.yml` template creates a VPC with two private subnets, a public subnet, and a VPC endpoint\.

You can use the private subnets in the VPC to host a database that is isolated from the internet\. Resources in the public subnet can communicate with the database, but the database can't be accessed from the internet\.

**Example [vpc\-network\.yml](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-templates/vpc-network.yml) – Private subnets**  

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  vpc:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 172.31.0.0/16
      EnableDnsHostnames: true
      EnableDnsSupport: true
      Tags:
        - Key: Name
          Value: !Ref AWS::StackName
  privateSubnetA:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref vpc
      AvailabilityZone:
        Fn::Select:
         - 0
         - Fn::GetAZs: ""
      CidrBlock: 172.31.3.0/24
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: !Sub  ${AWS::StackName}-subnet-a
  ...
```

The `vpc-network` template shows how to create a VPC endpoint\. The VPC endpoint is not required to connect the detector to a database, but can be used to communicate securely with Lookout for Metrics from compute resources in a private subnet\.

**Example [vpc\-network\.yml](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-templates/vpc-network.yml) – VPC endpoint**  

```
  lookoutfmEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      ServiceName: !Sub com.amazonaws.${AWS::Region}.lookoutmetrics
      VpcId: !Ref vpc
      VpcEndpointType: Interface
      SecurityGroupIds:
      - !GetAtt vpc.DefaultSecurityGroup
      PrivateDnsEnabled: true
      SubnetIds:
      - !Ref privateSubnetA
      - !Ref privateSubnetB
      PolicyDocument:
        Version: 2012-10-17
        Statement:
        - Effect: Allow
          Principal: "*"
          Action:
            - "lookoutmetrics:*"
          Resource:
            - "*"
```

The `PolicyDocument` is a resource\-based permissions policy that defines the API calls that can be made with the endpoint\. You can modify the policy to restrict the actions and resources that can be accessed through the endpoint\.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*\. 