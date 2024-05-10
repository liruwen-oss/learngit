import pytest
import allure
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

@allure.feature("访问百度")
@allure.story("验证访问成功成功")
def test_baidu_success():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS'  # 指定 Chrome 可执行文件的路径
    chrome_options.add_argument('--no-sandbox')  # 如果需要，添加其他选项
    # ChromeDriver 的路径
    chromedriver_path = '/Users/bytedance/Downloads/chromedriver_mac64/chromedriver'
    # 设置 ChromeDriver 的路径
    chrome_options.add_argument(f'--webdriver-path={chromedriver_path}')
    # 启动 Chrome，并指定 Chrome 选项
    wd = webdriver.Chrome(options=chrome_options)
    # 执行操作
    wd.get('https://www.baidu.com')
    sleep(3)
    current_page_url = wd.current_url
    # 断言网页url是否是百度
    assert current_page_url == "https://www.baidu.com/"
    # 断言网页title
    assert '百度一下，你就知道' == wd.title
    # 退出 WebDriver
    wd.quit()

@allure.feature("访问百度")
@allure.story("正常输入查询：python-成功")
def test_normal_search():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS'
    chrome_options.add_argument('--no-sandbox')
    chromedriver_path = '/Users/bytedance/Downloads/chromedriver_mac64/chromedriver'
    chrome_options.add_argument(f'--webdriver-path={chromedriver_path}')
    wd = webdriver.Chrome(options=chrome_options)
    wd.get('https://www.baidu.com')
    sleep(3)
    search_box = wd.find_element(By.ID, 'kw')
    search_box.send_keys('Python')  # 输入"Python"
    search_box.submit()  # 提交搜索
    sleep(3)
    current_page_url = wd.current_url
    assert current_page_url == "https://www.baidu.com/s?wd=Python"  # 检查返回的页面URL是否正确
    wd.quit()

@allure.feature("访问百度")
@allure.story("正常输入查询多个关键字：python编程")
def test_normal_more_search():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS'
    chrome_options.add_argument('--no-sandbox')
    chromedriver_path = '/Users/bytedance/Downloads/chromedriver_mac64/chromedriver'
    chrome_options.add_argument(f'--webdriver-path={chromedriver_path}')
    wd = webdriver.Chrome(options=chrome_options)
    wd.get('https://www.baidu.com')
    sleep(3)
    search_box = wd.find_element(By.ID, 'kw')
    search_box.send_keys('Python')  # 输入"Python"
    search_box.submit()  # 提交搜索
    sleep(3)
    current_page_url = wd.current_url
    assert current_page_url == "https://www.baidu.com/s?wd=Python"  # 检查返回的页面URL是否正确
    wd.quit()

@allure.feature("访问百度")
@allure.story("边界场景查询：搜索内容含有特殊字符")
def test_abnormal_search_special_symbols():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS'
    chrome_options.add_argument('--no-sandbox')
    chromedriver_path = '/Users/bytedance/Downloads/chromedriver_mac64/chromedriver'
    chrome_options.add_argument(f'--webdriver-path={chromedriver_path}')
    wd = webdriver.Chrome(options=chrome_options)
    wd.get('https://www.baidu.com')
    sleep(3)
    search_box = wd.find_element(By.ID, 'kw')  # 假设搜索框的id为'kw'
    search_box.send_keys('@#$%^&*(abc123)')  # 输入非法字符
    sleep(1)
    search_box.submit()  # 提交搜索
    sleep(2)
    current_page_url = wd.current_url
    assert "abc" in current_page_url
    wd.quit()

@allure.feature("访问百度")
@allure.story("边界场景查询：搜索内容超出长度限制大于100个字符长度")
def test_abnormal_limit_search():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS'
    chrome_options.add_argument('--no-sandbox')
    chromedriver_path = '/Users/bytedance/Downloads/chromedriver_mac64/chromedriver'
    chrome_options.add_argument(f'--webdriver-path={chromedriver_path}')
    wd = webdriver.Chrome(options=chrome_options)
    wd.get('https://www.baidu.com')
    sleep(3)
    search_box = wd.find_element(By.ID, 'kw')  # 假设搜索框的id为'kw'
    search_box.send_keys('搜索内容超出长度限制搜索内容超出长度限制搜索内容超出长度限制搜索内容超出长度限制搜索内容超出长度限制搜索内容超出长度限制搜索内容超出长度限制搜索内容超出长度限制搜索内容超出长度限制搜索内容超出长度限制1')  # 输入非法字符
    sleep(1)
    search_box.submit()  # 提交搜索
    sleep(2)
    current_page_url = wd.current_url
    assert "搜索内" in current_page_url
    wd.quit()