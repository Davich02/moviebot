#from playwright.sync_api import sync_playwright
#import random
#поведение человека
'''def human_delay(page, min_ms=1000, max_ms=3000):
    page.wait_for_timeout(random.randint(min_ms, max_ms))

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,  # обязательно False — Cloudflare блокирует headless
        slow_mo=100
    )

    # Имитируем реальный браузер
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 800},
        locale="ru-RU",
    )

    page = context.new_page()

    # 1. Главная страница
    page.goto("https://kinogo.online", wait_until="domcontentloaded")
    human_delay(page, 2000, 4000)

    # Двигаем мышкой как человек
    page.mouse.move(random.randint(100, 500), random.randint(100, 400))
    human_delay(page, 500, 1500)
    page.mouse.move(random.randint(200, 700), random.randint(200, 500))
    human_delay(page, 1000, 2000)

    print("Главная:", page.title())

    # 2. Кликаем на Новинки как человек (не goto)
    # Вместо клика — просто переходим напрямую
    page.goto("https://kinogo.online/novinki/", wait_until="domcontentloaded")
    human_delay(page, 3000, 5000)  # ждём дольше после клика

    print("Текущая страница:", page.title())
    print("URL:", page.url)

    # 3. Проверяем не попали ли на капчу
    if "момент" in page.title().lower() or "cloudflare" in page.title().lower():
        print("Попали на капчу, ждём...")
        human_delay(page, 5000, 8000)  # ждём пока пройдёт

    # 4. Ждём заголовки
    page.locator(".hTitle").first.wait_for(timeout=15000)
    human_delay(page, 1000, 2000)

    # 5. Скроллим как человек
    page.evaluate("window.scrollTo(0, 300)")
    human_delay(page, 500, 1000)
    page.evaluate("window.scrollTo(0, 600)")
    human_delay(page, 500, 1000)

    # 6. Собираем заголовки
    titles = page.locator(".hTitle h2 a").all()
    print(f"\nНайдено фильмов: {len(titles)}")

    for title in titles:
        text = title.inner_text()
        href = title.get_attribute("href")
        print(f"{text} -> {href}")

    browser.close()'''
from playwright.sync_api import sync_playwright
import random

def human_delay(page, min_ms=1000, max_ms=3000):
    page.wait_for_timeout(random.randint(min_ms, max_ms))

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 800},
        locale="ru-RU",
    )
    page = context.new_page()

    page.goto("https://kinogo.online/novinki/", wait_until="domcontentloaded")

    # Ждём пока вручную пройдёшь капчу (60 секунд)
    print("Если есть капча — поставь галочку вручную!")
    page.wait_for_function("document.title !== 'Один момент…'", timeout=60000)
    print("Капча пройдена!")

    # Сохраняем сессию
    context.storage_state(path="session.json")
    print("Сессия сохранена в session.json")

    browser.close()