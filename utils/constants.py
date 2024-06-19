from dataclasses import dataclass


@dataclass
class Servers:
    STAGE = 'stage'
    PREPROD = 'preprod'
    PROD = 'prod'
