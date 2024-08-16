from abc import ABC, abstractmethod


class BaseCampaign(ABC):
    VALID_ID = []

    def __init__(self, campaign_id: int, brand: str, budget: float, required_engagement: float):
        self.campaign_id = campaign_id
        self.brand = brand  # name of the brand associated with the campaign
        self.budget = budget  # budget required for the campaign.
        self.required_engagement = required_engagement  # minimum engagement rate required
        self.approved_influencers = []  # storing influencers objects for the campaign

    @property
    def campaign_id(self):
        return self.__campaign_id

    @campaign_id.setter
    def campaign_id(self, value):

        if value < 0:
            raise ValueError("Campaign ID must be a positive integer greater than zero.")

        if any(i == value for i in self.VALID_ID):
            raise ValueError(f"Campaign with ID {value} already exists. Campaign IDs must be unique.")

        self.VALID_ID.append(value)
        self.__campaign_id = value

    @abstractmethod
    def check_eligibility(self, engagement_rate: float):
        pass
