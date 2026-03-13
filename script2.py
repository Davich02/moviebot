from playwright.sync_api import sync_playwright
import random


def human_delay(page, min_ms=1000, max_ms=3000):
    page.wait_for_timeout(random.randint(min_ms, max_ms))


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    # Загружаем сохранённую сессию
    context = browser.new_context(
        storage_state="session.json"
    )
    page = context.new_page()

    page.goto("https://kinogo.online/novinki/", wait_until="domcontentloaded")
    human_delay(page, 2000, 3000)

    print("Страница:", page.title())

    # Ждём заголовки
    page.locator(".hTitle").first.wait_for(timeout=15000)

    # Собираем фильмы
    titles = page.locator(".hTitle h2 a").all()
    print(f"Найдено фильмов: {len(titles)}")

    for title in titles:
        print(f"{title.inner_text()} -> {title.get_attribute('href')}")

    browser.close()