# game_config.py
from playwright.async_api import Page

# 各个地区的 BASE_URL 设置
BASE_URL_INDO = "https://www.we88bertuah.com/"
BASE_URL_MY = "https://www.we88my1.com/"
BASE_URL_THAI = "https://www.we88th6.com/"
BASE_URL_VIET = "https://www.we88vet.com/"

# True = Off Chrome, False = On Chrome
headless = False

from playwright.async_api import Page

async def check_visible_text_for_errors(page: Page, payment_method, data_id) -> bool:
    """
    异步版：检查页面是否含有错误/维护等字眼，仅检测可见文本，不包含 <script> 内容。
    返回 True 表示通过，False 表示失败。
    同时打印 Status: Pass / Fail
    """
    keywords = [
        "error",
        "maintenance",
        "out of service",
        "unavailable",
        "404",
        "503",
        "not found",
        "wrong",
        "disconnect"
    ]

    try:
        visible_text = (await page.inner_text("body")).lower()
    except Exception as e:
        print(f"⚠ Unable Reach The Page: {e}")
        print("Status: Fail")
        return False

    for keyword in keywords:
        if keyword in visible_text:
            print(f"ID:[{data_id}], Payment Method:[{payment_method}],\n❌ Status: Fail")
            print(f"Keywords Found: [{keyword}]\n")
            return False

    print(f"ID:[{data_id}], Payment Method:[{payment_method}],\n✅ Status: Pass\n")
    return True

# Script Starting Add on this
# ------------INDO------------
async def indo(page: Page):
    await page.add_init_script("""
        // 永久关闭所有弹窗
        window.localStorage.setItem('popupClosed', 'true');
        window.sessionStorage.setItem('popupClosed', 'true');
        document.cookie = 'popupClosed=true; path=/; max-age=31536000';

        // 永久关闭聊天窗口
        window.localStorage.setItem('chatClosed', 'true');

        // 监听DOM变化，确保聊天窗口不会重新出现
        const observer = new MutationObserver(() => {
            const epl_popup = document.querySelector('#epl-popup');
            const container = document.querySelector('#chat-widget-container');
            const promo_popup = document.querySelector('#promo-popup');
            const noti_inbox = document.querySelector('.small-notifications-wrapper');

            if (epl_popup) {
                epl_popup.style.display = 'none';
                epl_popup.remove();
            }

            if (container) {
                container.style.display = 'none';
                container.remove();
            }

            if (promo_popup) {
                promo_popup.style.display = 'none';
                promo_popup.remove();
            }

            if (noti_inbox) {
                noti_inbox.style.display = 'none';
                noti_inbox.remove();
            }                                    
        });

        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    """)


# ------------MY------------
# 在页面加载前设置永久关闭弹窗和聊天窗口的脚本
async def my(page: Page):
    await page.add_init_script("""
           // 永久关闭所有弹窗
           window.localStorage.setItem('popupClosed', 'true');
           window.sessionStorage.setItem('popupClosed', 'true');
           document.cookie = 'popupClosed=true; path=/; max-age=31536000';

           // 永久关闭聊天窗口
           window.localStorage.setItem('chatClosed', 'true');

           // 监听DOM变化，确保聊天窗口不会重新出现
           const observer = new MutationObserver(() => {
               const epl_popup = document.querySelector('#epl-popup');
               const container = document.querySelector('#chat-widget-container');
               const overlay = document.querySelector('.overlay-fog');
               const inbox = document.querySelector('.inbox-wrapper');
               const noti_inbox = document.querySelector('.small-notifications-wrapper');

               if (epl_popup) {
                   epl_popup.style.display = 'none';
                   epl_popup.remove();
               }

               if (container) {
                   container.style.display = 'none';
                   container.remove();
               }

               if (overlay) {
                   overlay.style.display = 'none';
                   overlay.remove();
               }

               if (inbox) {
                   inbox.style.display = 'none';
                   inbox.remove();
               }      

               if (noti_inbox) {
                   noti_inbox.style.display = 'none';
                   noti_inbox.remove();
               }                 
           });

           observer.observe(document.body, {
               childList: true,
               subtree: true
           });
       """)


# ------------THAI------------
# 在页面加载前设置永久关闭弹窗和聊天窗口的脚本
async def thai(page: Page):
    await page.add_init_script("""
        // 永久关闭所有弹窗
        window.localStorage.setItem('popupClosed', 'true');
        window.sessionStorage.setItem('popupClosed', 'true');
        document.cookie = 'popupClosed=true; path=/; max-age=31536000';

        // 永久关闭聊天窗口
        window.localStorage.setItem('chatClosed', 'true');

        // 监听DOM变化，确保聊天窗口不会重新出现
        const observer = new MutationObserver(() => {
            const epl_popup = document.querySelector('#epl-popup');
            const container = document.querySelector('#chat-widget-container');
            const noti_inbox = document.querySelector('.small-notifications-wrapper');

            if (epl_popup) {
                epl_popup.style.display = 'none';
                epl_popup.remove();
            }

            if (container) {
                container.style.display = 'none';
                container.remove();
            }

            if (noti_inbox) {
                noti_inbox.style.display = 'none';
                noti_inbox.remove();
            }                     
        });

        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    """)


# ------------VIET------------
# 在页面加载前设置永久关闭弹窗和聊天窗口的脚本
async def viet(page: Page):
    await page.add_init_script("""
        // 永久关闭所有弹窗
        window.localStorage.setItem('popupClosed', 'true');
        window.sessionStorage.setItem('popupClosed', 'true');
        document.cookie = 'popupClosed=true; path=/; max-age=31536000';

        // 永久关闭聊天窗口
        window.localStorage.setItem('chatClosed', 'true');

        // 监听DOM变化，确保聊天窗口不会重新出现
        const observer = new MutationObserver(() => {
            const epl_popup = document.querySelector('#epl-popup');
            const container = document.querySelector('#chat-widget-container');
            const noti_inbox = document.querySelector('.small-notifications-wrapper');

            if (epl_popup) {
                epl_popup.style.display = 'none';
                epl_popup.remove();
            }

            if (container) {
                container.style.display = 'none';
                container.remove();
            }

            if (noti_inbox) {
                noti_inbox.style.display = 'none';
                noti_inbox.remove();
            }                
        });

        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    """)


# =====================================================#
# Closing All Popups and Chat List
# ------------INDO------------
async def indo_close_all_popups_and_chat(page: Page):
    """关闭所有弹窗和聊天窗口，并确保它们不会再次出现"""
    # 确保元素被永久关闭
    await page.evaluate("""
        // 直接移除或隐藏聊天元素
        const epl_popup = document.querySelector('#epl-popup');
        const container = document.querySelector('#chat-widget-container');
        const promo_popup = document.querySelector('#promo-popup');
        const noti_inbox = document.querySelector('.small-notifications-wrapper');

        if (epl_popup) {
            epl_popup.style.display = 'none';
            epl_popup.remove();
        }

        if (container) {
            container.style.display = 'none';
            container.remove();
        }

        if (promo_popup) {
            promo_popup.style.display = 'none';
            promo_popup.remove();
        }
        if (noti_inbox) {
            noti_inbox.style.display = 'none';
            noti_inbox.remove();
        }

        // 设置永久关闭标记
        window.localStorage.setItem('chatClosed', 'true');
        window.sessionStorage.setItem('chatClosed', 'true');
        document.cookie = 'chatClosed=true; path=/; max-age=31536000';

        // 确保弹窗不会再次出现
        window.localStorage.setItem('popupClosed', 'true');
        window.sessionStorage.setItem('popupClosed', 'true');
        document.cookie = 'popupClosed=true; path=/; max-age=31536000';
    """)


# ------------MY------------
async def my_close_all_popups_and_chat(page: Page):
    """关闭所有弹窗和聊天窗口，并确保它们不会再次出现"""
    # 确保元素被永久关闭
    await page.evaluate("""
                // 直接移除或隐藏聊天元素
                const epl_popup = document.querySelector('#epl-popup');
                const container = document.querySelector('#chat-widget-container');
                const overlay = document.querySelector('.overlay-fog');
                const inbox = document.querySelector('.inbox-wrapper');
                const noti_inbox = document.querySelector('.small-notifications-wrapper');

                if (epl_popup) {
                    epl_popup.style.display = 'none';
                    epl_popup.remove();
                }

                if (container) {
                    container.style.display = 'none';
                    container.remove();
                }

                if (overlay) {
                    overlay.style.display = 'none';
                    overlay.remove();
                }

                if (inbox) {
                    inbox.style.display = 'none';
                    inbox.remove();
                }
                if (noti_inbox) {
                    noti_inbox.style.display = 'none';
                    noti_inbox.remove();
                }         

                // 设置永久关闭标记
                window.localStorage.setItem('chatClosed', 'true');
                window.sessionStorage.setItem('chatClosed', 'true');
                document.cookie = 'chatClosed=true; path=/; max-age=31536000';

                // 确保弹窗不会再次出现
                window.localStorage.setItem('popupClosed', 'true');
                window.sessionStorage.setItem('popupClosed', 'true');
                document.cookie = 'popupClosed=true; path=/; max-age=31536000';
            """)


# ------------THAI------------
async def th_close_all_popups_and_chat(page: Page):
    """关闭所有弹窗和聊天窗口，并确保它们不会再次出现"""
    # 确保元素被永久关闭
    await page.evaluate("""
        // 直接移除或隐藏聊天元素
        const epl_popup = document.querySelector('#epl-popup');
        const container = document.querySelector('#chat-widget-container');
        const noti_inbox = document.querySelector('.small-notifications-wrapper');

        if (epl_popup) {
            epl_popup.style.display = 'none';
            epl_popup.remove();
        }

        if (container) {
            container.style.display = 'none';
            container.remove();
        }

        if (noti_inbox) {
            noti_inbox.style.display = 'none';
            noti_inbox.remove();
        }

        // 设置永久关闭标记
        window.localStorage.setItem('chatClosed', 'true');
        window.sessionStorage.setItem('chatClosed', 'true');
        document.cookie = 'chatClosed=true; path=/; max-age=31536000';

        // 确保弹窗不会再次出现
        window.localStorage.setItem('popupClosed', 'true');
        window.sessionStorage.setItem('popupClosed', 'true');
        document.cookie = 'popupClosed=true; path=/; max-age=31536000';
    """)


# ------------VIET------------

async def vn_close_all_popups_and_chat(page: Page):
    """关闭所有弹窗和聊天窗口，并确保它们不会再次出现"""
    # 确保元素被永久关闭
    await page.evaluate("""
        // 直接移除或隐藏聊天元素
        const epl_popup = document.querySelector('#epl-popup');
        const container = document.querySelector('#chat-widget-container');
        const noti_inbox = document.querySelector('.small-notifications-wrapper');

        if (epl_popup) {
            epl_popup.style.display = 'none';
            epl_popup.remove();
        }

        if (container) {
            container.style.display = 'none';
            container.remove();
        }

        if (noti_inbox) {
            noti_inbox.style.display = 'none';
            noti_inbox.remove();
        }

        // 设置永久关闭标记
        window.localStorage.setItem('chatClosed', 'true');
        window.sessionStorage.setItem('chatClosed', 'true');
        document.cookie = 'chatClosed=true; path=/; max-age=31536000';

        // 确保弹窗不会再次出现
        window.localStorage.setItem('popupClosed', 'true');
        window.sessionStorage.setItem('popupClosed', 'true');
        document.cookie = 'popupClosed=true; path=/; max-age=31536000';
    """)
