Plotly.d3.csv("../data/data1.csv", function (err, rows) {
    var plotDiv = document.getElementById('bsBarDiv');

    function unpack(rows, key) {
        return rows.map(function (row){ return row[key]; });
    } 
    
    //console.log(rows.filter(d => d.ticker === 'weed').map(d => d.date))
    var page_link = window.location.href
    var tickers = ['acb', 'apha', 'cron', 'fire', 'hexo', 'ogi', 'oh', 'ter', 'weed', 'wmd']
    for (i=0;i<tickers.length;i++) {
      if (page_link.endsWith(tickers[i])) {
        var page_ticker = tickers[i]
      }
    };
    var co_ticker = rows.filter(d => d.ticker === page_ticker)
    var co_dates = co_ticker.map((i,d) => d)
    var co_c_assets = co_ticker.map(d => d.current_assets)
    var co_nc_assets = co_ticker.map(d => d.non_assets)
    var co_liab = co_ticker.map(d => d.current_liabilities)
    var co_noliab = co_ticker.map(d => d.non_liabilities)
    var co_itdebt = co_ticker.map(d => d.it_debt)
    var co_equity = co_ticker.map(d => d.equity)


var trace1 = {
  x: co_dates,
  y: co_c_assets,
  name: 'Current Assets',
  type: 'bar'
};
var trace2 = {
  x: co_dates,
  y: co_nc_assets,
  name: 'Non-current Assets',
  type: 'bar'
};
var trace3 = {
  x: co_dates,
  y: co_liab,
  name: 'Current liabilities',
  type: 'bar'
 };
 var trace4 = {
    x: co_dates,
    y: co_noliab,
    name: 'Non-Current liabilities',
    type: 'bar'
 };
 var trace5 = {
    x: co_dates,
    y: co_itdebt,
    name: 'IT-debt',
    type: 'bar'
 };
 var trace6 = {
    x: co_dates,
    y: co_equity,
    name: 'Equity',
    type: 'bar'
 };
 
var data = [trace1, trace2, trace3, trace4,trace5,trace6];
var layout = {
  xaxis: {title: 'Financial Years'},
  yaxis: {title: 'Balance sheet elements'},
  barmode: 'relative',
  title: `${page_ticker}: Balance sheet`
};

Plotly.newPlot(plotDiv, data, layout);
});
