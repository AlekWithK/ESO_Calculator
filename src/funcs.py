from buffs import buffs

#Primary function for Parse Normalizer
def normalizer(t_dps, c_chance, t_hits, t_c_hits, t_non_hits, c_damage):
    
    c_chance = c_chance / 100
    c_damage = c_damage / 100
    
    #Total hits - hits that cannot crit -> Actual crit %
    valid_hits = t_hits - t_non_hits
    true_crit = t_c_hits / valid_hits
    
    #Calculating % difference
    dps_delta = ((1 + (c_chance * c_damage)) / (1 + true_crit * c_damage) - 1)
    dps_delta_str = round((dps_delta * 100), 2)
    str_delta = f'+{dps_delta_str}%' if dps_delta >= 0 else f'{dps_delta_str}%'
    
    #Calculating new DPS total
    result = round((t_dps * (1 + dps_delta)), 0)
    str_result = str(result)[:-2]
    
    return str_result, str_delta

#Primary function for Crit Calculator
#Must == relative to pre-checked boxes
avg_crit = 74

def crit_calc(self, src, val):    
    global avg_crit
    
    #Check for special case 
    if buffs[src] != "shadow":
        #If selected  
        if val is True:
            if self.ids[str(src)].text == "":
                avg_crit += (buffs[src][0] * buffs[src][1])
            else:
                avg_crit += (buffs[src][0] * (float(self.ids[str(src)].text)))
                
        #If not selected
        else:
            if self.ids[str(src)].text == "":
                avg_crit -= (buffs[src][0] * buffs[src][1])
            else:
                avg_crit -= (buffs[src][0] * (float(self.ids[str(src)].text)))
                
    else:
        if val is True:
            if self.ids[str(src)].text == "":
                avg_crit += (buffs[src][0] + (1 * buffs[src][1]))
            else:
                avg_crit += (buffs[src][0] + (1 * (float(self.ids[str(src)].text))))
                
        else:
            if self.ids[str(src)].text == "":
                avg_crit -= (buffs[src][0] + (1 * buffs[src][1]))
            else:
                avg_crit -= (buffs[src][0] + (1 * (float(self.ids[str(src)].text))))
         
    return avg_crit