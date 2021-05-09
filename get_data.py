import requests

class generic_data_client:
    """
    A class to get and save data from given url in .csv format.
    ...
    Attributes
    ----------
    url : str
       url to download csv from
    name : str
       name to save the file with

    Methods
    -------
    get_data():
       downloads data from given url and saves it in data_files_csv folder.
    """
    def __init__(self,url,name):
        """
        Constructs all the necessary attributes for the generic_data_client object.

        Parameters
        ----------
           url : str
               url to download csv from
           name : str
               name to save the file with

        """
        self.url = url
        self.name = name

    def get_data(self):
        """
        downloads data from given url and saves it in data_files_csv folder.

        Returns
        -------
        1 or 0 According to when data is fetched and saved or when there was an http error while fetching
        """
        print("Getting {} ".format(self.name))
        data = requests.get(url=self.url)
        if data.status_code == 200:
            addr = 'data_files_csv/'+str(self.name) + '.csv'
            open(addr, 'wb').write(data.content)
            print("Data saved as {} in data_files_csv directory".format(addr))
            return 1;
        else:
            print("There was an error fetching  {} ,code: {}".format(self.name,data.status_code))
            return 0;


