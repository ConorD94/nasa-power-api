from typing import List, Union, Optional
from pathlib import Path
from datetime import date, datetime
import requests
import pandas as pd
import os
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


class PowerAPI:
    """
    Query the NASA Power API.
    Check https://power.larc.nasa.gov/ for documentation
    Attributes
    ----------
    url : str
        Base URL
    """
    url = "https://power.larc.nasa.gov/api/temporal/hourly/point?"

    def __init__(self,
                 start: Union[date, datetime, pd.Timestamp],
                 end: Union[date, datetime, pd.Timestamp],
                 long: float, lat: float,
                 use_long_names: bool = False,
                 parameter: Optional[List[str]] = None):
        """
        Parameters
        ----------
        start: Union[date, datetime, pd.Timestamp]
            Start time. Hour resolution is supported.
        end: Union[date, datetime, pd.Timestamp]
            End time. Hour resolution is supported.
        long: float
            Longitude as float
        lat: float
            Latitude as float
        use_long_names: bool
            NASA provides both identifier and human-readable names for the fields. If set to True this will parse
            the data with the latter
        parameter: Optional[List[str]]
            List with the parameters to query.
            Default is ['T2M', 'TS', 'T2MDEW', 'T2MWET', 'QV2M', 'RH2M',
                        'PRECTOTCORR', 'PS', 'WS10M', 'WS50M']
        """
        self.start = start
        self.end = end
        self.long = long
        self.lat = lat
        self.use_long_names = use_long_names
        if parameter is None:
            self.parameter = ['T2M', 'TS', 'T2MDEW', 'T2MWET', 'QV2M', 'RH2M',
                              'PRECTOTCORR', 'PS', 'WS10M', 'WS50M']

        self.request = self._build_request()

    def _build_request(self) -> str:
        """
        Build the request
        Returns
        -------
        str
            Full request including parameter
        """
        r = self.url
        r += f"parameters={(',').join(self.parameter)}"
        r += '&community=RE'
        r += f"&longitude={self.long}"
        r += f"&latitude={self.lat}"
        r += f"&start={self.start.strftime('%Y%m%d%H')}"
        r += f"&end={self.end.strftime('%Y%m%d%H')}"
        r += '&format=JSON'

        return r

    def get_weather(self) -> pd.DataFrame:
        """
        Main method to query the weather data
        Returns
        -------
        pd.DataFrame
            Pandas DataFrame with DateTimeIndex
        """

        response = requests.get(self.request)

        assert response.status_code == 200

        data_json = response.json()

        records = data_json['properties']['parameter']

        df = pd.DataFrame.from_dict(records)

        return df

