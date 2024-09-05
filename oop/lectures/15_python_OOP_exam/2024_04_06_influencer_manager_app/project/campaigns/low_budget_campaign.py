from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign (BaseCampaign):
    HIGH_BUDGET = 2500.00
    ENGAGEMENT_RATE_MULTIPLIER = 0.9

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.HIGH_BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float) -> bool:
        return engagement_rate >= (self.required_engagement * self.ENGAGEMENT_RATE_MULTIPLIER)