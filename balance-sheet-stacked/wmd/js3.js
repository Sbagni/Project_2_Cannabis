
Plotly.d3.csv("/data1.csv", function (err, rows) {
    //var plotDiv = document.getElementById('myDiv');

    function unpack(rows, key) {
        return rows.map(function (row){ return row[key]; });
    } 
    
    //console.log(rows.filter(d => d.ticker === 'weed').map(d => d.date))

    var co_ticker = rows.filter(d => d.ticker === 'wmd')
    var co_dates = co_ticker.map((i,d) => d)
    var co_c_assets = co_ticker.map(d => d.current_assets)
    var co_nc_assets = co_ticker.map(d => d.non_assets)
    var co_liab = co_ticker.map(d => d.current_liabilities)
    var co_noliab = co_ticker.map(d => d.non_liabilities)
    var co_itdebt = co_ticker.map(d => d.it_debt)
    var co_equity = co_ticker.map(d => d.equity)

    var traces = [
        { x: co_dates, y: co_c_assets, stackgroup: 'one', groupnorm: 'percent',text:"Current-assets"},
        { x: co_dates, y: co_nc_assets, stackgroup: 'one',text:"Non-current-assets" },
        { x: co_dates, y: co_liab, stackgroup: 'one',text:"Current-liabilities" },
        { x: co_dates, y: co_noliab, stackgroup: 'one',text:"Non current-liabilities" },
        { x: co_dates, y: co_itdebt, stackgroup: 'one',text:"IT-Debt," },
        { x: co_dates, y: co_equity, stackgroup: 'one',text:"Equity" }
    ]

    Plotly.newPlot('myDiv', traces, { title: 'WMD: Balance sheet' });
});

