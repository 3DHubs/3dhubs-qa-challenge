from selenium.webdriver.common.by import By


class QuoteOverviewPageLocators:
    PAGE_TITLE = (By.TAG_NAME, "h3d-page-title")
    PART_DESCRIPTION_TITLE = (By.CLASS_NAME, "part-description__title")