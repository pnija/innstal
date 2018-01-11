
var app = angular.module('innstalApp');

app.controller('logincontroller',  function($scope, $http, $state){
    $scope.submitted = false;

    $scope.login = function (logindata) {

        $scope.logindata = logindata;

        $http({
            method: 'POST',
            url: 'user/login/',
            data: logindata,
        }).then(function (response) {
                console.log('sgdfhgdsfhsd');
                $scope.logindata = {};
                $scope.loginForm = {};
                $state.go("dashboard");

            }, function (response) {
                console.log('i am in error');
//                $modalInstance.dismiss('cancel');
        });
    };

})

