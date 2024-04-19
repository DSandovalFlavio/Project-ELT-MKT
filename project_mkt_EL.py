# %%
import pandas as pd
import requests
import pandas_gbq
from google.oauth2 import service_account
from datetime import datetime, timedelta
# %%
def get_data(start_date, end_date, path_file):
    """
    Esta función obtiene datos de una API y los guarda en un archivo local.

    Parámetros:
    start_date (str): La fecha de inicio para la consulta a la API en formato 'YYYY-MM-DD'.
    end_date (str): La fecha de fin para la consulta a la API en formato 'YYYY-MM-DD'.
    path_file (str): La ruta del archivo donde se guardarán los datos obtenidos.

    Retorna:
    None. Sin embargo, como efecto secundario, crea un nuevo archivo con los datos obtenidos de la API.
    """
    
    import json
    url = f'https://my.api.mockaroo.com/project_mkt_elt.json?start_date={start_date}&end_date={end_date}'
    headers = json.loads(open('credentials/mockaroo.json').read())
    r = requests.get(url, headers=headers)
    with open(path_file, 'wb') as f:
        f.write(r.content)
    print(f'{path_file} created')

def load_to_bigquery(path_file, source):
    """
    Esta función carga un archivo CSV a una tabla de BigQuery.

    Parámetros:
    path_file (str): La ruta del archivo CSV que se cargará en BigQuery.
    source (str): El nombre de la fuente de datos, que se utiliza para nombrar la tabla en BigQuery.

    Retorna:
    None. Sin embargo, como efecto secundario, carga los datos del archivo CSV en una tabla de BigQuery.
    """
    credentials = service_account.Credentials.from_service_account_file(
        'credentials/project-mkt-elt-0072df081010.json',
    )
    df = pd.read_csv(path_file)
    df = df.assign(source=source)
    df.Date = pd.to_datetime(df.Date)
    
    pandas_gbq.to_gbq(
    df, 
    f'bronce_mkt.{source}_raw', 
    project_id='project-mkt-elt', 
    if_exists='append',
    credentials=credentials
    )

def create_rango_fechas():
    """
    Esta función genera una lista de rangos de fechas. Cada rango de fechas es una lista de dos elementos, 
    donde el primer elemento es la fecha de inicio y el segundo es la fecha final. Los rangos de fechas se generan 
    para los años especificados en la lista 'anios' y para cada mes del año. Solo se generan rangos de fechas 
    para fechas anteriores a la fecha actual.

    Parámetros:
    Ninguno

    Retorna:
    range_dates (list): Una lista de listas. Cada sublista contiene dos elementos: la fecha de inicio y la fecha final 
    de un rango de fechas. Las fechas están en formato 'M/D/YYYY'.
    """
    anios = [2022, 2023, 2024]
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    now = datetime(datetime.now().year, datetime.now().month, 1).date()
    range_dates = []
    for anio in anios:
        for mes in meses:
            gen = (datetime(anio, mes, 1)).date()
            if gen < now:
                inicio = (datetime(anio, mes, 1)).strftime('%-m/%-d/%Y')
                if mes == 12:
                    final = (datetime(anio, mes, 31)).strftime('%-m/%-d/%Y')
                else:
                    final = (datetime(anio, mes+1, 1) - timedelta(days=1)).strftime('%-m/%-d/%Y')
                range_dates.append([inicio, final])
    return range_dates

def backfill_data(sources):
    """
    Esta función realiza un backfill de datos para una lista de fuentes de datos. Para cada fuente de datos, 
    se obtienen los datos para cada rango de fechas generado por la función 'create_rango_fechas', se guardan 
    los datos en un archivo CSV y luego se cargan los datos en BigQuery. Finalmente, se imprime un mensaje 
    indicando que se completó el backfill para la fuente de datos.

    Parámetros:
    sources (list): Una lista de fuentes de datos para las cuales se realizará el backfill de datos.

    Retorna:
    None. Sin embargo, como efecto secundario, realiza un backfill de datos para cada fuente de datos en la lista 'sources'.
    """
    rango_dete = create_rango_fechas()
    for source in sources:
        for rango in rango_dete:
            start_date = rango[0]
            end_date = rango[1]
            path_file = f'data/campaign_{source}_{start_date.replace('/', '-')}_{end_date.replace('/', '-')}.csv'
            get_data(start_date, end_date, path_file)
            load_to_bigquery(path_file, source)
        print(f'Backfill completed for {source}')

def update_data_montly(sources):
    """
    Esta función actualiza los datos mensualmente para una lista de fuentes de datos. Para cada fuente de datos, 
    se obtienen los datos para el rango de fechas del mes actual, se guardan los datos en un archivo CSV y luego 
    se cargan los datos en BigQuery. Finalmente, se imprime un mensaje indicando que se completó la actualización 
    para la fuente de datos y el rango de fechas.

    Parámetros:
    sources (list): Una lista de fuentes de datos para las cuales se actualizarán los datos.

    Retorna:
    None. Sin embargo, como efecto secundario, actualiza los datos para cada fuente de datos en la lista 'sources'.
    """
    start_date = (datetime(datetime.now().year, datetime.now().month, 1)).strftime('%-m/%-d/%Y')
    end_date = (datetime(datetime.now().year, datetime.now().month + 1, 1) - timedelta(days=1)).strftime('%-m/%-d/%Y')
    for source in sources:
        path_file = f'data/campaign_{source}_{start_date.replace('/', '-')}_{end_date.replace('/', '-')}.csv'
        get_data(start_date, end_date, path_file)
        load_to_bigquery(path_file, source)
        print(f'Update completed for {source}')
        print(f'between {start_date} and {end_date}')

# %%
sources = ['google_ads', 'youtube_ads', 'instagram_ads', 'twitter_ads', 'facebook_ads', 'email']

# backfill_data(sources) # funcion para cargar datos historicos
update_data_montly(sources) # funcion para cargar datos mensuales

# %%
