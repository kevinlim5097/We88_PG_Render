# -*- coding: utf-8 -*-
import unittest
import sys
import os
os.environ['PLAYWRIGHT_BROWSERS_PATH'] = '/opt/render/.cache/ms-playwright'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from playwright.async_api import async_playwright
from new_config import BASE_URL_INDO, headless, indo_close_all_popups_and_chat, indo, check_visible_text_for_errors

class TestChromiumBrowser(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        """启动浏览器并登录"""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=headless)
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()
        await indo(self.page)
        await self.login()

    async def login(self):
        """执行登录操作"""
        await self.page.goto(BASE_URL_INDO)
        self.assertIn("WE88", await self.page.title())

        # 确保聊天窗口和弹窗已关闭
        await self.page.click("#langeDiv > a > img")
        await self.page.click("#region_language_modal > div > div > div > div > div.region-select-text > div:nth-child(2) > div.region-select-lang > a:nth-child(1)")
        await self.page.wait_for_load_state("load")
        await self.page.fill("#fr_login > div.col-lg-3.nopadding > div > div:nth-child(1) > input", "fintest123")
        await self.page.fill("#fr_pass", "123123")
        await self.page.click("#fr_login button")

        await self.page.wait_for_selector("#head-logo-username", timeout=5000)
        logged_in_username = await self.page.inner_text("#head-logo-username")
        self.assertEqual(logged_in_username, "fintest123", "Login Fail")
        print("\nLogin Success, Username: fintest123")

    async def test_id(self):
        await indo_close_all_popups_and_chat(self.page)
        await self.page.click('button.ewallatbtn')
        await self.page.wait_for_timeout(1000)
        print('...Start Testing Indonesia Crypto Deposit...')
        await self.page.click("#btn-crypto-deposit")

        # 点击打开下拉菜单
        await self.page.wait_for_selector("#cryptoChannelWrap > div.custom-dropdown-wrapper > div", timeout=5000)
        await self.page.click("#cryptoChannelWrap > div.custom-dropdown-wrapper")

        # 等待下拉选项加载
        await self.page.wait_for_selector("#cryptoChannelWrap > div.custom-dropdown-wrapper > div > div.custom-options",timeout=5000)
        # 获取所有 data-id
        data_ids = await self.page.evaluate('''
                () => Array.from(document.querySelectorAll("#cryptoChannelWrap > div.custom-dropdown-wrapper > div > div.custom-options > div[data-id]"))
                    .map(el => el.getAttribute("data-id"))
               ''')

        print("Data-IDs:", data_ids)
        self.assertTrue(len(data_ids) > 0, "No data-ids found!")

        # 遍历点击每个 data-id 并获取新页面
        for data_id in data_ids:
            selector_crypto = f'.crypto-payment div[data-id="{data_id}"]'
            # 确保元素可见
            try:
                await self.page.wait_for_selector(selector_crypto, state="visible", timeout=5000)
            except:
                print(f"Element with data-vendor {data_id} not visible, skipping...")
                continue

            await self.page.wait_for_timeout(1000)
            await indo_close_all_popups_and_chat(self.page)
            await self.page.click(selector_crypto)

            payment_method_selector = f'.custom-options div[data-id="{data_id}"]'
            try:
                payment_method = (await self.page.locator(payment_method_selector).text_content()).strip()
            except:
                payment_method = "Unknown"

            try:
                selector_1 = "#cryptoPGWrap > div.flex-only.crypto-method > div"
                await self.page.wait_for_selector(selector_1, timeout=5000)
                await self.page.click(selector_1)
                await self.page.wait_for_selector("#cryptoPGWrap > div.flex-only.crypto-method > div")
                await self.page.click("#cryptoPGWrap > div.flex-only.crypto-method > div")
            except Exception:
                pass  # 忽略异常，继续执行

            try:
                selector_2 = "#cryptoPGNetworkWrap > div.crypto-network > div.active"
                await self.page.wait_for_selector(selector_2, timeout=5000)
                await self.page.click(selector_2)
                await self.page.wait_for_selector("#cryptoPGNetworkWrap > div.crypto-network > div.active")
                await self.page.click("#cryptoPGNetworkWrap > div.crypto-network > div.active")
            except Exception:
                pass  # 忽略异常，继续执行

            await self.page.click("#cryptoPGNetworkWrap > div.crypto-network > div:nth-child(1)", timeout=5000)
            await self.page.wait_for_selector(".fieldInput.mb-2 input[id='depAmount']", timeout=5000)  # 等待金额输入框出现

            # 填写金额
            await self.page.fill(".fieldInput.mb-2 input[id='depAmount']", "10000")
            await self.page.wait_for_timeout(1000)

            async with self.context.expect_page() as new_page_event:
                await self.page.click("#cryptoGatewayBtn")  # 点击元素

                new_page = await new_page_event.value
                # 等待页面完全加载
                await new_page.wait_for_load_state("domcontentloaded")
                await new_page.wait_for_timeout(13000)  # 可调整时间

                # 调用检测函数，传递支付方式
                await check_visible_text_for_errors(new_page, payment_method, data_id)

                # 关闭新页面
                if not new_page.is_closed():
                    await new_page.close()

        print("--------------------INDO Crypto Testing Done--------------------\n")

        print('...Start Testing Indonesia Fast Deposit...')
        await self.page.click('button.ewallatbtn')
        await self.page.wait_for_timeout(1000)
        await self.page.click("#btn-quick-deposit")
        await self.page.wait_for_selector("#qdMethodWrap > div.flex-only.qd-method", timeout=5000)

        # 获取所有 data-id
        data_ids = await self.page.evaluate('''
                   () => Array.from(document.querySelectorAll("#qdMethodWrap > div.flex-only.qd-method div[data-id]"))
                       .map(el => el.getAttribute("data-id"))
               ''')
        print("Data-IDs:", data_ids)
        self.assertTrue(len(data_ids) > 0, "No data-ids found!")

        # 遍历点击每个 data-id 并获取新页面
        for data_id in data_ids:
            selector_fast = f'.flex-only.qd-method div[data-id="{data_id}"]'

            # 确保元素可见
            try:
                await self.page.wait_for_selector(selector_fast, state="visible", timeout=5000)
            except:
                print(f"Element with data-vendor {data_id} not visible, skipping...")
                continue

            # 获取支付方式
            payment_method_selector = f'.flex-only.qd-method div[data-id="{data_id}"]'
            try:
                payment_method = (await self.page.locator(payment_method_selector).text_content()).strip()
            except:
                payment_method = "Unknown"

            await self.page.wait_for_timeout(1000)
            await indo_close_all_popups_and_chat(self.page)
            await self.page.click(selector_fast)  # 点击元素

            await self.page.wait_for_selector(".input-wrap.bank-deposit.payment-gateway input[id='depAmount']",
                                              timeout=5000)
            await self.page.fill(".input-wrap.bank-deposit.payment-gateway input[id='depAmount']", "200000")

            try:
                dropdown_selector = "#qdBankWrap > div.deposit-bank.custom-dropdown-wrapper > div"
                await self.page.wait_for_selector(dropdown_selector, timeout=5000)
                await self.page.click(dropdown_selector)

                option_selector = "#qdBankWrap > div.deposit-bank.custom-dropdown-wrapper > div > div.deposit-bank.custom-options > div:nth-child(1)"
                await self.page.wait_for_selector(option_selector, timeout=5000)
                await self.page.click(option_selector)
            except:
                pass  # 忽略异常，继续执行

            async with self.context.expect_page() as new_page_event:
                await self.page.click("#tfButton")

                new_page = await new_page_event.value
                # 等待页面完全加载
                await new_page.wait_for_load_state("domcontentloaded")
                await new_page.wait_for_timeout(13000)  # 可调整时间

                # 调用检测函数，传递支付方式
                await check_visible_text_for_errors(new_page, payment_method, data_id)

                # 关闭新页面
                if not new_page.is_closed():
                    await new_page.close()

            await self.page.wait_for_timeout(3000)
            await self.page.click('button.ewallatbtn')
            await self.page.wait_for_timeout(1000)
            await self.page.click("#btn-quick-deposit")
            await self.page.wait_for_selector("#qdMethodWrap > div.flex-only.qd-method", timeout=5000)
            await indo_close_all_popups_and_chat(self.page)

        print("--------------------INDO Fast Deposit Testing Done--------------------\n")

    async def asyncTearDown(self):
        """关闭浏览器"""
        if self.page and not self.page.is_closed():
            await self.page.close()
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

if __name__ == "__main__":
    unittest.main()