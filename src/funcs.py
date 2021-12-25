from src.data import buffs

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
#Default crit values
avg_crit = 50
max_crit = 50
#src = textinput ID | src2 = label ID 
def calc_avg_crit(self, src, src2, val):    
    global avg_crit
    
    #Check for special case 
    if buffs[src][2] != "shadow":
        #If selected  
        if val is True:
            if self.ids[str(src)].text == "":
                avg_crit += (buffs[src][0] * buffs[src][1])
                
                if buffs[src][2] == "med_armor":
                    bonus_crit = str(round((buffs[src][0] * buffs[src][1])))
                    self.ids[str(src2)].text = f'{bonus_crit}%'
                else:
                    bonus_crit = str(round((buffs[src][0] * buffs[src][1]), 2))
                    self.ids[str(src2)].text = f'{bonus_crit}%'
                    
            #If custom value      
            else:
                if buffs[src][2] == "med_armor" or buffs[src][2] == "kilt":
                    avg_crit += (buffs[src][0] * (float(self.ids[str(src)].text)))
                    bonus_crit = str(round(buffs[src][0] * (float(self.ids[str(src)].text)), 2))
                    self.ids[str(src2)].text = f'{bonus_crit}%'
                    
                else:
                    avg_crit += (buffs[src][0] * ((float(self.ids[str(src)].text)) / 100))
                    bonus_crit = str(round(buffs[src][0] * ((float(self.ids[str(src)].text)) / 100), 2))
                    self.ids[str(src2)].text = f'{bonus_crit}%'
                
        #If not selected
        else:
            if self.ids[str(src)].text == "":
                avg_crit -= (buffs[src][0] * buffs[src][1])
                self.ids[str(src2)].text = f'0%'
            else:
                if buffs[src][2] == "med_armor" or buffs[src][2] == "kilt":
                    avg_crit -= (buffs[src][0] * (float(self.ids[str(src)].text)))
                    self.ids[str(src2)].text = f'0%'
                else:
                    avg_crit -= (buffs[src][0] * ((float(self.ids[str(src)].text)) / 100))
                    self.ids[str(src2)].text = f'0%'
    #If Shadow         
    else:
        if val is True:
            if self.ids[str(src)].text == "":
                avg_crit += (buffs[src][0] + (1 * buffs[src][1]))
                bonus_crit = str((buffs[src][0] + (1 * buffs[src][1])))
                self.ids[str(src2)].text = f'{bonus_crit}%'
            else:
                avg_crit += (buffs[src][0] + (1 * (float(self.ids[str(src)].text))))
                bonus_crit = str(buffs[src][0] + (1 * (float(self.ids[str(src)].text))))[:-2]
                self.ids[str(src2)].text = f'{bonus_crit}%'                
                
        else:
            if self.ids[str(src)].text == "":
                avg_crit -= (buffs[src][0] + (1 * buffs[src][1]))
                self.ids[str(src2)].text = f'0%'
            else:
                avg_crit -= (buffs[src][0] + (1 * (float(self.ids[str(src)].text))))
                self.ids[str(src2)].text = f'0%'
         
    return avg_crit

def calc_max_crit(self, src, val):
    global max_crit    
        
    #If selected    
    if val is True:
        if self.ids[str(src)].text == "": #If no value is given
            if buffs[src][2] == "med_armor":
                max_crit += (buffs[src][0] * buffs[src][1])
            elif buffs[src][2] == "shadow":
                max_crit += (buffs[src][0] + (1 * buffs[src][1]))
            elif buffs[src][2] == "kilt": 
                max_crit += 10
            else:            
                max_crit += buffs[src][0]            
                
        else: #If value is given
            if buffs[src][2] == "med_armor":
                max_crit += (buffs[src][0] * float(self.ids.med_armor.text))
            elif buffs[src][2] == "shadow":
                max_crit += (buffs[src][0] + (1 * float(self.ids.shadow.text)))
            elif buffs[src][2] == "kilt": 
                max_crit += 10
            #Default case (uptime is a %)
            else:            
                max_crit += buffs[src][0]            
            
    #If not selected      
    else:
        if self.ids[str(src)].text == "": #If no value is given
            if buffs[src][2] == "med_armor":
                max_crit -= (buffs[src][0] * buffs[src][1])
            elif buffs[src][2] == "shadow":
                max_crit -= (buffs[src][0] + (1 * buffs[src][1]))
            elif buffs[src][2] == "kilt": 
                max_crit -= 10
            else:            
                max_crit -= buffs[src][0]            
                
        else: #If value is given
            if buffs[src][2] == "med_armor":
                max_crit -= (buffs[src][0] * float(self.ids.med_armor.text))
            elif buffs[src][2] == "shadow":
                max_crit -= (buffs[src][0] + (1 * float(self.ids.shadow.text)))
            elif buffs[src][2] == "kilt": 
                max_crit -= 10
            #Default case (uptime is a %)
            else:            
                max_crit -= buffs[src][0]
    
    return max_crit