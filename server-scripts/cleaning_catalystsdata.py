#!/home/solarchem/scripts/.venv/kgc/bin/python

import pandas as pd
from datetime import datetime

def clean_numeric_columns(value):
    """Return float values for numeric column of empty values when there is no value"""
    try:
        value = float(value)
        if value == 0.0:
            return('')
        else:
            return(value)
    
    except ValueError or TypeError:
        return('')	


def set_wavelengths(wl):
    """Stablish range of wavelegths instead of specific values"""
    try:
        wl = float(wl)
        if (wl) >= 192 and (wl) <= 280:
            return("192-280")
        elif (wl) >= 280 and (wl) <= 315:
            return("280-315")
        elif (wl) >= 315 and (wl) <= 400:
            return("315-400")
        elif (wl) >= 400 and (wl) <= 780:
            return("400-780")
        elif (wl) >= 315 and (wl) <= 780:
            return("315-780")
        elif (wl) >= 280 and (wl) <= 780:
            return("280-780")
        elif (wl) >= 192 and (wl) <= 780:
            return("192-780")
        
    except ValueError:
        wl = wl.replace('192-280(UV-A)', '192-280')
        wl = wl.replace('315-400(UV-C)', '315-400')
        wl = wl.replace('280-315(UV-B)', '280-315')
        return(wl)
    
    except TypeError:
        return('')


def co2_production(CO, CH4, C2H4, C2H6, C3H6, C3H8, C4H8, C4H10, C5H10, C5H12, CH3OH, C2H5OH, CH3COH, HCOOH, CH2O, C2H4O2):
    """Calculate production of CO2"""
    values = []
    for var in [CO, CH4, CH3OH, HCOOH, CH2O]:
        try:
            float(var)
            values.append(var)
        except:
            pass

    for var in [C2H4, C2H6, C2H5OH, C2H4O2, CH3COH]:
        try:
            float(var)
            values.append(var*2)
        except:
            pass

    for var in [C3H6, C3H8]:
        try:
            float(var)
            values.append(var*3)
        except:
            pass

    for var in [C4H8, C4H10]:
        try:
            float(var)
            values.append(var*4)
        except:
            pass

    for var in [C5H10, C5H12]:
        try:
            float(var)
            values.append(var*5)
        except:
            pass
    if sum(values) == 0.0:
        return('')
    else:
        return(sum(values))


def selectivity(product, H2, CO, CH4, CH3OH):
    """Calculate selectivity of catalysts"""
    if product == '':
        return('')
    
    values = []
    for value in [H2, CO, CH4, CH3OH]:
        try:
            values.append(float(value))
        except:
            values.append(0.0)

    sum_values = sum(values)
    return ((product/sum_values)*100)


def cleaning_catalystdata():
	"""
		Cleaning the file `raw_catalystsdata.csv`:
          - Normalize null values
          - Cleaning numeric columns
          - Normalizing categoric values to align with the terms in the ontology
          - Calculating CO2 production and catalyst selectivity
          
        It uses the following functions:
          - selectivity()
          - co2_production()
          - set_wavelengths()
          - clean_numeric_columns()
	"""

	print('['+str(datetime.now().time())[0:8]+'] Processing catalystsdata.csv')
	exp_df = pd.read_csv("/home/solarchem/data/raw/raw-catalystsdata.csv")

	print('['+str(datetime.now().time())[0:8]+'] Fixing null values')
	# Removing negative numbers and values that serve as null
	exp_df.replace([-1,"-1", -1.0, 0.0, 9999.99], '', inplace=True)
	exp_df.head(5)

	# Cleaning false null values 
	exp_df.Masscat_g = exp_df.Masscat_g.apply(clean_numeric_columns)
	exp_df.support_percent = exp_df.support_percent.apply(clean_numeric_columns)
	exp_df.percent = exp_df.percent.apply(clean_numeric_columns)
	exp_df.percent_cc_2 = exp_df.percent_cc_2.apply(clean_numeric_columns)
	exp_df.percent_cc_3 = exp_df.percent_cc_3.apply(clean_numeric_columns)
	exp_df.dopant_percent = exp_df.dopant_percent.apply(clean_numeric_columns)
	exp_df.dye_percent = exp_df.dye_percent.apply(clean_numeric_columns)

	print('['+str(datetime.now().time())[0:8]+'] Aligning values with terms in the ontology')
	# Aligning values with ontology hierarchies
	# Reactor types
	exp_df['Reactor_type'] = exp_df['Reactor_type'].replace((' ', 'Batch'), '')
	
	# Light sources
	exp_df['Light_source'] = exp_df['Light_source'].replace(' ', '')

	# Lamps
	exp_df['Lamp'] = exp_df['Lamp'].replace({"Mercury(Hg)":"Mercury", 
                              "Xenon(Xe)":"Xenon", 
                              "Solar":"SolarSimulator",  
                              "Not spedified":"", 
                              "Mercury-Xenon(Hg-Xe)":"Mercury-Xenon", 
                              "Tungsten(W)":"Tungsten"})

	# Wavelengths
	exp_df.Wavelength_nm = exp_df.Wavelength_nm.apply(set_wavelengths)

	print('['+str(datetime.now().time())[0:8]+'] Calculating CO2 production and selectivity')
	# Calculating CO2 production
	exp_df['co2_prod_molgh'] = exp_df.apply(lambda x: co2_production(x['CO_mol_gh'], x['CH4_mol_gh'], x['C2H4_mol_gh'], x['C2H6_mol_gh'], x['C3H6_mol_gh'], x['C3H8_mol_gh'], x['C4H8_mol_gh'], x['C4H10_mol_gh'], x['C5H10_mol_gh'], x['C5H12_mol_gh'], x['CH3OH_mol_gh'], x['C2H5OH_mol_gh'], x['CH3COH_mol_gh'], x['HCOOH_mol_gh'], x['CH2O_mol_gh'], x['C2H4O2_mol_gh']), axis=1)
	exp_df['co2_prod_molg'] = exp_df.apply(lambda x: co2_production(x['CO_mol_g'], x['CH4_mol_g'], x['C2H4_mol_g'], x['C2H6_mol_g'], x['C3H6_mol_g'], x['C3H8_mol_g'], x['C4H8_mol_g'], x['C4H10_mol_g'], x['C5H10_mol_g'], x['C5H12_mol_g'], x['CH3OH_mol_g'], x['C2H5OH_mol_g'], x['CH3COH_mol_g'], x['HCOOH_mol_g'], x['CH2O_mol_g'], x['C2H4O2_mol_g']), axis=1)
	exp_df['co2_prod_molm2h'] = exp_df.apply(lambda x: co2_production(x['CO_mol_m2h'], x['CH4_mol_m2h'], x['C2H4_mol_m2h'], x['C2H6_mol_m2h'], x['C3H6_mol_m2h'], x['C3H8_mol_m2h'], x['C4H8_mol_m2h'], x['C4H10_mol_m2h'], x['C5H10_mol_m2h'], x['C5H12_mol_m2h'], x['CH3OH_mol_m2h'], x['C2H5OH_mol_m2h'], x['CH3COH_mol_m2h'], x['HCOOH_mol_m2h'], x['CH2O_mol_m2h'], x['C2H4O2_mol_m2h']), axis=1)

	# Calculating catalyst selectivity
	exp_df['h2_selectivity_molg'] = exp_df.apply(lambda x: selectivity( x['H2_mol_g'], x['CO_mol_g'], x['CH4_mol_g'], x['H2_mol_g'], x['CH3OH_mol_g']), axis=1)
	exp_df['ch4_selectivity_molg'] = exp_df.apply(lambda x: selectivity( x['CH4_mol_g'], x['CO_mol_g'], x['CH4_mol_g'], x['H2_mol_g'], x['CH3OH_mol_g']), axis=1)
	exp_df['co_selectivity_molg'] = exp_df.apply(lambda x: selectivity( x['CO_mol_g'], x['CO_mol_g'], x['CH4_mol_g'], x['H2_mol_g'], x['CH3OH_mol_g']), axis=1)
	exp_df['ch3oh_selectivity_molg'] = exp_df.apply(lambda x: selectivity( x['CH3OH_mol_g'], x['CO_mol_g'], x['CH4_mol_g'], x['H2_mol_g'], x['CH3OH_mol_g']), axis=1)
     
	print('['+str(datetime.now().time())[0:8]+'] Saving file in ~/data/processed/catalystsdata.csv')
	# Saving file
	exp_df.to_csv("/home/solarchem/data/processed/catalystsdata.csv", index=False, sep=",")

def main():
	cleaning_catalystdata()


if __name__ == '__main__':
    main()

