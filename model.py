#  implement predition and detection methods here 
def tomato_disease_info(disease_name):
    disease_info = {
        "Tomato___Bacterial_spot": {
            "Causes": "Bacterial speck caused by Xanthomonas vesicatoria",
            "Prevention": "Crop rotation, removing weeds, and avoiding excessive nitrogen fertilizer",
            "Solution": "Copper fungicide",
            "Medications": "Copper fungicide"
        },
        "Tomato___Early_blight": {
            "Causes": "Early blight caused by Alternaria solani",
            "Prevention": "Crop rotation, removing weeds, and avoiding excessive nitrogen fertilizer",
            "Solution": "Pruning and fungicide",
            "Medications": "Fungicide"
        },
        "Tomato___Late_blight": {
            "Causes": "Late blight caused by Phytophthora infestans",
            "Prevention": "Crop rotation, removing weeds, and avoiding excessive nitrogen fertilizer",
            "Solution": "Copper spray",
            "Medications": "Copper spray"
        },
        "Tomato___Leaf_Mold": {
            "Causes": "Leaf mold caused by Septoria lycopersici",
            "Prevention": "Increase air circulation, water at soil line, and remove weeds",
            "Solution": "Fungicide",
            "Medications": "Fungicide"
        },
        "Tomato___Septoria_leaf_spot": {
            "Causes": "Septoria leaf spot caused by Septoria lycopersici",
            "Prevention": "Crop rotation, removing weeds, and avoiding excessive nitrogen fertilizer",
            "Solution": "Fungicide",
            "Medications": "Fungicide"
        },
        "Tomato___Spider_mites": {
            "Causes": "Spider mites caused by Tetranychus urticae",
            "Prevention": "Good garden hygiene, removing weeds, and avoiding excessive nitrogen fertilizer",
            "Solution": "Insecticide",
            "Medications": "Insecticide"
        },
        "Tomato___Target_Spot": {
            "Causes": "Target spot caused by Corynespora cassiicola",
            "Prevention": "Crop rotation, removing weeds, and avoiding excessive nitrogen fertilizer",
            "Solution": "Fungicide",
            "Medications": "Fungicide"
        },
        "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
            "Causes": "Tomato yellow leaf curl virus caused by Begomovirus",
            "Prevention": "Good garden hygiene, removing weeds, and avoiding excessive nitrogen fertilizer",
            "Solution": "No cure, but can be managed through good garden practices",
            "Medications": "None"
        },
        "Tomato___Tomato_mosaic_virus": {
            "Causes": "Tomato mosaic virus caused by Tomato mosaic virus",
            "Prevention": "Good garden hygiene, removing weeds, and avoiding excessive nitrogen fertilizer",
            "Solution": "No cure, but can be managed through good garden practices",
            "Medications": "None"
        },
        "Tomato___healthy": {
            "Causes": "No disease",
            "Prevention": "Good garden practices such as crop rotation, removing weeds, and avoiding excessive nitrogen fertilizer",
            "Solution": "None",
            "Medications": "None"
        }
    }

    if disease_name in disease_info:
        return disease_info[disease_name]
    else:
        return "Disease not found"
