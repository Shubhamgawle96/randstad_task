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

