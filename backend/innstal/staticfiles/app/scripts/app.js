
var app = angular.module("innstalApp", ['ui.router']);

app.config(function ($stateProvider, $locationProvider, $urlRouterProvider) {
    $locationProvider.hashPrefix('');
    $urlRouterProvider.otherwise("/");
    $stateProvider
        .state('/', {
            url: '/',
            templateUrl: '/static/app/index.html',
        })
        .state('join', {
            url: '/user/user/register',
            templateUrl: '/static/app/views/sign-up.html',
        })
        .state('login', {
            url: '/user/user/login',
            templateUrl: '/static/app/views/signin.html',
        })
})