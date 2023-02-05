import json
dict = {
    "Odisha": "Bhubaneswar",
    "Andhrapradesh": "vishakhapatnam",
    "Karnataka": "Bengaluru",
    "Bihar": "Patna",
    "west Bengal": "Kolkata",
    "Kerala": "Thiruvanthanpuram",
    "Tamil Nadu": "Chennai"
}
with open("State_Capitals.json","w") as f:
    json.dump(dict,f)