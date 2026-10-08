# Start de oefen mee met onderstaande dictionary.
planner = {
    "Slaap": 6,
    "Werk":  8,
    "Ontspanning": 8
}
# print("planning van morgen.")
# print(f"- slaap :{planner["Slaap"]} u.")
# print(f"- werk :{planner["Werk"]} u.")
# print(f"- ontspanning :{planner["Ontspanning"]} u.")
# uitkomst = 24 - planner["Ontspanning"] - planner["Werk"] - planner["Slaap"]
# print(f"je hebt {uitkomst}")
#Niveau2
uitkomst = 24
for sleutel , waarde in planner.items():
    print(f"- {sleutel} : {planner[sleutel]} u.")
    uitkomst = uitkomst - waarde
print(uitkomst)