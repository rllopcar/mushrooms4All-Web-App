import pandas as pd
import numpy as np

mushrooms_aux = pd.read_csv("mushrooms_clean_2.csv")

mushrooms = mushrooms_aux.iloc[:,2:]
def data_enconding(data):
    
    mushrooms_appended = mushrooms.append(data)
    data_encoded = pd.get_dummies(mushrooms_appended, columns=["cap.shape", "cap.surface","cap.color","bruises","odor","gill.attachment",
                                            "gill.spacing","gill.size","gill.color","stalk.shape","stalk.root",
                                            "stalk.surface.above.ring","stalk.surface.below.ring","stalk.color.above.ring",
                                            "stalk.color.below.ring","veil.type","veil.color","ring.number","ring.type","spore.print.color",
                                            "population","habitat"],
                                            prefix=["cap.shape", "cap.surface","cap.color","bruises","odor","gill.attachment",
                                            "gill.spacing","gill.size","gill.color","stalk.shape","stalk.root",
                                            "stalk.surface.above.ring","stalk.surface.below.ring","stalk.color.above.ring",
                                            "stalk.color.below.ring","veil.type","veil.color","ring.number","ring.type","spore.print.color",
                                            "population","habitat"
                                            ])

    mushrooms_encoded = data_encoded.iloc[-1,:]
    return mushrooms_encoded
