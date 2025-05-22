from playwright.sync_api import sync_playwright

def choisir_club():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        url = "https://www.basic-fit.com/fr-fr/checkout?stage=HomeClub#HomeClub"
        page.goto(url, wait_until='networkidle')

        page.wait_for_selector('.js-select-club-new-checkout', timeout=10000)

        boutons = page.query_selector_all('.js-select-club-new-checkout')
        for bouton in boutons:
            nom_club = bouton.get_attribute("data-name")
            if nom_club and "Paris Rue Froment" in nom_club:
                print(f"✅ Club trouvé : {nom_club}")
                bouton.click()
                break
        else:
            print("❌ Club non trouvé.")

        page.wait_for_timeout(3000)
        browser.close()

# Pour test local (peut être retiré si intégré dans une API)
if __name__ == "__main__":
    choisir_club()
