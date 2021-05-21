from splinter.browser import Browser


def before_all(context):
    context.browser = Browser('chrome', headless=True)
    context.browser.driver.set_window_size(1200, 985)


def after_all(context):
    context.browser.quit()
    context.browser = None
