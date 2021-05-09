import pandas as pd

class data_frame:
    """
       A class to represent a data frame by name.
       ...
       Attributes
       ----------
       name : str
          name to save the file with

       Methods
       -------
       make_df():
          make df according to self.name. if name is who_csv_data then who_csv_data dataframe will be returned,
          if name is covid_csv_data then covid_csv_data dataframe will be returned
       """
    def __init__(self,name):
        """
        Constructs all the necessary attributes for the data_frame object.

        Parameters
        ----------
        name : str
          name to save the file with
        """
        self.name = name

    def make_df(self):
        """
            make df according to self.name. if name is who_csv_data then who_csv_data dataframe will be returned,
            if name is covid_csv_data then covid_csv_data dataframe will be returned

            Returns
            -------
            Dataframe object created by reading csv through pandas
        """
        if(self.name == 'who_csv_data'):
            chunksize = 10000
            tfr = pd.read_csv('data_files_csv/who_data.csv', chunksize=chunksize, iterator=True)
            who_csv_data = pd.concat(tfr, ignore_index=True)
            return who_csv_data
        elif(self.name == 'covid_csv_data'):
            covid_csv_data = pd.read_csv("data_files_csv/covid_data.csv")
            covid_csv_data.rename(columns={"Country/Region": "Country"}, inplace=True)
            return covid_csv_data
        else:
            print('Name parameter wrong. choose between covid_csv_data or who_csv_data')


class merged_data_frame:
    """
       A class to represent a merged data_frame from two data_frames.
       ...
       Attributes
       ----------
       df1 : <class 'pandas.core.frame.DataFrame'>
          1st data_frame to merge with 2nd
       df2 : <class 'pandas.core.frame.DataFrame'>
          2nd data_frame to merge with 1st

       Methods
       -------
       merge_data():
          right merge two dataframes (df2,df1,how=right). and remove columns if it is fully empty.
    """

    def __init__(self,df1,df2):
        """
        Constructs all the necessary attributes for the merged_data_frame object.

        Parameters
        ----------
        df1 : <class 'pandas.core.frame.DataFrame'>
          1st data_frame to merge with 2nd
        df2 : <class 'pandas.core.frame.DataFrame'>
          2nd data_frame to merge with 1st
        """
        self.df1 = df1
        self.df2 = df2
    def merge_data(self):
        """
        right merge two dataframes (df2,df1,how=right). and remove columns if it is fully empty.

        Returns
        -------
        Final Dataframe object after merging and removing empty column
        """
        left_merged = pd.merge(self.df2, self.df1, on="Country", how="right")
        left_merged.dropna(axis=1, how='all', inplace=True)
        return left_merged

class modify_data_frame:
    """
       A class to represent a modified data_frame.
       ...
       Attributes
       ----------
       df : <class 'pandas.core.frame.DataFrame'>
          data_frame to modify

       Methods
       -------
       add_cols():
          adds 'Recovered_percentage' and 'New_recovered_percentage_from_new_cases' computed columns to data_frame
       rearrange_cols():
          moves 'Recovered_percentage' and 'New_recovered_percentage_from_new_cases' computed columns to 1st and 2nd column in data_frame
       convert_to_csv():
          converts data_frame to csv and saves in root folder by name final.csv
    """
    def __init__(self,df):
        """
        Constructs all the necessary attributes for the modify_data_frame object.

        Parameters
        ----------
        df : <class 'pandas.core.frame.DataFrame'>
          data_frame to modify
        """
        self.df = df
    def add_cols(self):
        """
        adds 'Recovered_percentage' and 'New_recovered_percentage_from_new_cases' computed columns to data_frame

        Returns
        -------
        Final Dataframe object after adding computed columns column
        """
        self.df["Recovered_percentage"] = (self.df["Recovered"] / self.df["Confirmed"]) * 100
        self.df["New_recovered_percentage_from_new_cases"] = (self.df["New recovered"] / self.df["New cases"]) * 100

        print("Added computed columns")
        return self.df
    def rearrange_cols(self):
        """
        moves 'Recovered_percentage' and 'New_recovered_percentage_from_new_cases' computed columns to 1st and 2nd column in data_frame

        Returns
        -------
        Final Dataframe object after rearranging columns.
        """
        second_column = self.df.pop('Recovered_percentage')
        self.df.insert(1, 'Recovered_percentage', second_column)
        third_column = self.df.pop('New_recovered_percentage_from_new_cases')
        self.df.insert(2, 'New_recovered_percentage_from_new_cases', third_column)
        print("Rearranged columns")
        return self.df

    def convert_to_csv(self):
        """
        converts dataframe to csv
        Returns
        -------
        None
        """
        print("Saving result in final.csv in root project directory.")
        self.df.to_csv('final.csv')


