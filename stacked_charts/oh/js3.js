
Plotly.d3.csv("/data2.csv", function (err, rows) {
    

    function unpack(rows, key) {
        return rows.map(function (row){ return row[key]; });
    } 
    
    //console.log(rows.filter(d => d.ticker === 'weed').map(d => d.date))

    var co_ticker = rows.filter(d => d.ticker === 'oh')
    var co_dates = co_ticker.map((i,d) => d)
    var co_sales = co_ticker.map(d => d.sales)
    var co_cogs = co_ticker.map(d => d.cogs)
    var co_sga = co_ticker.map(d => d.sga)
    var traces = [
        { x: co_dates, y: co_cogs, stackgroup: 'one', groupnorm: 'percent',text:"COGS"},
        { x: co_dates, y: co_sga, stackgroup: 'one',text:"SGA" },
        { x: co_dates, y: co_sales, stackgroup: 'one',text:"SALES" }
    ]

    Plotly.newPlot('myDiv', traces, { title: 'OH: Revenue and sales' });
});

