 $(document).ready(function () {

     //CHART 1
            var plot1 = $.jqplot('chart1', [[3, 7, 9, 1, 5, 3, 8, 2, 5]], {
                animate: true,
                // Will animate plot on calls to plot1.replot({resetAxes:true})
                animateReplot: true,
                cursor: {
                    show: true,
                    zoom: true,
                    looseZoom: true,
                    showTooltip: true
                },
                series: [
                    {
                        color: '#ff9937'
                    }
                ],
                axesDefaults: {
                    labelRenderer: $.jqplot.CanvasAxisLabelRenderer
                },
                seriesDefaults: {
                    rendererOptions: {
                        smooth: true
                    }
                },
                grid: {
                    drawGridLines: true,
                    gridLineColor: '#cccccc',
                    background: '#ffffff',
                    borderColor: '#ffffff',
                    borderWidth: 2.0,
                    shadow: false,
                    renderer: $.jqplot.CanvasGridRenderer,
                    rendererOptions: {}
                },
                axes: {

                    xaxis: {
                        label: "Month 2017",
                        pad: 0,
                        tickOptions: {
                            showGridline: false
                        }
                    },
                    yaxis: {
                        label: "Total Number of Users"
                    }
                }
            });
        });
      
//CHART 2

        $(document).ready(function () {
            $.jqplot.config.enablePlugins = true;
            var s2 = [2, 6, 7, 10];
            var ticks = ['JAN ', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP'];

            plot2 = $.jqplot('chart2', [s2], {
                // Only animate if we're not using excanvas (not in IE 7 or IE 8)..
                animate: !$.jqplot.use_excanvas,
                seriesDefaults: {
                    renderer: $.jqplot.BarRenderer,
                    pointLabels: { show: true }
                },
                series: [
                    {
                        color: '#6dba54'
                    }
                ],
                grid: {
                    drawGridLines: true,
                    gridLineColor: '#cccccc',
                    background: '#ffffff',
                    borderColor: '#ffffff',
                    borderWidth: 2.0,
                    shadow: false,
                    renderer: $.jqplot.CanvasGridRenderer,
                    rendererOptions: {}
                },
                axes: {
                    xaxis: {
                        label: "Month 2017",
                        renderer: $.jqplot.CategoryAxisRenderer,
                        ticks: ticks,
                        tickOptions: {
                            showGridline: false
                        }
                    },
                    yaxis: {
                        label: "Total Number of Manual Downloded"
                    }
                },
                highlighter: { show: false }
            });

            $('#chart2').bind('jqplotDataClick',
                function (ev, seriesIndex, pointIndex, data) {
                    $('#info2').html('series: ' + seriesIndex + ', point: ' + pointIndex + ', data: ' + data);
                }
            );
        });


//CHART 3

        $(document).ready(function () {
            $.jqplot.config.enablePlugins = true;
            var s21 = [2, 6, 7, 10, 12, 15, 15, 20];
            var ticks = ['JAN ', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP'];

            plot3 = $.jqplot('chart3', [s21], {
                // Only animate if we're not using excanvas (not in IE 7 or IE 8)..
                animate: !$.jqplot.use_excanvas,
                seriesDefaults: {
                    renderer: $.jqplot.BarRenderer,
                    pointLabels: { show: true }
                },
                grid: {
                    drawGridLines: true,
                    gridLineColor: '#cccccc',
                    background: '#ffffff',
                    borderColor: '#ffffff',
                    borderWidth: 2.0,
                    shadow: false,
                    renderer: $.jqplot.CanvasGridRenderer,
                    rendererOptions: {}
                },
                axes: {
                    xaxis: {
                        label: "Month 2017",
                        renderer: $.jqplot.CategoryAxisRenderer,
                        ticks: ticks,
                        tickOptions: {
                            showGridline: false
                        }
                    },
                    yaxis: {
                        label: "Total Number of Warranties Claimed"
                    }
                },
                highlighter: { show: false }
            });

            $('#chart2').bind('jqplotDataClick',
                function (ev, seriesIndex, pointIndex, data) {
                    $('#info2').html('series: ' + seriesIndex + ', point: ' + pointIndex + ', data: ' + data);
                }
            );

            //Chart 4
            $(document).on('click', '.bjqs-controls', function(){
                setTimeout(function(){
                    var s4 = [0, 5, 7, 10, 12, 15, 18, 20];
                    var s4_1 = [2, 6, 7, 2, 12, 15, 15, 20];
                    var plot4 = $.jqplot('chart4', [s4, s4_1], {
                        animate: true,
                        // Will animate plot on calls to plot1.replot({resetAxes:true})
                        animateReplot: true,
                        cursor: {
                            show: true,
                            zoom: true,
                            looseZoom: true,
                            showTooltip: true
                        },
                        series: [
                            
                                {color: '#3cbb4c'},
                                {color: '#40ccf1'}
                            
                        ],
                        axesDefaults: {
                            labelRenderer: $.jqplot.CanvasAxisLabelRenderer
                        },
                        seriesDefaults: {
                            rendererOptions: {
                                smooth: true
                            }
                        },
                        grid: {
                            drawGridLines: true,
                            gridLineColor: '#cccccc',
                            background: '#ffffff',
                            borderColor: '#ffffff',
                            borderWidth: 2.0,
                            shadow: false,
                            renderer: $.jqplot.CanvasGridRenderer,
                            rendererOptions: {}
                        },
                        axes: {
        
                            xaxis: {
                                label: "Month 2017",
                                pad: 0,
                                tickOptions: {
                                    showGridline: false
                                }
                            },
                            yaxis: {
                                label: "Total Number of Users"
                            }
                        }
                    });
        
                    //Chart 5
                    var s5 = [0, 5, 7, 10, 12, 15, 18, 20];
                    var s5_1 = [2, 6, 7, 2, 12, 15, 15, 20];
                    var plot5 = $.jqplot('chart5', [s5, s5_1], {
                        animate: true,
                        // Will animate plot on calls to plot1.replot({resetAxes:true})
                        animateReplot: true,
                        cursor: {
                            show: true,
                            zoom: true,
                            looseZoom: true,
                            showTooltip: true
                        },
                        series: [
                            {
                                color: '#39308e'
                            },
                            {
                                color: '#e84e54'
                            }
                        ],
                        axesDefaults: {
                            labelRenderer: $.jqplot.CanvasAxisLabelRenderer
                        },
                        seriesDefaults: {
                            rendererOptions: {
                                smooth: true
                            }
                        },
                        grid: {
                            drawGridLines: true,
                            gridLineColor: '#cccccc',
                            background: '#ffffff',
                            borderColor: '#ffffff',
                            borderWidth: 2.0,
                            shadow: false,
                            renderer: $.jqplot.CanvasGridRenderer,
                            rendererOptions: {}
                        },
                        axes: {
        
                            xaxis: {
                                label: "Month 2017",
                                pad: 0,
                                tickOptions: {
                                    showGridline: false
                                }
                            },
                            yaxis: {
                                label: "Total Number of Users"
                            }
                        }
                    });
    
    
                    var plot6 = $.jqplot('chart6', [[3, 7, 9, 1, 5, 3, 8, 2, 5]], {
                        animate: true,
                        // Will animate plot on calls to plot1.replot({resetAxes:true})
                        animateReplot: true,
                        cursor: {
                            show: true,
                            zoom: true,
                            looseZoom: true,
                            showTooltip: true
                        },
                        series: [
                            {
                                color: '#cf3146'
                            }
                        ],
                        axesDefaults: {
                            labelRenderer: $.jqplot.CanvasAxisLabelRenderer
                        },
                        seriesDefaults: {
                            rendererOptions: {
                                smooth: true
                            }
                        },
                        grid: {
                            drawGridLines: true,
                            gridLineColor: '#cccccc',
                            background: '#ffffff',
                            borderColor: '#ffffff',
                            borderWidth: 2.0,
                            shadow: false,
                            renderer: $.jqplot.CanvasGridRenderer,
                            rendererOptions: {}
                        },
                        axes: {
        
                            xaxis: {
                                label: "Month 2017",
                                pad: 0,
                                tickOptions: {
                                    showGridline: false
                                }
                            },
                            yaxis: {
                                label: "Total Number of Users"
                            }
                        }
                    });
    
                    var plot7 = $.jqplot('chart7', [[0, 7, 9, 1, 5, 3, 8, 2, 5]], {
                        animate: true,
                        // Will animate plot on calls to plot1.replot({resetAxes:true})
                        animateReplot: true,
                        cursor: {
                            show: true,
                            zoom: true,
                            looseZoom: true,
                            showTooltip: true
                        },
                        series: [
                            {
                                color: '#c18f55'
                            }
                        ],
                        axesDefaults: {
                            labelRenderer: $.jqplot.CanvasAxisLabelRenderer
                        },
                        seriesDefaults: {
                            rendererOptions: {
                                smooth: true
                            }
                        },
                        grid: {
                            drawGridLines: true,
                            gridLineColor: '#cccccc',
                            background: '#ffffff',
                            borderColor: '#ffffff',
                            borderWidth: 2.0,
                            shadow: false,
                            renderer: $.jqplot.CanvasGridRenderer,
                            rendererOptions: {}
                        },
                        axes: {
        
                            xaxis: {
                                label: "Month 2017",
                                pad: 0,
                                tickOptions: {
                                    showGridline: false
                                }
                            },
                            yaxis: {
                                label: "Total Number of Users"
                            }
                        }
                    });
    
                    var plot8 = $.jqplot('chart8', [[0, 7, 9, 1, 5, 3, 8, 2, 5]], {
                        animate: true,
                        // Will animate plot on calls to plot1.replot({resetAxes:true})
                        animateReplot: true,
                        cursor: {
                            show: true,
                            zoom: true,
                            looseZoom: true,
                            showTooltip: true
                        },
                        series: [
                            {
                                color: '#744499'
                            }
                        ],
                        axesDefaults: {
                            labelRenderer: $.jqplot.CanvasAxisLabelRenderer
                        },
                        seriesDefaults: {
                            rendererOptions: {
                                smooth: true
                            }
                        },
                        grid: {
                            drawGridLines: true,
                            gridLineColor: '#cccccc',
                            background: '#ffffff',
                            borderColor: '#ffffff',
                            borderWidth: 2.0,
                            shadow: false,
                            renderer: $.jqplot.CanvasGridRenderer,
                            rendererOptions: {}
                        },
                        axes: {
        
                            xaxis: {
                                label: "Month 2017",
                                pad: 0,
                                tickOptions: {
                                    showGridline: false
                                }
                            },
                            yaxis: {
                                label: "Total Number of Users"
                            }
                        }
                    });
    
                    var plot9 = $.jqplot('chart9', [[0, 7, 9, 1, 5, 5, 8, 2, 10]], {
                        animate: true,
                        // Will animate plot on calls to plot1.replot({resetAxes:true})
                        animateReplot: true,
                        cursor: {
                            show: true,
                            zoom: true,
                            looseZoom: true,
                            showTooltip: true
                        },
                        series: [
                            {
                                color: '#f8ec0f'
                            }
                        ],
                        axesDefaults: {
                            labelRenderer: $.jqplot.CanvasAxisLabelRenderer
                        },
                        seriesDefaults: {
                            rendererOptions: {
                                smooth: true
                            }
                        },
                        grid: {
                            drawGridLines: true,
                            gridLineColor: '#cccccc',
                            background: '#ffffff',
                            borderColor: '#ffffff',
                            borderWidth: 2.0,
                            shadow: false,
                            renderer: $.jqplot.CanvasGridRenderer,
                            rendererOptions: {}
                        },
                        axes: {
        
                            xaxis: {
                                label: "Month 2017",
                                pad: 0,
                                tickOptions: {
                                    showGridline: false
                                }
                            },
                            yaxis: {
                                label: "Total Number of Manuals Downloded"
                            }
                        }
                    });
                }, 100);
            });

            $(document).on('click','[data-toggle="trigger"]', function(){
                var x = $(this).data('target');
                $(document).find(x).trigger('click');
            });

        });
