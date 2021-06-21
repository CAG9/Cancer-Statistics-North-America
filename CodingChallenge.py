import numpy as np
import pandas as pd
import seaborn as sns
import re 
from matplotlib import pyplot as plt


def Get_ICD_Gruoups(Mexico_newcases,Mexico_mortality,Usa_newcases,Usa_mortality,Canada_newcases,Canada_mortality,ICD_Codes):

    # Store info from icd goups
    Mexico_newcases_icd = [0]*len(ICD_Codes)
    Mexico_mortality_icd = [0]*len(ICD_Codes)
    Usa_newcases_icd = [0]*len(ICD_Codes)
    Usa_mortality_icd = [0]*len(ICD_Codes)
    Canada_newcases_icd = [0]*len(ICD_Codes)
    Canada_mortality_icd = [0]*len(ICD_Codes)

    for country in range(3):
        C7A_flag = False
        C7B_flag = False
        count = 0 # to check C7A and C7B appear
        for icd_code in ICD_Codes:
            # Create bounds to check the range of icd_codes
            bounds  = re.findall(r'\d+',icd_code)
            lower_bounds = int(bounds[0])
            upper_bounds = int(bounds[1])
            if count == 13:
                C7A_flag = True
            if count == 14:
                C7B_flag = True
            count+=1
            for cancer_info in range(1,len(Mexico_newcases)):#all dataset have the same length
                if country == 0:
                    if C7A_flag == False and C7B_flag == False:#check if there is not C7A and C7B codes
                        # Incidence
                        inner_codes_newcases = re.findall(r'\d+',Mexico_newcases.iloc[cancer_info,0])# get the  codes in the dataset
                        inner_codes_newcases = np.array(inner_codes_newcases)
                        inner_codes_newcases = inner_codes_newcases.astype(int) #Convert icd codes to integers
                        # Check if exist a number out of the bounds
                        inner_codes_newcases_minus  = inner_codes_newcases >= lower_bounds
                        inner_codes_newcases_greater = inner_codes_newcases <= upper_bounds
                        complete_inner_codes_newcases = inner_codes_newcases_minus * inner_codes_newcases_greater

                        #Mortality
                        inner_codes_mortality = re.findall(r'\d+',Mexico_mortality.iloc[cancer_info,0])
                        inner_codes_mortality = np.array(inner_codes_mortality)
                        inner_codes_mortality = inner_codes_mortality.astype(int)
                        #check if exist a number out of the bounds
                        inner_codes_mortality_minus  = inner_codes_mortality >= lower_bounds
                        inner_codes_mortality_greater = inner_codes_mortality <= upper_bounds
                        complete_inner_codes_mortality = inner_codes_mortality_minus * inner_codes_mortality_greater
                        if not False in complete_inner_codes_newcases:
                            Mexico_newcases_icd[count-1] += Mexico_newcases.iloc[cancer_info,2]
                        if not False in complete_inner_codes_mortality:
                            Mexico_mortality_icd[count-1] += Mexico_mortality.iloc[cancer_info,2]

                    else: # Evaluating C7A and C7B Groups
                        if C7A_flag == True:
                            if "C7A" in Mexico_newcases.iloc[cancer_info,0]:
                                Mexico_newcases_icd[count-1] += Mexico_newcases.iloc[cancer_info,2]

                            if "C7A" in Mexico_mortality.iloc[cancer_info,0]:
                                Mexico_mortality_icd[count-1] += Mexico_mortality.iloc[cancer_info,2]

                            C7A_flag = False

                        if C7B_flag == True:
                            if "C7B" in Mexico_newcases.iloc[cancer_info,0]:
                                Mexico_newcases_icd[count-1] += Mexico_newcases.iloc[cancer_info,2]

                            if "C7B" in Mexico_mortality.iloc[cancer_info,0]:
                                Mexico_mortality_icd[count-1] += Mexico_mortality.iloc[cancer_info,2]

                            C7B_flag = False

                # Do the same for the last countries
                elif country == 1:
                    if C7A_flag == False and C7B_flag == False:
                        # Incidence
                        inner_codes_newcases = re.findall(r'\d+',Usa_newcases.iloc[cancer_info,0])
                        inner_codes_newcases = np.array(inner_codes_newcases)
                        inner_codes_newcases = inner_codes_newcases.astype(int) 
                        inner_codes_newcases_minus  = inner_codes_newcases >= lower_bounds
                        inner_codes_newcases_greater = inner_codes_newcases <= upper_bounds
                        complete_inner_codes_newcases = inner_codes_newcases_minus * inner_codes_newcases_greater

                        # Mortality
                        inner_codes_mortality = re.findall(r'\d+',Usa_mortality.iloc[cancer_info,0])
                        inner_codes_mortality = np.array(inner_codes_mortality)
                        inner_codes_mortality = inner_codes_mortality.astype(int)
                        inner_codes_mortality_minus  = inner_codes_mortality >= lower_bounds
                        inner_codes_mortality_greater = inner_codes_mortality <= upper_bounds
                        complete_inner_codes_mortality = inner_codes_mortality_minus * inner_codes_mortality_greater

                        if not False in complete_inner_codes_newcases:
                            Usa_newcases_icd[count-1] += Usa_newcases.iloc[cancer_info,2]
                        if not False in complete_inner_codes_mortality:
                            Usa_mortality_icd[count-1] += Usa_mortality.iloc[cancer_info,2]

                    else: 
                        if C7A_flag == True:
                            if "C7A" in Usa_newcases.iloc[cancer_info,0]:
                                Usa_newcases_icd[count-1] += Usa_newcases.iloc[cancer_info,2]

                            if "C7A" in Usa_mortality.iloc[cancer_info,0]:
                                Usa_mortality_icd[count-1] += Usa_mortality.iloc[cancer_info,2]

                            C7A_flag = False

                        if C7B_flag == True:
                            if "C7B" in Usa_newcases.iloc[cancer_info,0]:
                                Usa_newcases_icd[count-1] += Usa_newcases.iloc[cancer_info,2]

                            if "C7B" in Usa_mortality.iloc[cancer_info,0]:
                                Usa_mortality_icd[count-1] += Usa_mortality.iloc[cancer_info,2]

                            C7B_flag = False

                if country == 2:
                    if C7A_flag == False and C7B_flag == False:
                        # Incidence
                        inner_codes_newcases = re.findall(r'\d+',Canada_newcases.iloc[cancer_info,0])
                        inner_codes_newcases = np.array(inner_codes_newcases)
                        inner_codes_newcases = inner_codes_newcases.astype(int) 
                        inner_codes_newcases_minus  = inner_codes_newcases >= lower_bounds
                        inner_codes_newcases_greater = inner_codes_newcases <= upper_bounds
                        complete_inner_codes_newcases = inner_codes_newcases_minus * inner_codes_newcases_greater

                        # Mortality
                        inner_codes_mortality = re.findall(r'\d+',Canada_mortality.iloc[cancer_info,0])
                        inner_codes_mortality = np.array(inner_codes_mortality)
                        inner_codes_mortality = inner_codes_mortality.astype(int)
                        inner_codes_mortality_minus  = inner_codes_mortality >= lower_bounds
                        inner_codes_mortality_greater = inner_codes_mortality <= upper_bounds
                        complete_inner_codes_mortality = inner_codes_mortality_minus * inner_codes_mortality_greater

                        if not False in complete_inner_codes_newcases:
                            Canada_newcases_icd[count-1] += Canada_newcases.iloc[cancer_info,2]
                        if not False in complete_inner_codes_mortality:
                            Canada_mortality_icd[count-1] += Canada_mortality.iloc[cancer_info,2]

                    else: 
                        if C7A_flag == True:
                            if "C7A" in Canada_newcases.iloc[cancer_info,0]:
                                Canada_newcases_icd[count-1] += Canada_newcases.iloc[cancer_info,2]

                            if "C7A" in Canada_mortality.iloc[cancer_info,0]:
                                Canada_mortality_icd[count-1] += Canada_mortality.iloc[cancer_info,2]

                            C7A_flag = False

                        if C7B_flag == True:
                            if "C7B" in Canada_newcases.iloc[cancer_info,0]:
                                Canada_newcases_icd[count-1] += Canada_newcases.iloc[cancer_info,2]

                            if "C7B" in Canada_mortality.iloc[cancer_info,0]:
                                Canada_mortality_icd[count-1] += Canada_mortality.iloc[cancer_info,2]

                            C7B_flag = False
    # Create Region data
    North_america_newcases = np.array(Mexico_newcases_icd)+np.array(Usa_newcases_icd)+np.array(Canada_newcases_icd)
    North_america_mortality = np.array(Mexico_mortality_icd)+np.array(Usa_mortality_icd)+np.array(Canada_mortality_icd)
    Groups = np.array([North_america_newcases,North_america_mortality,Mexico_newcases_icd,Mexico_mortality_icd,Usa_newcases_icd,Usa_mortality_icd,Canada_newcases_icd,Canada_mortality_icd])
    return Groups


def Create_Table(data,countries,Info,index_name,index_column):
    df = pd.DataFrame(data.T,
                 index = index_column ,
                 columns = [countries,
                            Info])
    df.index.name = index_name
    return df
    

def Create_DataFrame_to_Plot(ICD_Gropus_Data,Region,Country1,Country2,Country3):
    Amount_of_CountriesRegion = 4
    ICD_Codes_Length = len(ICD_Gropus_Data[0])
    incidence_data = np.concatenate((ICD_Gropus_Data[0],ICD_Gropus_Data[2],ICD_Gropus_Data[4],ICD_Gropus_Data[6]), axis=None)
    mortality_data = np.concatenate((ICD_Gropus_Data[1],ICD_Gropus_Data[3],ICD_Gropus_Data[5],ICD_Gropus_Data[7]), axis=None)
    New_codes = ICD_Codes * Amount_of_CountriesRegion
    Countries_name = [Region]*(ICD_Codes_Length)+ [Country1]*(ICD_Codes_Length) + [Country2]*(ICD_Codes_Length)+[Country3]*(ICD_Codes_Length)
    # Create a new dataframe
    new_data = {'Incidence':incidence_data , 'Mortality': mortality_data,'ICD_Groups': New_codes, 'Countries':Countries_name }
    new_df = pd.DataFrame(data=new_data)
    return new_df





if __name__ == "__main__":


    # Import datasets
    Canada_mortality = pd.read_csv("ChallengeCancer/challengeCancer/canada-mortality.csv",index_col = False)
    Canada_newcases = pd.read_csv("ChallengeCancer/challengeCancer/canada-newcases.csv",index_col = False)
    Usa_mortality = pd.read_csv("ChallengeCancer/challengeCancer/usa-mortality.csv",index_col = False)
    Usa_newcases = pd.read_csv("ChallengeCancer/challengeCancer/usa-newcases.csv",index_col = False)
    Mexico_mortality = pd.read_csv("ChallengeCancer/challengeCancer/mexico-mortality.csv",index_col = False)
    Mexico_newcases = pd.read_csv("ChallengeCancer/challengeCancer/mexico-newcases.csv",index_col = False)

    # Define Codes Groups
    ICD_Codes = ['C00-C14','C15-C26','C30-C39','C40-C41','C43-C44','C45-C49',
                        'C50-C50','C51-C58','C60-C63','C64-C68','C69-C72','C73-C75',
                        'C76-C80','C7A-C7A','C7B-C7B','C81-C96']

    # Collect Countries and region names
    # For the initial purpose, type in this order : North America, Mexico, USA, Canada
    print("Type Region's Name")
    Region = str(input())
    print("Type First Country's Name")
    Country1 = str(input())
    print("Type Second Country's Name")
    Country2 = str(input())
    print("Type Third Country's Name")
    Country3 = str(input())



    # Store data for create the table
    countries = [Region, Region, Country1, Country1, Country2, Country2, Country3, Country3]
    Column_Info = ["Incidence","Mortality","Incidence","Mortality","Incidence","Mortality","Incidence","Mortality"]
    index_name = 'ICD groups'



    # Task 1
    # Pass the countries in the same order you wrote them
    ICD_Gropus_Data = Get_ICD_Gruoups(Mexico_newcases,Mexico_mortality,Usa_newcases,Usa_mortality,Canada_newcases,Canada_mortality,ICD_Codes)
    Final_table = Create_Table(ICD_Gropus_Data,countries,Column_Info,index_name,ICD_Codes)
    print(Final_table)

    # Task 2
    Plotting_data = Create_DataFrame_to_Plot(ICD_Gropus_Data,Region,Country1,Country2,Country3)
    # Plotting
    chart = sns.scatterplot(data =Plotting_data, x = "Incidence", y = "Mortality",hue = "Countries",
                size = "Incidence",sizes=(40, 300),legend = "brief" )
    plt.show()




































