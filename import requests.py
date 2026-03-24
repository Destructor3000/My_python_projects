import requests, time

def limpiar(t):
    return float(t.replace("€", "").replace(",", ".").replace("-", "0").strip())

presupuesto = 0.35
skin = "M4A4 | Magnesium (Field-Tested)"

while True:
    url = f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name={skin}"
    try:
        res = requests.get(url).json()
        if res.get("success"):
            p_act = limpiar(res.get("lowest_price", "0"))
            p_med = limpiar(res.get("median_price", "0"))

            print(f"\n{skin} | Actual: {p_act}€ | Media: {p_med}€")

            if p_act <= (p_med * 0.9) and p_act > 0: print("🔥 ¡CHOLLO!")
            print("✅ COMPRAR" if p_act <= presupuesto and p_act > 0 else "❌ CARO")
    except:
        print("💥 Error")
    
    time.sleep(60)
