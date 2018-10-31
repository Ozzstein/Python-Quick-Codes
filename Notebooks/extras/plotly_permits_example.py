# Get this figure: fig = py.get_figure("https://plot.ly/~damoncrockett/663/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~damoncrockett/663/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="Discretionary Permit Counts by Year", fileopt="extend"))
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~damoncrockett/663/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
# py.sign_in('username', 'api_key')
trace1 = Scatter(
    x=['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014'],
    y=[239, 268, 216, 164, 132, 95, 61, 91, 74, 77, '98'],
    name='cdp',
    uid='753d1a',
    visible=True,
    xsrc='damoncrockett:661:6d8370',
    ysrc='damoncrockett:661:b55dce'
)
trace2 = Scatter(
    x=['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014'],
    y=[51, 81, 81, 64, 61, 96, 49, 70, 62, 40, '77'],
    name='cup',
    uid='443dc4',
    visible=True,
    xsrc='damoncrockett:661:6d8370',
    ysrc='damoncrockett:661:f1b927'
)
trace3 = Scatter(
    x=['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014'],
    y=[128, 166, 146, 113, 116, 110, 64, 79, 74, 68, '72'],
    name='sdp',
    uid='a357d6',
    xsrc='damoncrockett:661:6d8370',
    ysrc='damoncrockett:661:688f10'
)
trace4 = Scatter(
    x=['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014'],
    y=[23, 39, 39, 33, 38, 25, 12, 19, 17, 25, '33'],
    name='row',
    uid='aa08d4',
    visible=True,
    xsrc='damoncrockett:661:6d8370',
    ysrc='damoncrockett:661:3329da'
)
trace5 = Scatter(
    x=['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014'],
    y=[19, 21, 35, 33, 27, 13, 12, 13, 15, 33, '28'],
    name='ndp',
    uid='ac7e1e',
    visible=True,
    xsrc='damoncrockett:661:6d8370',
    ysrc='damoncrockett:661:12814b'
)
trace6 = Scatter(
    x=['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014'],
    y=[49, 56, 65, 37, 44, 35, 22, 39, 39, 38, '26'],
    name='pdp',
    uid='b0203e',
    visible=True,
    xsrc='damoncrockett:661:6d8370',
    ysrc='damoncrockett:661:9d990f'
)
trace7 = Scatter(
    x=['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014'],
    y=[182, 328, 84, 34, 20, 13, 5, 5, 13, 17, '25'],
    name='tmap',
    uid='b49e3b',
    visible=True,
    xsrc='damoncrockett:661:6d8370',
    ysrc='damoncrockett:661:6e7cec'
)
trace8 = Scatter(
    x=['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014'],
    y=[29, 46, 67, 47, 67, 62, 31, 40, 42, 42, '23'],
    name='nup',
    uid='e10662',
    visible=True,
    xsrc='damoncrockett:661:6d8370',
    ysrc='damoncrockett:661:9f7593'
)
trace9 = Scatter(
    x=['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014'],
    y=[125, 159, 139, 77, 37, 23, 14, 12, 13, 10, '18'],
    name='mapw',
    uid='37456b',
    visible=True,
    xsrc='damoncrockett:661:6d8370',
    ysrc='damoncrockett:661:0a370d'
)
data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9])
layout = Layout(
    autosize=True,
    height=556,
    showlegend=True,
    title='Discretionary Permit Counts by Year',
    width=1022,
    xaxis=XAxis(
        autorange=True,
        nticks=13,
        range=[2003.3881000676133, 2014.6118999323867],
        title='Application Year',
        type='linear'
    ),
    yaxis=YAxis(
        autorange=True,
        nticks=13,
        range=[-17.01163493502569, 350.0116349350257],
        title='Count',
        type='linear'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)