from splinter.browser import Browser
import django


def before_all(context):
    context.browser = Browser('chrome', headless=False)


def after_all(context):
    context.browser.quit()
    context.browser = None
