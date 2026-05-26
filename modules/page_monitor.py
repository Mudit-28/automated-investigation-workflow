import asyncio
import time


class PageMonitor:
    def __init__(self, network_monitor, screenshot, html_capture):
        self.screenshot = screenshot
        self.html_capture = html_capture
        self.network_monitor = network_monitor
        self.monitored_pages = []
        self.last_screenshot_time = 0     
        self.screenshot_cooldown = 4      
        self.initial_url = None           
        self.page_ready = False
        self._active = True 

    def stop(self):
        self._active = False          

    def _can_screenshot(self):
        now = time.time()
        if now - self.last_screenshot_time >= self.screenshot_cooldown:
            self.last_screenshot_time = now
            return True
        return False

    async def _safe_capture(self, page, url):
        if not self._can_screenshot():
            return
        try:
            await self.screenshot.capture_ss(page, url)
            await self.html_capture.capture_html(page, url)
        except Exception as e:
            print(f"[Page Monitor] Capture error: {e}")

    def attach(self, page, url):
        self.initial_url = url
        self.base_url = url
        page.on("popup", lambda popup: asyncio.ensure_future(
            self._on_popup(popup)
        ))
        page.on("framenavigated", lambda frame: asyncio.ensure_future(
            self._on_navigation(frame, page)
        ))
        page.on("load", lambda: asyncio.ensure_future(
            self._on_page_load(page)
        ))
        print(f"[Page Monitor] Attached to: {url}")

    async def _on_page_load(self, page):
        await asyncio.sleep(3)
        self.page_ready = True
        print(f"[Page Monitor] Page ready, DOM observer active")
        await self._setup_mutation_observer(page)

    async def _on_popup(self, popup):
        try:
            print(f"[Page Monitor] New popup/tab detected")
            await popup.wait_for_load_state("domcontentloaded")
            popup_url = popup.url

            self.network_monitor.attach(popup)
            await asyncio.sleep(2)

            await self._safe_capture(popup, popup_url)
            self.monitored_pages.append(popup_url)
            print(f"[Page Monitor] Popup captured: {popup_url}")

            popup.on("popup", lambda p: asyncio.ensure_future(
                self._on_popup(p)
            ))
            popup.on("framenavigated", lambda frame: asyncio.ensure_future(
                self._on_navigation(frame, popup)
            ))
        except Exception as e:
            print(f"[Page Monitor] Popup error: {e}")

    async def _on_navigation(self, frame, page):
        if not self._active:  
            return
        try:
            if not self.page_ready:
                return

            if frame != page.main_frame:
                return

            new_url = frame.url

            if not new_url or new_url == "about:blank":
                return

            if new_url == self.initial_url:
                return

            print(f"[Page Monitor] Navigation detected: {new_url}")
            await page.wait_for_load_state("domcontentloaded")
            await asyncio.sleep(1)
            await self._safe_capture(page, new_url)

        except Exception as e:
            print(f"[Page Monitor] Navigation error: {e}")

    async def _setup_mutation_observer(self, page):
        try:
            await page.evaluate("""
                () => {
                    // reset flag cleanly before starting
                    window._paymentDomChanged = false;
                    window._domChangeCount = 0;

                    const observer = new MutationObserver((mutations) => {
                        for (const mutation of mutations) {
                            if (mutation.addedNodes.length > 0) {
                                window._domChangeCount += 1;
                                // only flag after 3 changes to avoid noise
                                if (window._domChangeCount >= 3) {
                                    window._paymentDomChanged = true;
                                    window._domChangeCount = 0;
                                }
                            }
                        }
                    });
                    observer.observe(document.body, {
                        childList: true,
                        subtree: true
                    });
                }
            """)
            asyncio.ensure_future(self._poll_dom_changes(page))
            print(f"[Page Monitor] DOM observer injected")
        except Exception as e:
            print(f"[Page Monitor] DOM observer error: {e}")

    async def _poll_dom_changes(self, page):
        await asyncio.sleep(5)
        while self._active:             
            try:
                await asyncio.sleep(3)
                changed = await page.evaluate(
                    "() => window._paymentDomChanged || false"
                )
                if changed:
                    print(f"[Page Monitor] DOM change detected — capturing")
                    await self._safe_capture(page, page.url)
                    await page.evaluate(
                        "() => { window._paymentDomChanged = false; window._domChangeCount = 0; }"
                    )
            except Exception:
                break

    def attach_context(self, context, url):
        self.base_url = url
        context.on("page", lambda page: asyncio.ensure_future(
            self._on_new_context_page(page)
        ))
        print(f"[Page Monitor] Context listener attached")

    async def _on_new_context_page(self, page):
        if not self._active:  
            return
        try:
            print(f"[Page Monitor] New context page detected")
            await page.wait_for_load_state("domcontentloaded")
            await asyncio.sleep(2)
            self.network_monitor.attach(page)
            await self._safe_capture(page, page.url)
            page.on("popup", lambda popup: asyncio.ensure_future(
                self._on_popup(popup)
            ))
        except Exception as e:
            print(f"[Page Monitor] Context page error: {e}")