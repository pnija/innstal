
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
            url: '/login',
            templateUrl: '/static/app/views/signin.html',
            controller: 'logincontroller',
        })
        .state('register', {
            url: '/register',
            templateUrl: '/static/app/views/sign-up.html',
            controller: 'joinincontroller',
        })
        .state('dashboard', {
            url: '/dashboard',
            templateUrl: '/static/app/views/dashboard.html',
            controller: 'dashboardcontroller',
        })
        .state('dashboard_home', {
            url: '/dashboard',
            templateUrl: '/static/app/views/dashboard.html',
            controller: 'dashboardhomecontroller',
        })
        .state('blog', {
            url: '/blog',
            templateUrl: '/static/app/views/blog-homepage.html',
            controller: 'bloghomecontroller',
        })
        .state('blog-detail', {
            url: '/blog/:id',
            params: { id : null },
            templateUrl: '/static/app/views/blog-details.html',
            controller: 'blogdetailcontroller',
        })
        .state('contact', {
            url: '/contact',
            templateUrl: '/static/app/views/contact-us.html',
        })
        .state('warranty', {
            url: 'user/warranty',
            templateUrl: '/static/app/views/register-for-warranty.html',
            controller: 'warrantyregistercontroller',
        })
})
.run(function($http, $window) {
    if($window.sessionStorage.token){
        $http.defaults.headers.common.Authorization = 'Token '+$window.sessionStorage.token;
    }
});