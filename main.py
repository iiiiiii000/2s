import requests
import math
import random

URL = [
    "https://codeberg.org/VALCHIK/bypass-rkn-blocks/raw/branch/main/configs/obhod_WL"
]

country_order = [
    "Russia", "Germany", "Netherlands", "Finland", "Sweden", "Norway", "Denmark",
    "Poland", "Czech", "Austria", "Switzerland", "France", "Spain", "Italy",
    "United Kingdom", "Canada", "USA", "Japan", "Singapore", "Australia",
    "Belgium", "Ireland", "Portugal", "Greece", "Hungary", "Romania", "Bulgaria",
    "Croatia", "Slovakia", "Slovenia", "Estonia", "Latvia", "Lithuania",
    "Iceland", "Luxembourg", "Malta", "Cyprus", "Turkey", "Israel", "UAE",
    "Saudi Arabia", "India", "Indonesia", "Malaysia", "Thailand", "Vietnam",
    "Philippines", "South Korea", "Brazil", "Argentina", "Chile", "Mexico",
    "South Africa", "Nigeria", "Kenya"
]

country_map = {
    "Russia": "🇷🇺 Россия", "Germany": "🇩🇪 Германия", "Netherlands": "🇳🇱 Нидерланды",
    "Finland": "🇫🇮 Финляндия", "Sweden": "🇸🇪 Швеция", "Norway": "🇳🇴 Норвегия",
    "Denmark": "🇩🇰 Дания", "Poland": "🇵🇱 Польша", "Czech": "🇨🇿 Чехия",
    "Austria": "🇦🇹 Австрия", "Switzerland": "🇨🇭 Швейцария", "France": "🇫🇷 Франция",
    "Spain": "🇪🇸 Испания", "Italy": "🇮🇹 Италия", "United Kingdom": "🇬🇧 Великобритания",
    "Canada": "🇨🇦 Канада", "USA": "🇺🇸 США", "Japan": "🇯🇵 Япония",
    "Singapore": "🇸🇬 Сингапур", "Australia": "🇦🇺 Австралия", "Belgium": "🇧🇪 Бельгия",
    "Ireland": "🇮🇪 Ирландия", "Portugal": "🇵🇹 Португалия", "Greece": "🇬🇷 Греция",
    "Hungary": "🇭🇺 Венгрия", "Romania": "🇷🇴 Румыния", "Bulgaria": "🇧🇬 Болгария",
    "Croatia": "🇭🇷 Хорватия", "Slovakia": "🇸🇰 Словакия", "Slovenia": "🇸🇮 Словения",
    "Estonia": "🇪🇪 Эстония", "Latvia": "🇱🇻 Латвия", "Lithuania": "🇱🇹 Литва",
    "Iceland": "🇮🇸 Исландия", "Luxembourg": "🇱🇺 Люксембург", "Malta": "🇲🇹 Мальта",
    "Cyprus": "🇨🇾 Кипр", "Turkey": "🇹🇷 Турция", "Israel": "🇮🇱 Израиль",
    "UAE": "🇦🇪 ОАЭ", "Saudi Arabia": "🇸🇦 Саудовская Аравия", "India": "🇮🇳 Индия",
    "Indonesia": "🇮🇩 Индонезия", "Malaysia": "🇲🇾 Малайзия", "Thailand": "🇹🇭 Таиланд",
    "Vietnam": "🇻🇳 Вьетнам", "Philippines": "🇵🇭 Филиппины", "South Korea": "🇰🇷 Южная Корея",
    "Brazil": "🇧🇷 Бразилия", "Argentina": "🇦🇷 Аргентина", "Chile": "🇨🇱 Чили",
    "Mexico": "🇲🇽 Мексика", "South Africa": "🇿🇦 ЮАР", "Nigeria": "🇳🇬 Нигерия",
    "Kenya": "🇰🇪 Кения"
}

def get_country(tag):
    for country in country_order:
        if country in tag:
            return country
    return random.choice(country_order)

def transform_link(link, country_name):
    if '#' not in link:
        return link
    base = link.split('#')[0] + '#'
    ru_name = country_map.get(country_name, f"{country_name}")
    return f"{base}{ru_name}"

def main():
    all_lines = []
    for url in URL:
        resp = requests.get(url)
        for l in resp.text.splitlines():
            l = l.strip()
            if l and not l.startswith('#') and l.startswith('vless://'):
                all_lines.append(l)
    seen = set()
    unique_lines = []
    for line in all_lines:
        if line not in seen:
            seen.add(line)
            unique_lines.append(line)
    by_country = {c: [] for c in country_order}
    for line in unique_lines:
        country = get_country(line)
        by_country[country].append(line)
    all_final_links = []
    for country in country_order:
        for link in by_country[country]:
            all_final_links.append(transform_link(link, country))
    header = "# profile-title: loli vpn <3\n# profile-update-interval: 1\n#profile-web-page-url: https://t.me/loli_free_vpn\n#announce: Бесплатная подписка навсегда- | Бот: @lolivpnrobot\n"
    with open("sub", "w", encoding="utf-8") as f:
        f.write(header + "\n".join(all_final_links))

if __name__ == "__main__":
    main()
