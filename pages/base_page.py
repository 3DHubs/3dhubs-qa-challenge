"""The most basic page class, that receives Playwright Page object for initiating"""
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
