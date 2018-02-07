
angular.module("innstalApp", ['innstal.controllers','ui.router', 'ui.bootstrap'])
.config(function ($stateProvider, $locationProvider, $urlRouterProvider) {
    $locationProvider.hashPrefix('');
    $urlRouterProvider.otherwise('/');
    $stateProvider
        .state('home', {
            url: '/',
            templateUrl: '/static/app/base.html',
            controller: 'basecontroller',
            cache: false,
        })
        .state('login', {
            url: '/login',
            templateUrl: '/static/app/views/signin.html',
            controller: 'logincontroller',
            cache: false,
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
        .state('business', {
            url: '/business',
            templateUrl: '/static/app/views/business.html',
            controller: 'businesscontroller',
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
            cache: false,
        })
        .state('blog-detail', {
            url: '/blog/:id',
            params: { id : null },
            templateUrl: '/static/app/views/blog-details.html',
            controller: 'blogdetailcontroller',
            cache: false,
        })
        .state('contact', {
            url: '/contact',
            templateUrl: '/static/app/views/contact-us.html',
        })
        .state('warranty', {
            url: '/warranty',
            templateUrl: '/static/app/views/register-for-warranty1.html',
            controller: 'warrantyregistercontroller',
        })
        .state('activate', {
            url: '/activate/:id',
            params: { id : null },
            templateUrl: '/static/app/views/signin.html',
            controller: 'logincontroller',
        })
        .state('change_password', {
            url: '/change_password/:id/:token/',
            params: { id : null , token : null},
            templateUrl: '/static/app/views/new-password.html',
            controller: 'changepasswordcontroller',
        })
        .state('search-results', {
            url: '/product/search-results/:searchText',
            templateUrl: '/static/app/views/search-results.html',
            controller: 'searchResultController'
        })
        .state('profile', {
            url: '/profile/',
            templateUrl: '/static/app/views/general_profile.html',
            controller: 'profileController'
        })
        .state('login-next', {
            url: '/login/?next',
            templateUrl: '/static/app/views/signin.html',
            controller: 'loginnextcontroller',
            cache: false,
        })
})
.run(function($rootScope, $http, $window, $state) {
    console.log('runnnnnnnnnnnn')
    $rootScope.logout = function() {
        $http({
                method: 'GET',
                url: 'user/logout/',
                headers: {'Authorization': 'Token '+$window.sessionStorage.token}
            }).then(function (response) {
                $window.sessionStorage.clear();
                $rootScope.user_id = '';
                $state.go('home');

                }, function (response) {
                    console.log('i am in error');
            });
    };
    if($window.sessionStorage.token){
        $rootScope.user_id = $window.sessionStorage.token;
    }
    else{
        $rootScope.user_id = null;
    }
})
