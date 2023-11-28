from typing import Optional
import pandas as pd
import numpy as np


def filtering(host_data: pd.DataFrame,
           postcode: Optional[str] = np.nan,
           room_type: Optional[str] = np.nan):
    """
    function takes a dataframe and filters based on parameters provied returning a table of matches
    :param postcode: host postcode
    :param room_type: type of room from host
    :return: a dataframe matching hosts
    """
    host_data[["postcode_first", "postcode_last"]] = host_data.Postcode.str.split(expand=True)
    post_filter = host_data[host_data.postcode_first == postcode]
    room_filter = host_data[host_data["Accomodation type"] == room_type]
    if postcode is not np.nan:
        host_data = host_data[host_data.postcode_first == postcode]
    if room_type is not np.nan:
        host_data = host_data[host_data["Accomodation type"] == room_type]
    return host_data, post_filter, room_filter





