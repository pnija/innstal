
angular.module('innstal.controllers', [])
    .controller('basecontroller', function($scope, $state, $modal, $window) {
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
    })
    .controller('logincontroller', function($scope, $http, $state, $window) {
        $scope.submitted = false;

        $scope.login = function (logindata) {

            $scope.logindata = logindata;

            $http({
                method: 'POST',
                url: 'user/login/',
                data: logindata,
            }).then(function (response) {

                    $scope.logindata = {};
                    $scope.loginForm = {};

                    $window.sessionStorage.token = response.data.token;

                    $state.go('dashboard')
                }, function (response) {
                    console.log('i am in error');
            });
        };

    })
    .controller('joinincontroller', function($scope, $http, $window) {
        $scope.submitted = false;

        $scope.submit = function (user) {
            $scope.user = user;

            $http({
                method: 'POST',
                url: 'user/register/',
                data: user,
            }).then(function (response) {

                    $scope.user = {};
                    $scope.regForm = {};

                }, function (response) {
                    console.log('i am in error');
            });
        };

    })
    .controller('dashboardcontroller', function($scope, $http, $window) {
        $http({
            method: 'GET',
            url: 'user/profile/',
        }).then(function (response) {
                $scope.userid = response.data.user_id;

                alert($scope.userid);

            }, function (response) {
                console.log('i am in error');
        });

    })
    .controller('dashboardhomecontroller', function($scope, $http, $window) {
       $scope.user_id = null;
       alert($scope.userid);
    })