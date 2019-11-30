var is_tickers = [{% for ticker in is_tickers %}
    "{{ ticker }}",
    {% endfor %}];

var is_dates = [{% for date in is_dates %}
    "{{ date }}",
    {% endfor %}];

var is_sales = [{% for salesDatum in is_sales %}
    "{{ salesDatum }}",
    {% endfor %}];

var is_cogs = [{% for cogsDatum in is_cogs %}
    "{{ cogsDatum }}",
    {% endfor %}];
    
var is_sga = [{% for sgaDatum in is_sga %}
    "{{ sgaDatum }}",
    {% endfor %}];


function(buildStackedArea) {
    nv.addGraph(function() {
        var chart = nv.models.stackedArea()
        .margin({right: 100})
        .x(is_dates)
        .y(is_sales)
        .useInteractiveGuideline(true)
        .rightAlignYAxis(true)
        .transitionDuration(500)
        .showControls(true)
        .clipEdge(true);

        chart.xAxis
            .tickFormath(function(d) {
                return d3.time.format('%x')(new Date(d))
        });

        chart.yAxis
            .tickFormat(d3.format(',.2f'));
        
        d3.select'(#chart svg')
            .datum(data)
            .call(chart);
        
        nv.utils.windowResize(chart.update);

        return chart;
    });
};
