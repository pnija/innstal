
var app = angular.module('innstalApp');

app.controller('logincontroller', ['$scope', '$http', '$window',  function($scope, $http, $window ){
    $scope.submitted = false;

    $scope.login = function (logindata) {
        alert()

        $scope.logindata = logindata;

        $http({
            method: 'POST',
            url: 'user/login/',
            data: logindata,
        }).then(function (response) {
                $scope.user = {};
                $scope.regForm = {};

                $window.location.href = 'user/dashboard/';

            }, function (response) {
                console.log('i am in error');
//                $modalInstance.dismiss('cancel');
        });
    };

}])