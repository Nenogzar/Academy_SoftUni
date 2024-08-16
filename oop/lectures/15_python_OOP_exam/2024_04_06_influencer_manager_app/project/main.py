from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign

try:

    c = HighBudgetCampaign(12, "NOrka" , 1000)
    print(c.HIGH_BUDGET,"HIGH_BUDGET")
    print(c.VALID_ID, "Valid ID")
    print(c.ENGAGEMENT_RATE_MULTIPLIER)
    print(c.check_eligibility(1199))
    print()

    b= HighBudgetCampaign(13, "NOrka" , 1000)
    print(b.HIGH_BUDGET,"HIGH_BUDGET")
    print(b.VALID_ID, "Valid ID")
    print(b.ENGAGEMENT_RATE_MULTIPLIER)
    print(b.check_eligibility(1200))
    print()

    d= LowBudgetCampaign(11, "NOrka" , 1000)
    print(d.HIGH_BUDGET,"HIGH_BUDGET")
    print(d.VALID_ID, "Valid ID")
    print(d.ENGAGEMENT_RATE_MULTIPLIER)
    print(d.check_eligibility(900))
    print()


except ValueError as e:
    print(e)
