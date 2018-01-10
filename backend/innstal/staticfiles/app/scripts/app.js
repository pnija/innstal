var app = angular.module("innstalApp", ['ui.router', 'ui.bootstrap']);

app.config(function ($stateProvider, $locationProvider, $urlRouterProvider) {
    $locationProvider.hashPrefix('');
    $urlRouterProvider.otherwise("/");
    $stateProvider
        .state('/', {
            url: '/',
            templateUrl: '/static/app/index.html',
            controller: 'basecontroller',
        })
        .state('dashboard', {
            templateUrl: '/static/app/views/dashboard.html',
        })
        .state('contact', {
            url: '/contact',
            templateUrl: '/static/app/views/contact-us.html',
        })        
});

app.controller('basecontroller', ['$scope', '$http', '$modal', '$state', function($scope, $http, $modal, $state){
    $scope.subscribe = function () {
        var params = $.param({firstname: $scope.firstname, email: $scope.subscribe_email});

        $http({
            method: 'POST',
            url: 'user/subcribe/newsletter/',
            data: params,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then(function (response) {
                $scope.firstname = '';
                $scope.subscribe_email = '';
            }, function (response) {
                console.log('i am in error');
        });
    };

}])