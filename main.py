from extract_data import data_frame,merged_data_frame,modify_data_frame
from get_data import generic_data_client

class data_analysis:
    """
       A class to respresent data_analysis task.
       ...
       Attributes
       ----------
       url1 : str
          url from where csv data file is to be downloaded and processed.
       url2 : str
          url from where 2nd csv data file is to be downloaded and processed.
    """
    def __init__(self,url1,url2):
        """
        Constructs all the necessary attributes for the data_analysis object.

        Parameters
        ----------
        url1 : str
          url from where csv data file is to be downloaded and processed.
        url2 : str
          url from where 2nd csv data file is to be downloaded and processed.
        """
        self.url1 = url1
        self.url2 = url2

    def __call__(self, *args, **kwargs):
        """
        fetch csv data from url, converts to data frames, merge data frames, add computed columns and rearrange
        columns and save th final csv file to the root project directory.
        Returns
        -------
        None
        """
        generic_data_client(url = self.url1,name='who_data').get_data()
        generic_data_client(url = self.url2,name='covid_data').get_data()
        who_csv_data = data_frame('who_csv_data').make_df()
        covid_csv_data = data_frame('covid_csv_data').make_df()
        merged_df = merged_data_frame(who_csv_data,covid_csv_data).merge_data()
        cols_added_df = modify_data_frame(merged_df).add_cols()
        cols_rearranged_df = modify_data_frame(cols_added_df).rearrange_cols()
        modify_data_frame(cols_rearranged_df).convert_to_csv()

url1 = 'https://query.data.world/s/rvgwskwqfej4ns6ftn662qsuxpgk73'
url2 = 'https://storage.googleapis.com/kagglesdsdata/datasets/494766/1402868/country_wise_latest.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20210507%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210507T110145Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=2e35579b41755e849e69918c8ec1e0b32840b73326818811b5645001acc58cc1a1a24b8f19698d330ad00f2d33e515995b724181cfea1971f4eda8a262fed7c93649fbfd02e2ebaa606085355ea2448fbbebb6bb5198973549092c814cfd693ece2101ac0e07d858ebb249592625206023e59bdc1f9b9204eb6514fe97094055b3f75aa7e6bf006267f98bf1611f904d540bea2681d8c8a5aa46197116a514ecccf35bfc9b1be6fd94fdcd2bea6a64022d18312f26038c8b19c8d31201f3b7a6fc6ba752f1e2ff57359697a0cb49edfb45f877b3c45ba39876e656a292671f5cf1685b01b645120dc0bd0cc44acbfb7918bda5b76d4dccbef63818a180fe329d'
solution  = data_analysis(url1=url1,url2=url2)
solution()