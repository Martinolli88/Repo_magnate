import pandas as pd 
import openpyxl

#Lee el archivo y lo transforma en un df
df_educ_sup=pd.read_csv('20230714_Titulados_Ed_Superior_2022_WEB.csv',sep=';',header=0)

#Filtra por la columna nivel_carrera_2 por solo carreras profesionales
df_educ_sup=df_educ_sup[df_educ_sup['nivel_carrera_2']=='Carreras Profesionales'] 

#Realiza un group by por la columna nomb_titulo_obtenido y transforma a excel 
df_count_carreras=df_educ_sup.groupby('nomb_titulo_obtenido').size().reset_index(name='Conteo')

df_count_carreras.to_excel('resumen_educacion_superior_2022.xlsx',index=False,sheet_name='res_carr')

#Realiza un group by por nomb_inst y nomb_titulo_obtenido y luego lo escribe en una hoja del excel creado anteriormente
df_count_por_univ_carr=df_educ_sup.groupby(['nomb_inst','nomb_titulo_obtenido']).size().reset_index(name='Conteo')
with pd.ExcelWriter('resumen_educacion_superior_2022.xlsx', engine='openpyxl', mode='a') as writer:
    df_count_por_univ_carr.to_excel(writer, sheet_name='res_uni_carr', index=False)

#Obtiene las 10 carreras universitarias con más titulados en el año y lo escribe en una hoja en excel
df_top10=df_count_carreras.sort_values(by='Conteo',ascending=False)
df_top10=df_top10.head(10)

with pd.ExcelWriter('resumen_educacion_superior_2022.xlsx', engine='openpyxl', mode='a') as writer:
    df_top10.to_excel(writer, sheet_name='top_10_carr', index=False)

#Obtiene las 10 carreras por universidad que obtuvieron más egresados en el año y la transforma a excel
df_top_10_u_c=df_count_por_univ_carr.sort_values(by='Conteo',ascending=False)
df_top_10_u_c=df_top_10_u_c.head(10)

with pd.ExcelWriter('resumen_educacion_superior_2022.xlsx', engine='openpyxl', mode='a') as writer:
    df_top_10_u_c.to_excel(writer, sheet_name='top_10_u_c', index=False)