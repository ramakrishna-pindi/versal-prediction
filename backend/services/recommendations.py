def recommendations(data):
    tips = []
    if data.acs >= 2:
        tips.append({"title":"Reduce AC consumption","message":"Use a suitable temperature, clean filters, keep doors/windows closed and use Eco/Sleep mode when suitable.","priority":"high"})
    if data.current_units > 300:
        tips.append({"title":"High current usage","message":"Check high-load appliances and unnecessary usage because the entered current-month units are high.","priority":"high"})
    if data.fans >= 5:
        tips.append({"title":"Use fans efficiently","message":"Turn fans off in empty rooms and keep blades clean.","priority":"medium"})
    if data.fridges >= 2:
        tips.append({"title":"Refrigerator efficiency","message":"Avoid unnecessary door opening and check door seals and temperature settings.","priority":"medium"})
    if data.tvs >= 3:
        tips.append({"title":"Manage electronics","message":"Switch off unused electronics and avoid unnecessary standby consumption.","priority":"medium"})
    tips.append({"title":"Lighting","message":"Use LED bulbs, daylight and switch off lights in empty rooms.","priority":"low"})
    return tips[:6]
