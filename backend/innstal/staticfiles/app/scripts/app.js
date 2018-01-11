
angular.module("innstalApp", ['innstal.controllers','ui.router', 'ui.bootstrap'])
.config(function ($stateProvider, $locationProvider, $urlRouterProvider) {
    $locationProvider.hashPrefix('');
    $stateProvider
        .state('home', {
            url: '',
            templateUrl: '/static/app/base.html',
            controller: 'basecontroller',
        })
        .state('login', {
            url: 'user/login',
            templateUrl: '/static/app/views/signin.html',
            controller: 'logincontroller',
        })
        .state('register', {
            url: 'user/register',
            templateUrl: '/static/app/views/sign-up.html',
            controller: 'joinincontroller',
        })
        .state('dashboard', {
            url: 'user/dashboard',
            templateUrl: '/static/app/views/dashboard.html',
            controller: 'dashboardcontroller',
        })
        .state('dashboard_home', {
            url: 'user/dashboard',
            templateUrl: '/static/app/views/dashboard.html',
            controller: 'dashboardhomecontroller',
        })
        .state('blog', {
            url: 'user/blog',
            templateUrl: '/static/app/views/blog-homepage.html',
        })
        .state('contact', {
            url: '/contact',
            templateUrl: '/static/app/views/contact-us.html',
        })
        .state('warranty', {
            templateUrl: '/static/app/views/warranty-register.html',
        })
})
.run(function($http, $window) {
    if($window.sessionStorage.token){
        $http.defaults.headers.common.Authorization = 'Token '+$window.sessionStorage.token;
    }
});