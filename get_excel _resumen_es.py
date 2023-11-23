import pandas as pd 
import openpyxl

#Lee el archivo y lo transforma en un df
df_educ_sup=pd.read_csv('20230714_Titulados_Ed_Superior_2022_WEB.csv',sep=';',header=0)

#Filtra por la columna nivel_carrera_2 por solo carreras profesionales
df_educ_sup=df_educ_sup[df_educ_sup['nivel_carrera_2']=='Carreras Profesionales'] 

#Realiza un group by por la columna nomb_titulo_obtenido y transforma a excel 
df_count_carreras=df_educ_sup.groupby('nomb_titulo_obtenido').size().reset_index(name='Conteo')

df_count_carreras.to_excel('resumen_educacion_superior_2022.xlsx',index=False,sheet_name='res_carr')
