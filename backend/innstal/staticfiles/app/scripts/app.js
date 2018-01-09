
var app = angular.module("innstalApp", ['ui.router']);

app.config(function ($stateProvider, $locationProvider, $urlRouterProvider) {
    $locationProvider.hashPrefix('');
    $urlRouterProvider.otherwise("/");
    $stateProvider
        .state('/', {
            url: '/',
            templateUrl: '/static/app/index.html',
        })
        .state('dashboard', {
            templateUrl: '/static/app/views/dashboard.html',
        })
})