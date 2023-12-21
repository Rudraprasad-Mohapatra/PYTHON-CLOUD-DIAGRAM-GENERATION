from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("aws basic", show=False):
    ELB("lb") >> [EC2("web1"), EC2("web2"), EC2("web3")] >> RDS("db")